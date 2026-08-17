---
name: "clear-eyed-deep-reading"
description: "Perform a complete, clear-eyed deep reading of a research paper, review, technical blog, commentary, or other long-form technical work. Independently reconstruct the problem and mechanism, trace capability and knowledge sources, determine the genuine contribution, explain how the reported result came about or whether the conclusion is warranted, and expand the consequential figures, equations, implementation details, evidence, and companion sources in plain language. Available only when the user explicitly invokes this skill. Do not use for a quick summary, full translation, formal peer review, or accept/reject recommendation."
display_name: "Clear-Eyed Deep Reading"
short_description: "Reconstruct the work, real contribution, details, and how its result comes about"
default_prompt: "Use $clear-eyed-deep-reading to reconstruct this work, explain its details and genuine contribution, and show how its result or conclusion comes about."
---

# Deep Reading Profile

Complete the same four judgments and contribution map as the quick profile, then verify them at full cost so a new reader can retell the problem in ordinary language, run the mechanism, identify capability or knowledge sources, explain every important contribution, interpret the evidence, reuse or reimplement the work, and challenge the final judgment.

Read the full text, appendices, decisive figures, tables, equations, and consequential implementation or analytical details when available. Expand every part of the map whose evidence or internal detail changes actual content, technical increment, field significance, result attribution, use, or final judgment. Identify material differences among the paper, appendix, official code, reviews, and reproductions; do not invent missing details. Separate training from inference, observation from intervention, or assumptions from consequences when relevant.

Systematically expand all six companion-evidence classes and cross-check them against the contribution map and result attribution. Name what remains unobserved. Companion evidence calibrates maturity, reproducibility, reusability, claim stability, whether the work has been superseded, and usage caveats; it does not replace nearest-primary-literature tests of what is new. Challenge every central contribution with at least two independent discovery paths, and stop only when a further expansion yields no judgment-changing neighbor or companion correction and remaining gaps are recorded.

Develop the same natural narrative spine as the quick profile with type-appropriate depth. Open with a one-sentence ordinary reconstruction, the most important genuine increment, the overall judgment, and the version those conclusions rest on. Then position the work, reconstruct the problem and answer, unfold the mechanism and its sources, relate each important design to its closest precedents, explain how the result came about and which other explanations remain, then form the contribution, use, and—for a complete research paper—the five-dimension judgment. Let the work's structure determine headings and emphasis while keeping the internal map and research process out of view. Weave companion facts in where they change mechanism, attribution, maturity, or use; do not add a popularity section.

Cover the necessary background, full mechanism chain, and consequential implementation or analytical details. Explain details that change understanding, reproduction, attribution, or confidence in the conclusion; mention ordinary configuration briefly.

Integrate every equation needed to understand the mechanism or conclusions into the step that uses it. Expand the running example across modules, dimensions, states, populations, or decisions when that makes the work concrete.

Explain the type-appropriate evidential setting and the evidence carrying each important contribution and central result. For experimental work, cover consequential data, baselines and fairness, metrics, main results, ablations, robustness checks, qualitative results, and failures. For theoretical, clinical, qualitative, resource, benchmark, review, or mixed work, expand the corresponding assumptions, comparisons, materials, definitions, and alternatives that bear on the contribution. Compress routine evidence to its role and conclusion; expand the details that change reconstruction or judgment.

Give special attention to the original figures or crops most directly tied to the mechanism, genuine contributions, or explanation of how the result came about. Explain how to read them and what they add; treat other figures according to their consequential role. Integrate material boundary facts, companion corrections, and uncertainty beside the affected content, contribution, attribution, or use.

Use a natural progression such as `opening judgment → reconstruct the problem and contribution → make the mechanism and sources understandable → explain the results, alternatives, and companion checks → form a judgment`. If the work is too long for one response, divide it by complete questions rather than page count and do not repeat conclusions. For a complete research paper, include the shared independent dimensions with the shared comparison threshold for novelty and significance.
