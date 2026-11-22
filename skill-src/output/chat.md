# Writing the Answer

Write for a smart reader outside the field. Follow the user's language.

## Plain words

- Never put this skill's working labels in the answer — "four questions", "ability source", "genuine increment", "outside material", "claim gap", "removal counterfactual", and the like. Say the plain thing instead: "this ability actually comes from the pretrained backbone", "the only new part is the reranker".
- Say what a module does before using the authors' name for it: "a small network that scores each image patch (the authors call it X)".
- Define each unavoidable technical term in a short clause at first use. Prefer short sentences with a concrete subject and verb. Avoid chains of hedges and repeated "not X but Y" contrasts.
- Where it matters whether a statement is checked, the authors' claim, or your inference, mark it briefly in place, such as "(inferred)" or "(checked in official config)"; do not tag every sentence.
- Do not narrate your process. State the scope in one or two plain lines: exact version, release date, and publication venue/tier (such as `ICLR 2024 Oral`, `Nature`, or `arXiv preprint`), the sources and traction platforms that inform the verdict, and anything decisive that could not be checked and why.

## Sections

Use these six sections in this order. Phrase each heading as the reader's question, in the user's language. For non-paper material, rename or merge sections that do not apply, keeping the order.

1. **In one sentence** — what the work actually does in plain words, its single most important new thing, and the overall verdict (weighing both novelty and real-world/community value), followed by the short scope line.
2. **What problem does it solve?** — the concrete difficulty, why it is hard, and how people handled it before. Give only the background this work needs.
3. **How does it work?** — first the diagram (below), whose `★`/`○` notes already show which parts are added versus borrowed or external, then **one concrete miniature example** followed from input to output. Pick a miniature case suited to the kind of work — such as a 3-number vector or 4-pixel row for a model, one sample task for a benchmark, one minimal special case for a theorem, one group comparison for an empirical or clinical study, or one core argument chain for an essay — followed by one line giving the work's real scale when applicable. Focus each step on what goes in, what transforms, what comes out, and why the step is needed; **keep comparisons with earlier papers for section 4** so sections 3 and 4 do not repeat each other.
   - **Inference before training:** walk through online operation or inference end-to-end first; add a compact training step afterwards only when training differs in a way that matters for the depth profile (for example, when the training setup is itself a core contribution, or in Deep Reading).
   - **Equation discipline:** write out an equation only when this work introduces, modifies, or hinges on its specific form. Summarize textbook or borrowed formulas (vanilla cross-entropy, standard MSE or flow-matching loss, simple averages) in plain words without displaying symbols or filler arithmetic. When an equation is shown, state what it does and why, define its symbols, and plug in **the same running example's numbers** — never invent a disconnected side vector just to illustrate a formula. Name equations by function, using equation numbers only as locators. Equations that serve as evaluation metrics or analysis belong in section 5 beside the result they support.
4. **What is actually new?** — a table covering every important claimed contribution, then a short synthesis paragraph:

   | Part | Already existed (closest earlier work) | What this work changed | Lost without this change |
   | --- | --- | --- | --- |

   In column 2, name the closest earlier work and briefly note how it was checked — for example `Spatia (§3)` when verified in that paper's primary text, `BM25 (standard)` for textbook tools, or `X (via survey)` / `X (per §2, primary text not rechecked)` when relying on a secondary reference or staying within the Quick budget. "Lost without this change" is relative to that closest earlier work, not to having no method at all; a benefit any similar method already gives is not lost. For a tutorial, review, or commentary whose contribution is the explanation or argument, compare its framing and claims with existing explanations instead. Say plainly when a claimed contribution is mostly relabeling, and just as plainly when an undersold part is the real contribution. Keep traction metrics out of novelty claims here.
5. **Why did the result come out this way — should I believe it?** — the evidence that carries the main result, **how complete and rich the experiments and manuscript are** (ablations, baseline fairness, stress/scaling checks, failure analysis, appendix depth versus thin or selective reporting), the strongest other explanation and whether the work rules it out, and anything from reviews, newer versions, code, issues, or reproductions that changes the picture. Raise a caveat only where it changes what the reader understands or does; no generic limitation list.
6. **Is it worth my time, and how would I use it?** — who should read or use it and for what, grounded in **three value references**: (a) **manuscript richness and experimental completeness** (whether reading the paper/appendix rewards the time spent), (b) **community value** (reusable open code, weights, datasets, benchmark harness, or durable empirical findings, plus whether something newer has superseded it), and (c) **venue standing and time-contextualized traction** when available (journal or conference venue and tier such as Oral/Spotlight/Poster versus preprint, alongside Semantic Scholar / Google Scholar citations, GitHub stars, and Hugging Face paper votes or model/dataset adoption, interpreted relative to release date; state plainly if unchecked or unavailable). Add practical reuse caveats, and place the five integer scores here when they apply.

Put each citation next to the fact it supports: section, figure, table, or equation number, or a link.

## Diagrams

Draw diagrams as plain-text box drawings inside a `text` code block, so they display identically in any terminal or chat interface. Do not use Mermaid, HTML, or images for diagrams.

- One main diagram of the method in section 3. Add a second only when training and inference, or two branches, differ in a way prose cannot carry. Draw nothing else unless a relationship is hard to follow in prose.
- Flow top to bottom, 3–7 boxes. The drawing, not counting notes, is at most 72 columns wide; keep notes short.
- Use box-drawing characters `┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼` and arrows `▼ ▶ ◀`. Parallel branches split with `├───┐`; a branch or side input joins a box with a side arrow, `──▶` from the left or `◀──┘` from the right. Separate inputs may sit side by side on the first row. When two boxes share a row, write one note after the rightmost box that names each (`left ○ …; right ★ …`).
- Label each arrow with what flows along it, with sizes when known: `image 224x224`, `top-20 passages`, `score in [0,1]`.
- Inside boxes use only short ASCII labels, so every row of a box has the same width. Wide characters such as Chinese, Japanese, or Korean text break alignment inside boxes; put explanations in the user's language to the right of the box as `← note`, where width no longer matters.
- Start each note with `★` for a part this work adds or changes, or `○` for a reused, external, or pretrained part.
- Before sending, check that every row of each box has the same length, that each vertical line keeps one column from where it leaves a box to where its arrow enters the next, and that the arrow entering a box and the `┬` leaving it share a column.

Format example (notes follow the user's language):

```text
  question
      │
      ▼
┌───────────┐
│ retriever │  ← ○ off-the-shelf BM25 search, unchanged
└─────┬─────┘
      │ top-20 passages
      ▼
┌───────────┐
│ reranker  │  ← ★ new: a small model rescores each passage
└─────┬─────┘
      │ top-3 passages
      ▼
┌───────────┐
│ LLM       │  ← ○ existing language model writes the answer
└─────┬─────┘
      ▼
   answer
```

A training-versus-inference split can branch sideways with `├──▶` when needed:

```text
┌───────────┐
│ encoder   │  ← ○ pretrained, frozen
└─────┬─────┘
      ├──────────────▶ training only: contrastive loss
      ▼
┌───────────┐
│ head      │  ← ★ new: the only trained part
└───────────┘
```

For original figures, cite the figure number and tell the reader where to look and what it shows. Embed an image only when the interface is known to display images.
