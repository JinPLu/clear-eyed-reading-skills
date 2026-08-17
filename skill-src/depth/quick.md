---
name: "clear-eyed-reading"
description: "Quickly understand and demystify a research paper, review, technical blog, commentary, or other article. Independently reconstruct what the work does, identify its genuine contribution and capability sources, explain how its reported result came about or whether its conclusion is warranted, and give a practical first-screen judgment in plain language. Available only when the user explicitly invokes this skill. Do not use for exhaustive section-by-section, figure-by-figure, equation, experiment, appendix, or companion-source coverage; full translation; formal peer review; or accept/reject recommendation."
display_name: "Clear-Eyed Reading"
short_description: "Explain what the work really does, contributes, and how its result comes about"
default_prompt: "Use $clear-eyed-reading to explain and demystify what this article really does, contributes, and how its result or conclusion comes about."
---

# Quick Reading Profile

Complete the shared four judgments. Cover every important candidate contribution in the target, even if the final reading mentions some only briefly. Spend the search budget on claims, nearest neighbors, and companion signals that would change the overall judgment or the decision to keep investing. Do not read the work as if this were a deep reading: do not exhaust appendices, every equation or figure, implementation detail, or all six companion-evidence classes.

Do one low-cost, high-yield companion pass: whether peer-review or errata traces exist, whether a newer version exists, and whether official code or a project page matches the paper's claims. Deep-dive a neighbor or companion source only when that signal would change the overall judgment. Mark unobserved classes as unobserved; do not infer from absence.

Deliver a usable first-screen answer. Open with a one-sentence ordinary reconstruction, the most important genuine increment, and the overall judgment, and name the version those conclusions rest on. Then reconstruct the problem and answer in ordinary language, explain the important designs and genuine contributions with their capability sources and field position, and carry the reader through the core mechanism with the shortest useful example, equation, or diagram.

Explain how the decisive result came about, whether the conclusion follows, or what lets the system produce the shown behavior. Compress other equations, figures, experiments, and implementation details to their conclusion plus the reason it follows. Expand internal detail only when it changes the actual content, genuine increment, result attribution, maturity, or use. Weave a companion fact in at the point it changes that account; do not add a popularity or external-info section.

Close with the applicable use and a concise overall judgment. Do not default to the five research-paper scores unless the user asks or the verified evidence already supports them. If scores are given, keep the shared comparison threshold for novelty and significance.

Let headings follow the material. A natural reader order is `opening judgment → plain reconstruction and real contributions → run the mechanism → explain the result or conclusion → use`. Keep the internal map, evidence boundaries, and research checklist out of view. Favor direct affirmative sentences over repetitive contrastive verdicts or a default catalogue of caveats. Keep the output compact without fixed word counts or forced numbers of contributions, results, or objections.

If the user needs the full method, implementation details, equations, experiments, figures, appendices, or exhaustive companion verification—or needs to retell, reuse, or challenge the method—recommend explicit use of `$clear-eyed-deep-reading` rather than silently turning this profile into a deep reading.
