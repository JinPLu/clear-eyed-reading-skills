---
name: "clear-eyed-reading"
description: "Quickly understand and demystify a research paper, review, technical blog, commentary, or other article. Reconstruct the problem and method for a reader with no field background, identify the genuine contribution and decisive evidence, narrow hype, and give a practical judgment. Available only when the user explicitly invokes this skill. Do not use for exhaustive section-by-section, figure-by-figure, equation, experiment, or appendix coverage; full translation; formal peer review; or accept/reject recommendation."
display_name: "Clear-Eyed Reading"
short_description: "Explain the method, real contribution, evidence, and hype"
default_prompt: "Use $clear-eyed-reading to explain and demystify this article."
---

# Quick Reading Profile

Present the completed analysis through five compact sections in this reader order. Localize the headings naturally, but keep their functions distinct:

1. **Problem and essential background:** Make the problem and its difficulty understandable without assuming field knowledge.
2. **How the method works:** Run the core mechanism through the shared concrete example. Include only the details and equations needed to understand it.
3. **What is genuinely new:** Position the real increment after the reader understands the method; do not copy the authors' contribution list.
4. **What the decisive evidence shows:** Select the evidence that most changes the judgment. State what it supports and what it does not establish; compress supporting experiments and figures unless they change the conclusion.
5. **Clear-eyed conclusion and five-dimension assessment:** State the material hype or limit, applicable range, practical use, and the shared scorecard without repeating the whole reading.

Open with a short orientation when useful, but do not make it another section. Embed the example and any necessary diagram in the method section. Keep the output compact without fixed word counts or forced numbers of contributions, results, or problems. This profile shortens what is shown; it does not lower the shared reading or evidence standard.

If the user needs the full method, implementation details, equations, experiments, figures, or appendices expanded, recommend explicit use of `$clear-eyed-deep-reading` rather than silently turning this profile into a deep reading.
