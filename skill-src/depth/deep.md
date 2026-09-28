---
name: "clear-eyed-deep-reading"
description: "Deeply read a research paper, review, technical blog, commentary, or other long technical work so the reader can retell, redraw, reuse, and challenge it, through a plain-language rebuild of the problem and mechanism with text diagrams and one worked example carried through every step, key equations with numbers, decisive figures, experiments, and implementation details, plus what is really new versus the closest earlier work, where its ability comes from, why its result came out that way, and checks against reviews, versions, code, and reproductions. Available only when the user explicitly invokes this skill. Do not use for a quick summary, full translation, formal peer review, or accept/reject recommendation."
display_name: "Clear-Eyed Deep Reading"
short_description: "Rebuild a work step by step: mechanism, real novelty, evidence, and checks"
default_prompt: "Use $clear-eyed-deep-reading to rebuild this work step by step in plain language, show what is actually new, and explain why its result or conclusion comes out that way."
---

# Deep Reading

Purpose: the reader can retell the work in plain words, redraw and run the mechanism, reuse or reimplement it, and challenge the verdict.

Research at full depth:

- Read the full text, appendices, decisive figures and tables, equations, and the implementation or analysis details that matter. Note material differences among the paper, appendix, official code, reviews, and reproductions; do not invent missing details. Separate training from inference, observation from intervention, and assumptions from consequences when relevant.
- Check all six kinds of material around the work and cross-check them against what is new and why the result appears. Name what was not found.
- Test each central claimed contribution against earlier work found by at least two independent routes. Stop only when further searching turns up nothing that would change an answer, and record the remaining gaps.

Write the same six sections, expanded:

- **Problem:** the background needed, earlier approaches, and exactly where they fell short.
- **How it works:** the main diagram, then every module in turn with the same running example carried through each module, dimension, state, population, or decision. Include every equation needed to follow the mechanism, with numbers. Cover implementation details that change understanding, reproduction, or the result; mention routine settings in a line.
- **What is new:** a table row for every important contribution, and the kind of contribution each is — a new problem, dataset or measurement, representation, method, theory, evidence, tool or system integration, synthesis, reliable negative result, or replication.
- **Why the result came out this way:** the evidential setup suited to the kind of work. For experiments: data, baselines and their fairness, metrics, main results, ablations, robustness, and failures. Guide the reader through the one to three figures that matter most — where to look and what each adds. Put findings from reviews, versions, code, and reproductions where they change the picture.
- **Use:** who should use it, for what, with which reuse caveats, and — for a complete research paper — the five scores.

If the answer is too long for one response, split it at section boundaries (for example sections 1–3, then 4–6) rather than by page count, and do not repeat conclusions.
