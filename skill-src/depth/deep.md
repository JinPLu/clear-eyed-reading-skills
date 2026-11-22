---
name: "clear-eyed-deep-reading"
description: "Deeply read a research paper, review, technical blog, commentary, or other long technical work so the reader can retell, redraw, reuse, and challenge it, through a plain-language rebuild of the problem and mechanism with text diagrams and one worked example carried through every step, key equations with numbers, decisive figures, experimental completeness, and implementation details, plus what is really new versus the closest earlier work, where its ability comes from, why its result came out that way, and checks of venue/tier, reviews, versions, code, reproductions, and community value (citations, GitHub stars, Hugging Face votes). Available only when the user explicitly invokes this skill. Do not use for a quick summary, full translation, formal peer review, or accept/reject recommendation."
display_name: "Clear-Eyed Deep Reading"
short_description: "Rebuild a work step by step: mechanism, real novelty, evidence, and community value"
default_prompt: "Use $clear-eyed-deep-reading to rebuild this work step by step in plain language, show what is actually new, and evaluate its evidence, completeness, and community value."
---

# Deep Reading

Purpose: full mastery — the reader finishes able to retell the work in plain words, redraw and hand-run the mechanism, reuse or reimplement it without hidden traps, and challenge the verdict.

Research at full depth:

- Read the full text, appendices, decisive figures and tables, equations, and the implementation or analysis details that matter. Audit manuscript richness and experimental completeness (baseline breadth, ablations, scaling/robustness checks, failure taxonomy, figure/table density, appendix depth). Cross-check the paper, appendix, official code and configs, reviews, and reproductions; report material discrepancies plainly and never invent missing details. Separate inference from training, observation from intervention, and assumptions from consequences.
- Check all six kinds of outside material — including Semantic Scholar / Google Scholar citation counts and how citing work uses the paper, GitHub stars/issues/maintenance, and Hugging Face votes/cards/adoption — and cross-check them against what is new, why the result appears, and what community value the work delivers. Name what was not found.
- Test every important claimed contribution against earlier work found by at least two independent routes, reading primary texts until further searching is unlikely to change any of the four answers, and record remaining gaps.

Write the same six sections, fully expanded:

- **Problem:** the background needed, earlier approaches, and the exact bottleneck where they fell short.
- **How it works:** the main diagram (plus a second if training and inference or two branches genuinely differ), then every module in turn with the **same running example** carried through each module, dimension, state, population, or decision. Walk through online operation / inference end-to-end first, then explain how training teaches the trainable parts when training differs. Include every non-trivial equation needed to follow or reproduce the mechanism, with the running example's numbers plugged in. Cover implementation details that change understanding, reproduction, or the result; mention routine settings in a line.
- **What is new:** a table row for every important claimed contribution (with primary-text check status noted on the earlier work), followed by what kind of contribution each is — a new problem, dataset or measurement, representation, method, theory, evidence, tool or system integration, synthesis, reliable negative result, or replication.
- **Why the result came out this way:** the evidential setup and **experimental completeness** suited to the kind of work. For experiments: data, baselines and their fairness, metrics, main results, ablations, scaling/robustness, failure cases, and whether the manuscript's evidence layout is thorough or selective. Guide the reader through the 1–3 original figures that matter most — figure number, where to look, and what pattern or exception each shows. Integrate findings from reviews, versions, code, issues, and reproductions where they change the picture.
- **Worth and use:** synthesize **paper & community value** — publication venue and tier, manuscript richness and experimental thoroughness (reading ROI), reusable open artifacts or empirical lessons, and time-contextualized traction (Semantic Scholar / Google Scholar citations and citing stance, GitHub stars and maintenance, Hugging Face votes/adoption) — plus who should read or use it, reproduction caveats, and, for a complete research paper, the five integer scores with evidence-based reasons.

If the answer is too long for one response, split it cleanly at section boundaries (for example sections 1–3, then 4–6) rather than by page count, and do not repeat conclusions.
