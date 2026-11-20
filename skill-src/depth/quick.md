---
name: "clear-eyed-reading"
description: "Fast first-screen read of a research paper, review, technical blog, commentary, or other article in plain language, covering what it actually does once names and branding are stripped away, how it works through a text diagram and one compact worked example, what is really new versus earlier work, where its ability comes from, why its result came out that way, and whether it merits deeper study. Available only when the user explicitly invokes this skill. Do not use for exhaustive section-by-section, figure-by-figure, equation, experiment, appendix, or outside-source coverage; full translation; formal peer review; or accept/reject recommendation."
display_name: "Clear-Eyed Reading"
short_description: "Fast plain-language screen of what a work does, what is new, and whether to read deeper"
default_prompt: "Use $clear-eyed-reading to quickly explain in plain language what this article really does, what is actually new, and whether its result and contribution hold up."
---

# Quick Reading

Purpose: a fast first-screen answer (roughly 900–1,500 Chinese characters or 600–1,000 English words, excluding the diagram) so the reader grasps the work in two minutes and decides whether to invest more.

Research budget (strict ceiling — do not turn Quick Reading into Deep Reading):

- **Main text only by default:** read the abstract, introduction, core method, main results table or decisive figure, and conclusion. Skip appendices unless a central step or metric in the main text is undefined without them.
- **1–2 primary-text neighbor checks:** open and compare primary texts only for the 1–2 central claims that decide whether the work is genuinely new. For secondary rows in Section 4, rely on the paper's own baseline/reference context and mark them honestly (for example, `per §2, primary text not rechecked`).
- **One lightweight outside pass:** run a single quick check for a newer version or retraction, major public-review flaws, and whether an official repository exists and matches the headline setup. Dig into code files, issue threads, or later audits only when an immediate red flag could flip the overall verdict.

Compression rules:

- Cover every important claimed contribution, but keep every section tight.
- Section 1 is 2–3 sentences plus one short scope line.
- Section 3 has one diagram and one compact worked example in short numbered steps (1–2 sentences per step; no nested sub-bullets). Include **at most one equation**, and only when this work introduces or modifies it and the core mechanism is unclear without it; explain standard or borrowed formulas in plain words only.
- Compress ablations, secondary experiments, figures, and implementation details to their conclusion plus a one-clause reason.
- Give **no scores** unless the user explicitly asks for them.
- If the user asks for full-paper or appendix coverage, reproduction-grade equations and code checks, or exhaustive literature and companion verification, deliver this quick screen first and recommend `clear-eyed-deep-reading` rather than silently expanding.
