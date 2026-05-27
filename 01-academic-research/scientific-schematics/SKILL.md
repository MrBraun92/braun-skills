---
name: scientific-schematics
description: Generates publication-quality scientific diagrams for a UiS Management master's thesis — PRISMA flow, conceptual model, theoretical framework, research design, coding tree (Gioia), variance/process model. Outputs Mermaid source the user can render directly, plus a draw.io / diagrams.net layout description for polished publication versions. Use when the user says "draw the conceptual model", "PRISMA diagram", "research design figure", "theoretical framework diagram", "Gioia data structure tree", or "thesis needs a figure here".
---

# Scientific Schematics

Produces the diagrams a Management master's thesis actually needs — not generic flowcharts, but the canonical figure types examiners expect to see. Outputs Mermaid source (immediately renderable, version-controllable) and a draw.io layout description (for polished publication-quality artwork). Built for a UiS thesis in English under APA 7, where every figure needs a caption, a number, and a back-reference in the text.

## When to use this skill
- The thesis methods chapter needs a PRISMA flow diagram.
- The literature review needs a conceptual model figure.
- The findings chapter needs a Gioia data structure (1st-order → 2nd-order → aggregate).
- The discussion needs a process model or variance model.
- The user says "I need a figure here but don't know what it should look like".

## Methodology

### Step 1: Identify the figure type required
Confirm with the user (or infer from context) which canonical figure is needed:

- **PRISMA 2020 flow** — for systematic reviews. Stages: Identification → Screening → Eligibility → Included, with counts and exclusion reasons at each stage.
- **Conceptual model** — boxes for constructs, arrows for hypothesized relationships. Used in lit review or methods.
- **Theoretical framework diagram** — like conceptual model but explicitly labels the theoretical lens(es) wrapped around the construct relationships.
- **Gioia data structure tree** — three columns left-to-right: 1st-order concepts, 2nd-order themes, aggregate dimensions. Used in qualitative findings chapters.
- **Process model** — sequence of stages with conditions and feedback loops. Used when the contribution is a process explanation.
- **Variance model** — independent → mediator → moderator → dependent variables, with arrows showing direction and sign. Used for hypothetico-deductive testing.
- **Research design figure** — phases of the study (e.g., Phase 1: lit review → Phase 2: pilot interviews → Phase 3: main interviews → Phase 4: analysis → Phase 5: theorizing).

### Step 2: Gather the inputs
For each figure type, the inputs are different. Prompt the user for what's missing:

- PRISMA: counts at each stage + exclusion reasons + database list. Pull from `systematic-literature-review` skill output if recent.
- Conceptual model: list of constructs + list of relationships (which → which, sign + or -, direct or moderating).
- Gioia tree: aggregate dimensions, 2nd-order themes per dimension, 1st-order codes per theme. Pull from `qualitative-coding-specialist` skill output if recent.
- Process model: stages, transitions, conditions for each transition.
- Variance model: independent variables, mediators, moderators, dependent variable, hypothesized signs.

### Step 3: Render in Mermaid
Mermaid is the primary deliverable because it can be pasted into Markdown / Notion / GitHub and renders immediately. Use the appropriate diagram type:

- `flowchart LR` for conceptual / theoretical / variance models.
- `flowchart TD` for PRISMA.
- `flowchart LR` with three subgraphs for Gioia trees.
- `stateDiagram-v2` or `flowchart TD` for process models.

Add labels, edge labels (relationship name + sign), and groupings via `subgraph`.

### Step 4: Provide a draw.io alternative description
For final publication, Mermaid sometimes is not flexible enough. Produce a parallel description:
- Page size and orientation.
- Per node: label, shape (rectangle / rounded / oval / diamond), position (relative coordinates), color (use accessible palette — avoid red/green only).
- Per edge: source, target, label, arrow style (solid for direct, dashed for moderating), arrowhead style.

The user can recreate manually in draw.io / diagrams.net or hand to a designer.

### Step 5: Write the figure caption
APA 7 captions are essential:
- Format: `Figure N. <Title>. <Note: explanatory text>.` placed below the figure.
- Title is a noun phrase (e.g., "Conceptual model of AI advisory dynamic capabilities"), not a sentence.
- Note clarifies abbreviations, statistical notation, sample, and source if reproduced.

### Step 6: Write the in-text reference
Every figure must be referenced in the body text (APA 7 requirement). Provide a 1-2 sentence template the user pastes near where the figure appears: "Figure 3 visualizes the proposed conceptual model. Sensing capability (Teece, 2007) is hypothesized to..."

## Output format

A Markdown deliverable with four sections per figure:

```
## Figure: <title>
Type: <PRISMA / Conceptual / Theoretical / Gioia / Process / Variance / Research design>

### 1. Mermaid source
<```mermaid block>

### 2. Draw.io layout description
- Page: A4 landscape, 1:1
- Nodes:
  - "Sensing capability" — rounded rectangle, top-left, color #E8F4F8
  - ...
- Edges:
  - Sensing → Seizing — solid arrow, label "enables"
  - ...

### 3. APA 7 caption
Figure N. <title>. <Note>.

### 4. Suggested in-text reference
"<sentence template>"
```

## Quality checklist
- [ ] Figure type is named and matches the chapter's actual need.
- [ ] Mermaid renders without errors (no orphan nodes, no syntax mistakes).
- [ ] Caption follows APA 7 format (Figure N. Title. Note.).
- [ ] Every box and arrow in the diagram is labeled.
- [ ] Color choices are accessible (do not rely on red/green alone).
- [ ] In-text reference is provided.
- [ ] PRISMA counts reconcile (Identified - Duplicates - Excluded TitleAbstract - Excluded FullText = Included).
- [ ] Gioia trees show ≥2 1st-order codes per 2nd-order theme and ≥2 themes per aggregate dimension.

## Notes for the assistant
- Diagrams should reduce cognitive load, not add to it. If a model has more than ~9 nodes, suggest splitting into two figures.
- For Management research conventions: solid arrows = direct effect, dashed = moderating, dotted = correlation only.
- Variance model arrows should show sign (+ / -) when the literature supports a directional hypothesis.
- Process model boxes should be verbs/gerunds ("Sensing AI opportunities") not nouns ("Sensing").
- Avoid clip-art, emoji, decorative elements. Thesis figures are functional.
- For PRISMA specifically, the 2020 update has slightly different boxes than 2009 — use 2020 unless the user says otherwise.
- Pair with `systematic-literature-review` (PRISMA inputs), `qualitative-coding-specialist` (Gioia inputs), and `theoretical-integration` (conceptual model inputs).
- Captions must be self-contained — a reader who only sees the figure should understand it without scrolling to body text.
