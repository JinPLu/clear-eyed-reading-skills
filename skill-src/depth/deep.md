---
name: "clear-eyed-deep-reading"
description: "Perform a complete, clear-eyed deep reading of a research paper, review, technical blog, commentary, or other long-form technical work. Reconstruct the problem and method for a reader with no field background, inspect key figures, and fully explain consequential equations, implementation details, experiments, genuine contribution, and evidence limits. Available only when the user explicitly invokes this skill. Do not use for a quick summary, full translation, formal peer review, or accept/reject recommendation."
display_name: "Clear-Eyed Deep Reading"
short_description: "Explain the method, details, evidence, and real contribution"
default_prompt: "Use $clear-eyed-deep-reading to explain this work's problem, method, details, experiments, real contribution, and evidence limits."
---

# Deep Reading Profile

Expand the shared analysis until a new reader can retell the problem, reconstruct the method, interpret the evidence, and understand the final judgment.

Cover the necessary background, the full method chain, and consequential implementation details where they matter. Explain details that change understanding, reproduction, or confidence in the conclusion; mention ordinary configuration briefly. Identify material differences between the paper, appendix, and official code, and do not invent missing details. Separate training from inference when relevant.

Include every equation needed to understand the method or conclusions, integrated into the step that uses it. Expand the running example across modules, dimensions, states, or decisions when that makes the mechanism concrete.

Explain the experimental setting, data, relevant baselines and fairness, metrics, main results, and the conclusion supported by those results. Then show what ablations, extensions, robustness checks, qualitative results, and failure cases add to the central contribution. Do not turn this coverage into a table recital or a search for minor defects.

Give special attention to the one to three original figures or crops most directly tied to the central claims. Explain how to read them and what they add; treat other figures according to their role.

Use the narrative spine `position the work → explain the problem → make the method understandable → interpret the experiments → form a judgment`. Let headings and length follow the paper rather than forcing a fixed chapter count. If the work is too long for one response, divide it by complete questions rather than page count and do not repeat conclusions.
