---
name: "clear-eyed-reading"
description: "Quickly understand and demystify a research paper, review, technical blog, commentary, or other article. Independently reconstruct what the work does, identify its genuine contribution and capability sources, explain how its reported result came about or whether its conclusion is warranted, and give a practical judgment in plain language. Available only when the user explicitly invokes this skill. Do not use for exhaustive section-by-section, figure-by-figure, equation, experiment, or appendix coverage; full translation; formal peer review; or accept/reject recommendation."
display_name: "Clear-Eyed Reading"
short_description: "Explain what the work really does, contributes, and how its result comes about"
default_prompt: "Use $clear-eyed-reading to explain and demystify what this article really does, contributes, and how its result or conclusion comes about."
---

# Quick Reading Profile

Complete the shared contribution map before writing, covering every important design and contribution even when the final reading mentions some only briefly. Present its conclusions as a compact, natural explanation. Lead with a short orientation when useful, then reconstruct the problem and answer in ordinary language, explain the important designs and genuine contributions with their capability sources and field position, and carry the reader through the core mechanism with the shortest useful example, equation, or diagram.

Explain how the decisive result came about, whether the conclusion follows, or what lets the system produce the shown behavior. Compress equations, figures, experiments, and implementation details to their conclusion plus the reason it follows. Expand internal detail when it changes the actual content, innovation or contribution, result attribution, or use. Integrate material boundaries and uncertainty where they affect those points. Close with the applicable use and a concise overall judgment. For a complete research paper, include the shared independent dimensions with the shared comparison threshold for novelty and significance.

Let headings and paragraph boundaries follow the material. A natural reader order is `orientation → plain reconstruction and real contributions → run the mechanism → explain the result or conclusion → use and five dimensions`. Keep the internal map, evidence boundaries, and research checklist out of view. Favor direct affirmative sentences over repetitive contrastive verdicts or a default catalogue of caveats.

Keep the output compact without fixed word counts or forced numbers of contributions, results, or objections. This profile shortens what is shown; it does not lower the shared reconstruction, research, or evidence standard.

If the user needs the full method, implementation details, equations, experiments, figures, or appendices expanded, recommend explicit use of `$clear-eyed-deep-reading` rather than silently turning this profile into a deep reading.
