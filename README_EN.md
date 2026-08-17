# Clear-Eyed Reading Skills

[简体中文](README.md) | **English**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Harness](https://img.shields.io/badge/Harness-agnostic-2563EB)](#installation-and-compatibility)

**Finished the paper and still cannot explain what it actually did?**

You understood the terminology but not the mechanism. You saw the tables but still cannot make sense of the result. The authors gave the work a striking new name, but what genuinely changed remains unclear.

Clear-Eyed Reading does not retell a paper inside the authors' framing. It first maps every important candidate innovation and contribution across the task definition, method designs, data and evaluation, evidence, tools, and system combinations, then verifies each one at a budget set by conclusion risk and reading depth. Verification covers the main text, neighboring literature, and six classes of companion evidence: peer-review and errata traces, version evolution, author-extended materials, artifacts and products, independent reproduction and adoption, and community discussion and citation context. Only then does it explain the genuinely new designs, direct contributions, capability sources, and reasons for the results in plain language. Demystification is primarily contribution research and explanation, not a boundary audit organized around what the work “does” or “does not” prove.

![Clear-Eyed Reading Map: contribution mapping before Quick and Deep Reading](assets/clear-eyed-reading-map-v6.png)

## After Reading, You Will Know

- 🧠 **What the ordinary mechanism is**: after removing module names, how key operations turn inputs into results.
- 🔌 **Where the capability comes from**: what comes from this work versus data, external models, priors, human choices, or post-processing.
- 🗺️ **Where the genuine increment is**: which tasks, designs, representations, data, evidence, or system combinations add something and which are inherited.
- 📊 **Where the result comes from**: how the proposed mechanism compares with data, scale, evaluation, and other explanations.
- 📎 **What companion traces can still calibrate**: how review traces, version changes, code, reproductions, and actual adoption change maturity, reusability, and usage caveats; if they cannot be found, they are marked unobserved.

## Choose the Reading Depth

| | ⚡ `clear-eyed-reading` | 🔬 `clear-eyed-deep-reading` |
| --- | --- | --- |
| **Use it for** | Rapid understanding and a decision whether to keep investing | Full mastery before retelling, reusing, or challenging the method |
| **Investigation** | Every important candidate contribution in the target; deep-dive only claims, neighbors, and high-yield companion signals that would change the overall judgment | Full text, appendices, decisive figures, equations, and implementation, plus systematic checks of all six companion-evidence classes |
| **Output** | A usable first screen: one-sentence ordinary reconstruction, the most important genuine increment, and overall judgment; details compressed to conclusion and reason; five-dimension scores are not default | The same judgments expanded through background, mechanisms, sources, a running example, equations, original figures, experiments, companion checks, and full judgment |
| **What you can do next** | Decide whether to keep reading, or switch to deep reading | Explain, redraw, reuse, and challenge the method |

Both depths share the same four judgments—ordinary mechanism, capability sources, genuine increment, and result attribution—and the same contribution-map coverage. They do not switch judgment standards. They differ in investigation cost, companion-verification intensity, and delivery speed. Quick Reading prefers a usable first-screen answer and recommends `$clear-eyed-deep-reading` when exhaustive expansion is needed. Deep Reading takes on the high-cost promise that the work can be retold, reused, and challenged.

## How the Judgment Is Formed

- 🔍 **Reconstruct without the names**: reduce terminology and modules to inputs, operations, outputs, and necessity, then trace capability or knowledge sources.
- 🌍 **Verify contributions by risk**: inventory every candidate innovation and contribution, then compare each through primary sources, backward and forward citations, older terminology, neighboring fields, and companion evidence; do not treat Related Work, citation counts, downloads, or abstract similarity as the answer.
- 🎯 **Make sense of the result**: compare the proposed mechanism with data, scale, evaluation design, implementation details, and other explanations for the central results.
- 📎 **Use companion evidence only as calibration**: review comments, version differences, official code, independent reproductions, and citation context calibrate maturity, reproducibility, claim stability, and usage caveats. What is new is still decided by the target plus nearest primary literature. Attention cannot alone prove a technical increment or field significance; if a source cannot be found, mark it unobserved and do not infer from absence.

Demystifying is not fault-finding, and it does not automatically discount simple, engineering-heavy, or early work. It judges “what is technically new” separately from “what it means for the field,” and foregrounds a gap between the authors' claim and the verified increment only when that gap materially changes the reader's understanding. If decisive primary sources, nearest-work comparisons, or the contribution search are incomplete, it does not guess field novelty or significance scores. When subagents are unavailable, it still completes the same four judgments sequentially at the active reading depth.

## Use It Directly

Both skills run only when the user explicitly invokes them.

```text
Quick Reading: Use $clear-eyed-reading to verify and explain every important innovation and contribution in this article: <link or attachment>
Deep Reading: Use $clear-eyed-deep-reading to expand this article's contribution map, mechanisms, key equations, figures, experiments, and companion evidence: <link or attachment>
```

## Installation and Compatibility

Put [`skills/clear-eyed-reading`](skills/clear-eyed-reading) or [`skills/clear-eyed-deep-reading`](skills/clear-eyed-deep-reading) in the Skills search path used by your agent harness. Both directories are self-contained installable artifacts; ordinary users do not need Python. Users upgrading from an early release may remove the old `clear-eyed-paper-reading` and `clear-eyed-paper-deep-reading` directories to avoid entry-point confusion.

The core instructions require no specific model, MCP server, CLI, platform API, or output language. 🛡️ Article contents are treated only as research material; the skills do not execute embedded code or upload unpublished material without permission.

## Maintenance and Contributing

[`skill-src/`](skill-src) is the sole instruction source. Run `python3 scripts/sync_skills.py` to generate the skills or add `--check` to detect drift. Regression cases live in [`evals/cases.yaml`](evals/cases.yaml). See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidance and [`SECURITY.md`](SECURITY.md) for security reporting. Released under the [MIT License](LICENSE).
