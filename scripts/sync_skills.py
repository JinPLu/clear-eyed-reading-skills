#!/usr/bin/env python3
"""Compose and validate self-contained reading skills from shared sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "skill-src"
EVALS_PATH = ROOT / "evals" / "cases.yaml"
TARGETS = {
    "quick": ROOT / "skills" / "clear-eyed-reading",
    "deep": ROOT / "skills" / "clear-eyed-deep-reading",
}
METADATA_KEYS = {
    "name",
    "description",
    "display_name",
    "short_description",
    "default_prompt",
}
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_profile(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    frontmatter, separator, body = text[4:].partition("\n---\n")
    if not separator:
        raise ValueError(f"{path}: unterminated frontmatter")

    metadata: dict[str, str] = {}
    for line in frontmatter.splitlines():
        key, separator, value = line.partition(":")
        if not separator or key not in METADATA_KEYS:
            raise ValueError(f"{path}: unsupported metadata line: {line}")
        metadata[key] = json.loads(value.strip())

    missing = METADATA_KEYS - metadata.keys()
    if missing:
        raise ValueError(f"{path}: missing metadata: {', '.join(sorted(missing))}")
    return metadata, body.strip()


def quote_yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def validate_metadata(target: Path, metadata: dict[str, str]) -> list[str]:
    errors: list[str] = []
    name = metadata["name"]
    if name != target.name:
        errors.append(f"{target}: metadata name {name!r} != dir name {target.name!r}")
    if not KEBAB_RE.match(name):
        errors.append(f"{target}: invalid kebab-case skill name {name!r}")
    if ": " in metadata["description"]:
        errors.append(
            f"{target}: description contains ': ' which breaks unquoted YAML frontmatter"
        )
    if f"${name}" not in metadata["default_prompt"]:
        errors.append(
            f"{target}: default_prompt must explicitly invoke ${name}"
        )
    return errors


def validate_evals(valid_skills: set[str]) -> list[str]:
    """Validate evals/cases.yaml structure without external PyYAML dependency."""
    errors: list[str] = []
    if not EVALS_PATH.is_file():
        return [f"missing {EVALS_PATH.relative_to(ROOT)}"]

    lines = EVALS_PATH.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "version: 1":
        errors.append("evals/cases.yaml: line 1 must be 'version: 1'")
    if len(lines) < 2 or lines[1].strip() != "cases:":
        errors.append("evals/cases.yaml: line 2 must be 'cases:'")

    seen_ids: set[str] = set()
    current_id: str | None = None
    has_skill = False
    has_prompt = False
    expect_count = 0
    in_block_prompt = False

    def flush_case() -> None:
        nonlocal current_id, has_skill, has_prompt, expect_count, in_block_prompt
        if current_id is None:
            return
        if not has_skill:
            errors.append(f"evals/cases.yaml ({current_id}): missing skill")
        if not has_prompt:
            errors.append(f"evals/cases.yaml ({current_id}): missing prompt")
        if expect_count == 0:
            errors.append(f"evals/cases.yaml ({current_id}): empty expect list")
        current_id = None
        has_skill = False
        has_prompt = False
        expect_count = 0
        in_block_prompt = False

    for lineno, raw in enumerate(lines[2:], start=3):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if in_block_prompt:
            if raw.startswith("      "):
                continue
            in_block_prompt = False

        if raw.startswith("  - id: "):
            flush_case()
            cid = raw[len("  - id: ") :].strip()
            if not KEBAB_RE.match(cid):
                errors.append(
                    f"evals/cases.yaml:{lineno}: invalid case id {cid!r}"
                )
            if cid in seen_ids:
                errors.append(
                    f"evals/cases.yaml:{lineno}: duplicate case id {cid!r}"
                )
            seen_ids.add(cid)
            current_id = cid
        elif raw.startswith("    skill: "):
            skill = raw[len("    skill: ") :].strip()
            if skill not in valid_skills:
                errors.append(
                    f"evals/cases.yaml:{lineno}: unknown skill {skill!r}"
                )
            has_skill = True
        elif raw.startswith("    prompt: "):
            val = raw[len("    prompt: ") :].strip()
            if val in ("|-", "|"):
                in_block_prompt = True
                has_prompt = True
            elif val:
                has_prompt = True
        elif raw.startswith("    expect:"):
            continue
        elif raw.startswith("      - "):
            expect_count += 1
        else:
            errors.append(
                f"evals/cases.yaml:{lineno}: unexpected indentation or key: {raw}"
            )

    flush_case()
    if not seen_ids:
        errors.append("evals/cases.yaml: no cases found")
    return errors


def render_skill(metadata: dict[str, str], profile: str) -> str:
    core = (SOURCE_ROOT / "core.md").read_text(encoding="utf-8").strip()
    output = (SOURCE_ROOT / "output" / "chat.md").read_text(encoding="utf-8").strip()
    return (
        "---\n"
        f"name: {metadata['name']}\n"
        f"description: {metadata['description']}\n"
        "disable-model-invocation: true\n"
        "argument-hint: \"<paper URL, arXiv id, DOI, or local file>\"\n"
        "---\n\n"
        "<!-- Generated by scripts/sync_skills.py; edit skill-src instead. -->\n\n"
        f"{core}\n\n{profile}\n\n{output}\n"
    )


def render_openai_yaml(metadata: dict[str, str]) -> str:
    return (
        "interface:\n"
        f"  display_name: {quote_yaml(metadata['display_name'])}\n"
        f"  short_description: {quote_yaml(metadata['short_description'])}\n"
        f"  default_prompt: {quote_yaml(metadata['default_prompt'])}\n"
        "policy:\n"
        "  allow_implicit_invocation: false\n"
    )


def expected_files() -> tuple[dict[Path, str], list[str]]:
    files: dict[Path, str] = {}
    errors: list[str] = []
    valid_skills: set[str] = set()
    for profile_name, target in TARGETS.items():
        metadata, body = parse_profile(SOURCE_ROOT / "depth" / f"{profile_name}.md")
        errors.extend(validate_metadata(target, metadata))
        valid_skills.add(metadata["name"])
        files[target / "SKILL.md"] = render_skill(metadata, body)
        files[target / "agents" / "openai.yaml"] = render_openai_yaml(metadata)
    errors.extend(validate_evals(valid_skills))
    return files, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated files and evals schema without writing",
    )
    args = parser.parse_args()

    files, errors = expected_files()
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    stale: list[Path] = []
    for path, expected in files.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == expected:
            continue
        stale.append(path)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")

    if args.check and stale:
        for path in stale:
            print(f"out of sync: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    if not args.check:
        for path in stale:
            print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
