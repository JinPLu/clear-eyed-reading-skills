# Writing the Answer

Write for a smart reader outside the field. Follow the user's language.

## Plain words

- Never put this skill's working labels in the answer — "four questions", "ability source", "genuine increment", "material around the work", "claim gap", and the like. Say the plain thing instead: "this ability actually comes from the pretrained model", "the only new part is the reranker".
- Say what a module does before using the authors' name for it: "a small network that scores each image patch (the authors call it X)".
- Define each unavoidable technical term in a short clause at first use. Prefer short sentences with a concrete subject and verb. Avoid chains of hedges and repeated "not X but Y" contrasts.
- Where it matters whether a statement is checked, the authors' claim, or your inference, mark it briefly in place, such as "(inferred)" or "(checked against the original)"; do not tag every sentence.
- Do not narrate your process. State the scope in one or two plain lines: which version and sources were checked, and what could not be checked and why (for example, a page was inaccessible).

## Sections

Use these six sections in this order. Phrase each heading as the reader's question, in the user's language. For non-paper material, rename or merge sections that do not apply, but keep the order.

1. **In one sentence** — what the work actually does in plain words, its single most important new thing, and the overall verdict. Then the scope note: version and the sources that decide the verdict, not every source read.
2. **What problem does it solve?** — the concrete difficulty, why it is hard, and how people handled it before. Give only the background this work needs.
3. **How does it work?** — first the diagram (below), then one running example with concrete values followed through every important step. Use toy sizes small enough to compute by hand (for example 3-dimensional vectors), then give one line scaling the example up to the real sizes. For each step say what goes in, what happens, what comes out, and why the step is needed, and say whether the step is borrowed or new. Put each needed equation at the step that uses it: first what it does and why, then the symbols, then the example's numbers plugged in. Name equations by function; use the number only as a locator. Equations that serve as analysis or evidence rather than mechanism belong in section 5, beside the result they support.
4. **What is actually new?** — a table, then a few sentences.

   | Part | Already existed (closest earlier work) | What this work changed | Lost without this change |
   | --- | --- | --- | --- |

   "Lost without this change" is relative to the closest earlier work, not to having no method at all; a benefit any similar method already gives is not lost. For a tutorial, review, or commentary whose contribution is the explanation or argument, compare its framing and claims with existing explanations instead; the diagram's `★`/`○` still mark where each part comes from. Cover every important claimed contribution. Say plainly when a claimed contribution is mostly relabeling, and just as plainly when an undersold part is the real contribution.
5. **Why did the result come out this way — should I believe it?** — the evidence that carries the main result, the strongest other explanation and whether the work rules it out, and anything from reviews, newer versions, code, or reproductions that changes the picture. Raise a caveat only where it changes what the reader understands or does; no generic limitation list, no popularity section.
6. **Is it worth my time, and how would I use it?** — who should read or use it, for what, with which caveats, and practical facts such as where a maintained implementation lives or whether something newer has replaced it. Scores go here when they apply.

Put each citation next to the fact it supports: section, figure, table, or equation number, or a link.

## Diagrams

Draw diagrams as plain-text box drawings inside a `text` code block, so they display identically in any terminal or chat interface. Do not use Mermaid, HTML, or images for diagrams.

- One main diagram of the method in section 3. Add a second only when training and inference, or two branches, differ in a way prose cannot carry. Draw nothing else unless a relationship is hard to follow in prose.
- Flow top to bottom, 3–7 boxes. The drawing, not counting notes, is at most 72 columns wide; keep notes short.
- Use box-drawing characters `┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼` and arrows `▼ ▶ ◀`. Parallel branches split with `├───┐`; a branch or side input joins a box with a side arrow, `──▶` from the left or `◀──┘` from the right. Separate inputs may sit side by side on the first row. When two boxes share a row, write one note after the rightmost box that names each (`left ○ …; right ★ …`).
- Label each arrow with what flows along it, with sizes when known: `image 224x224`, `top-20 passages`, `score in [0,1]`.
- Inside boxes use only short ASCII labels, so every row of a box has the same width. Wide characters such as Chinese, Japanese, or Korean text break alignment inside boxes; put explanations in the user's language to the right of the box as `← note`, where width no longer matters.
- Start each note with `★` for a part this work adds or changes, or `○` for a reused, external, or pretrained part.
- Before sending, check that every row of each box has the same length that each vertical line keeps one column from where it leaves a box to where its arrow enters the next, and that the arrow entering a box and the `┬` leaving it share a column.

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
