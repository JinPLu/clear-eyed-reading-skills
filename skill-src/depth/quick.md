---
name: "clear-eyed-reading"
description: "Quickly explain a research paper, review, technical blog, commentary, or other article in plain language, covering what it actually does once names and branding are stripped away, how the method works through a text diagram and one worked example, what is really new versus earlier work, where its ability comes from, why its result came out that way, and whether it is worth the reader's time. Available only when the user explicitly invokes this skill. Do not use for exhaustive section-by-section, figure-by-figure, equation, experiment, appendix, or outside-source coverage; full translation; formal peer review; or accept/reject recommendation."
display_name: "Clear-Eyed Reading"
short_description: "Plainly explain what a work really does, what is new, and why its result holds"
default_prompt: "Use $clear-eyed-reading to explain in plain language what this article really does, what is actually new, and why its result or conclusion comes out that way."
---

# Quick Reading

Purpose: a first-screen answer that lets the reader understand the work and decide whether to invest more.

- Cover every important claimed contribution, but keep each section short. Section 1 is two or three sentences. Section 3 is one diagram plus a short running example through the key steps. Compress other equations, figures, experiments, and implementation details to their conclusion plus the reason, unless a detail changes what the work does, what is new, why the result appears, or whether to use it.
- Research budget: check the claims, closest earlier work, and outside signals that could change the overall verdict. Do one cheap pass around the work — any reviews or errata, a newer version, and whether the official code or project page matches the paper — and dig further only when a signal would change the verdict. Do not exhaust appendices, every equation or figure, or all six kinds of outside material.
- Give no scores unless the user asks for them.
- If the reader needs the full method, equations, experiments, appendices, or exhaustive checking — or wants to retell, reuse, or challenge the method — recommend `$clear-eyed-deep-reading` rather than silently going deep.
