#!/usr/bin/env python3
"""Copy the self-contained skills into any agent-harness skills directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = ("clear-eyed-reading", "clear-eyed-deep-reading")
LEGACY_NAMES = (
    "clear-eyed-paper-reading",
    "clear-eyed-paper-deep-reading",
)

# Convenience discovery only. The skills do not depend on these harnesses.
# Unknown platforms: pass --dest <that-harness-skills-dir>.
DISCOVERY_DIRS = (
    Path.home() / ".claude" / "skills",
    Path.home() / ".codex" / "skills",
    Path.home() / ".config" / "opencode" / "skills",
    Path.home() / ".copilot" / "skills",
    Path.home() / ".cursor" / "skills",
    Path.home() / ".gemini" / "skills",
    Path.home() / ".hermes" / "skills",
    Path.home() / ".kiro" / "skills",
)


def skill_sources() -> dict[str, Path]:
    sources: dict[str, Path] = {}
    for name in SKILL_NAMES:
        path = ROOT / "skills" / name
        if not (path / "SKILL.md").is_file():
            raise SystemExit(f"missing installable skill: {path}")
        sources[name] = path
    return sources


def discovered_destinations() -> list[Path]:
    return sorted(path for path in DISCOVERY_DIRS if path.is_dir())


def resolve_destinations(explicit: list[Path], discover: bool) -> list[Path]:
    dests: list[Path] = []
    seen: set[Path] = set()
    for path in explicit:
        resolved = path.expanduser().resolve()
        if resolved not in seen:
            dests.append(resolved)
            seen.add(resolved)
    if discover:
        for path in discovered_destinations():
            resolved = path.resolve()
            if resolved not in seen:
                dests.append(resolved)
                seen.add(resolved)
    return dests


def install_into(dest: Path, sources: dict[str, Path], dry_run: bool) -> None:
    if not dry_run:
        dest.mkdir(parents=True, exist_ok=True)
    for legacy in LEGACY_NAMES:
        legacy_path = dest / legacy
        if legacy_path.exists():
            print(f"remove {legacy_path}")
            if not dry_run:
                shutil.rmtree(legacy_path)
    for name, source in sources.items():
        target = dest / name
        print(f"{source.relative_to(ROOT)} -> {target}")
        if dry_run:
            continue
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Install clear-eyed reading skills into agent-harness skills "
            "directories. The skills themselves are harness-agnostic; this "
            "script only copies folders."
        )
    )
    parser.add_argument(
        "--dest",
        action="append",
        type=Path,
        default=[],
        help="skills directory for any harness; repeatable. Created if missing.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="also install into every existing discovered personal skills directory",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print destination directories and exit",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print copy actions without writing",
    )
    args = parser.parse_args()

    discover = args.all or not args.dest
    dests = resolve_destinations(args.dest, discover=discover)

    if args.list:
        if not dests:
            print("no destinations; pass --dest <skills-dir>")
            return 1
        for dest in dests:
            print(dest)
        return 0

    if not dests:
        print(
            "no skills directories found; copy skills/<name> into your harness "
            "skills path, or pass --dest <skills-dir>",
            file=sys.stderr,
        )
        return 1

    sources = skill_sources()
    for dest in dests:
        install_into(dest, sources, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
