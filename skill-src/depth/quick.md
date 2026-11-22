---
name: "clear-eyed-reading"
description: "Fast first-screen read of a research paper, review, technical blog, commentary, or other article in plain language, covering what it actually does once names and branding are stripped away, how it works through a text diagram and one compact worked example, what is really new versus earlier work, where its ability comes from, why its result came out that way, and its practical and community value (venue/tier, experimental completeness, manuscript richness, citations, GitHub stars, Hugging Face votes). Available only when the user explicitly invokes this skill. Do not use for exhaustive section-by-section, figure-by-figure, equation, experiment, appendix, or outside-source coverage; full translation; formal peer review; or accept/reject recommendation."
display_name: "Clear-Eyed Reading"
short_description: "Fast plain-language screen of mechanism, real novelty, evidence, and community value"
default_prompt: "Use $clear-eyed-reading to quickly explain in plain language what this article really does, what is actually new, whether its evidence holds up, and what value it offers."
---

# Quick Reading

Purpose: a fast first-screen answer (roughly 900–1,500 Chinese characters or 600–1,000 English words, excluding the diagram) so the reader grasps the work in two minutes and decides whether to invest more.

Research budget (strict ceiling — do not turn Quick Reading into Deep Reading):

- **Main text core + completeness scan:** read the abstract, introduction, core method, main results table or decisive figure, and conclusion, and note at a glance how complete the manuscript and experiments are (whether ablations, stress tests, failure analysis, and substantial appendices exist). Do not read appendices line by line unless a central step or metric in the main text is undefined without them.
- **1–2 primary-text neighbor checks:** open and compare primary texts only for the 1–2 central claims that decide whether the work is genuinely new. For secondary rows in Section 4, rely on the paper's own baseline/reference context and mark them honestly (for example, `per §2, primary text not rechecked`).
- **One lightweight outside & traction pass:** run a single quick check for publication venue and tier (journal, conference Oral/Spotlight/Poster, or preprint), newer versions or retractions, major public-review flaws, official repo status, and headline traction metrics — Semantic Scholar or Google Scholar citations, GitHub stars, and Hugging Face paper votes or model/dataset likes (noted alongside publication date). Dig into code files, issue threads, or later audits only when an immediate red flag could flip the overall verdict.

Compression rules:

- Cover every important claimed contribution, but keep every section tight.
- Section 1 is 2–3 sentences plus one short scope line.
- Section 3 has one diagram and one compact worked example in short numbered steps (1–2 sentences per step; no nested sub-bullets). Include **at most one equation**, and only when this work introduces or modifies it and the core mechanism is unclear without it; explain standard or borrowed formulas in plain words only.
- Compress ablations, secondary experiments, figures, and implementation details to their conclusion plus a one-clause reason, while noting in Section 5 whether experimental coverage is thorough or thin.
- In Section 6, include a compact **value snapshot** (publication venue/tier, manuscript/experimental completeness, concrete community value, and checked Scholar citations / GitHub stars / HF votes relative to release age). Give **no integer scores** unless the user explicitly asks for them.
- If the user asks for full-paper or appendix coverage, reproduction-grade equations and code checks, or exhaustive literature and companion verification, deliver this quick screen first and recommend `clear-eyed-deep-reading` rather than silently expanding.
