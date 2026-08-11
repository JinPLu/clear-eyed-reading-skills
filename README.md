# Paper Demystifier Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Harness](https://img.shields.io/badge/Harness-agnostic-2563EB)](#harness-and-language)

Read past the terminology. **Locate the work in its field, disassemble the method, test the decisive evidence, and separate genuine contribution from hype.**

![Comic map of the quick-reading and deep-reading paths](assets/paper-demystifier-map-v2.png)

> Current version: `v0.1`. Both skills pass structural validation and are being tested across disciplines, article types, languages, and agent environments.

## 🧭 Choose a Skill

| What you need | Skill | What it produces |
| --- | --- | --- |
| ⚡ “Help me understand this quickly, assess the novelty, and find the hype.” | [`clear-eyed-paper-reading`](skills/clear-eyed-paper-reading/SKILL.md) | A compact explanation, decisive evidence, five-dimension assessment, and bottom line |
| 🔬 “Deep-read every section, figure, table, equation, and experiment.” | [`clear-eyed-paper-deep-reading`](skills/clear-eyed-paper-deep-reading/SKILL.md) | A field map, runnable method model, complete evidence chain, and final assessment |

In one line: **use quick reading to decide whether a work deserves attention; use deep reading to understand it well enough to explain, reuse, or challenge it.**

The two skills are intentionally separate. A simple reading request should not trigger an exhaustive workflow, and a genuine deep-reading request should not collapse into a summary.

## 🌐 Harness and Language

- **Harness-agnostic core**: All essential behavior lives in plain Markdown `SKILL.md` files. The skills require no specific model, MCP server, CLI, filesystem layout, or platform API.
- **English instructions, no fixed output language**: The skill instructions are written in English for precision. Output language is determined by the user request, active conversation, and host model.
- **Optional platform metadata**: `agents/openai.yaml` supplies display metadata for OpenAI products. Other harnesses can ignore it without changing skill behavior.

Any agent harness that can load skill instructions can use the core skills. The harness remains responsible for document access, web research, citation tools, and other environment-specific capabilities.

## ✨ How Demystification Works

Both reading depths use the same standard:

1. 🌍 **Restore the field context**: independently identify direct precedents instead of repeating Related Work.
2. ⚙️ **Disassemble the method**: reduce it to ordinary components and expose capabilities supplied by prompts, labels, rules, or external models.
3. 📊 **Test the evidence**: distinguish “the system won,” “this module caused the win,” and “the authors' explanation is correct.”
4. ⚖️ **Converge on a verdict**: state which claim must be narrowed and what remains valuable afterward.

The critical tone applies only to claims, evidence, and reasoning—not to authors. Every strong judgment should trace back to the source text, a figure, a table, an equation, or an independently verified precedent.

## 🚀 Install

Each skill is self-contained. Install the entire chosen directory into the skill search path used by your harness. If the harness accepts only a single instruction file, import the corresponding `SKILL.md`.

Platform-specific examples below are illustrations, not requirements.

### ChatGPT example

Import each desired `SKILL.md` through the interface that supports personal skills.

- [Clear-Eyed Article Reading](skills/clear-eyed-paper-reading/SKILL.md)
- [Clear-Eyed Deep Reading](skills/clear-eyed-paper-deep-reading/SKILL.md)

### Codex example

```bash
cp -R skills/clear-eyed-paper-reading ~/.codex/skills/
cp -R skills/clear-eyed-paper-deep-reading ~/.codex/skills/
```

## 💬 Use

Quick reading:

```text
Use $clear-eyed-paper-reading to explain and critically assess this paper: <link or attachment>
```

Deep reading:

```text
Use $clear-eyed-paper-deep-reading to explain the background, method, equations, every figure, and the experiments: <link or attachment>
```

Prompts may be written in any language. The skills do not prescribe a default output language.

## 🗂️ Project Layout

```text
paper-demystifier-skills/
├── assets/
│   ├── paper-demystifier-map.png
│   └── paper-demystifier-map-v2.png
├── skills/
│   ├── clear-eyed-paper-reading/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── clear-eyed-paper-deep-reading/
│       ├── SKILL.md
│       └── agents/openai.yaml
├── evals/cases.yaml
├── CONTRIBUTING.md
└── LICENSE
```

## ✅ Development and Validation

Changes should preserve these properties:

- The two trigger descriptions remain mutually exclusive.
- Core instructions remain harness-neutral and introduce no platform dependency.
- The skills impose no default output language.
- ⚡ Quick reading stays compact and does not expand into a section-by-section review.
- 🔬 Deep reading accounts for every figure and table, key equations, and relevant appendices.
- Novelty and significance rely on independent field positioning rather than author self-description.
- Conclusions remain concrete and traceable instead of manufacturing criticism from generic limitations.

Regression cases live in [`evals/cases.yaml`](evals/cases.yaml). Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before contributing and [`SECURITY.md`](SECURITY.md) for security reporting.

Released under the [MIT License](LICENSE).

## 🔗 Format References

- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI: Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
