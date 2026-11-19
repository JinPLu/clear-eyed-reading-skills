# Repository Guidelines

## Project Structure & Module Organization

This repository packages two complementary reading skills:

- `skills/clear-eyed-reading/` contains the compact article-review workflow.
- `skills/clear-eyed-deep-reading/` contains the exhaustive paper-reading workflow.
- Each skill keeps its core instructions in `SKILL.md` and optional OpenAI interface metadata in `agents/openai.yaml`.
- `evals/cases.yaml` holds shared routing and behavior regression cases.
- `assets/` contains diagrams used by the bilingual `README.md` and `README_EN.md`.

Keep each skill self-contained. Do not add per-skill READMEs or changelogs, and do not merge the quick and deep workflows.

## Build, Test, and Development Commands

There is no build step or package manager. Useful checks are:

```sh
git diff --check
git diff -- skills/ evals/ README.md README_EN.md
rg 'name:|description:' skills/*/SKILL.md
```

`git diff --check` catches whitespace errors. Review the focused diff before committing, and run the relevant prompts from `evals/cases.yaml` in the target agent harness. At minimum, exercise cases for any routing, language, safety, or output-format behavior you changed.

## Coding Style & Naming Conventions

Write core skill instructions in concise, platform-neutral English; they must not force an output language or depend on a specific model, MCP, CLI, or API. Use kebab-case skill directories, and keep the directory name identical to the frontmatter `name`. YAML uses two-space indentation. `SKILL.md` frontmatter contains `name` and `description`, plus the generated invocation hints `disable-model-invocation: true` (explicit invocation only, as in Claude Code) and `argument-hint`; other harnesses ignore these. Edit `skill-src/` and regenerate with `scripts/sync_skills.py`; never hand-edit `skills/`. In `agents/openai.yaml`, ensure `default_prompt` explicitly invokes the matching skill, for example `$clear-eyed-reading`.

Add rules only for observed failures. Critique claims and evidence, never authors, and preserve the boundary between quick reading and exhaustive deep reading.

## Testing Guidelines

Regression cases use descriptive kebab-case IDs such as `quick-system-paper` and include `skill`, `prompt`, and observable `expect` statements. Add the smallest case that demonstrates a new failure or guards a changed behavior. Verify both positive behavior and nearby routing conflicts when editing trigger descriptions.

## Commit & Pull Request Guidelines

Recent history uses short, imperative, sentence-case subjects such as `Reframe project as clear-eyed reading`. Keep commits focused on one behavioral or documentation change. Pull requests should explain the observed problem, summarize the change, list evaluated case IDs, and note affected skills. Link relevant issues and include before/after output excerpts when behavior changes. Never attach unpublished papers or restricted review material; follow `SECURITY.md` for sensitive reports.
