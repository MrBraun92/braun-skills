---
name: theoretical-integration
description: Forces real conceptual integration of a literature review or discussion chapter — turning a "list of authors who said similar things" into a synthesized framework that names tensions, complementarities, and unresolved gaps. Use when the user says "my lit review is just a list", "integrate these theories", "build a conceptual framework", "synthesize this", or "the theory chapter feels flat". Designed for a UiS Management master's thesis (English, APA 7) on AI advisory, dynamic capabilities, and service quality.
---

# Theoretical Integration

Pushes a literature review past summary into synthesis. The most common failure mode of master's thesis lit reviews is the "annotated bibliography in prose" — paragraph 1 says what Author A wrote, paragraph 2 says what Author B wrote, and there is no theoretical argument linking them. This skill produces the missing argument: the integrated framework that says how these theories speak to each other and where the user's research enters.

## When to use this skill
- Lit review reads as paper-by-paper recitation; supervisor said "synthesize, don't summarize".
- User has 30-80 papers organized but no overarching framework.
- Discussion chapter doesn't connect findings back to theory in a coherent way.
- User needs a conceptual model diagram but no integrated theory to draw.
- Two literatures (e.g., dynamic capabilities + service quality) need to be bridged by the thesis.

## Methodology

### Step 1: Inventory the theoretical perspectives
List every theoretical lens, framework, or construct currently invoked. For each: foundational author(s), core claim in one sentence, dominant unit of analysis (firm? individual? interaction?), epistemological stance. A typical master's thesis uses 2-4 perspectives. If more than 5 are listed, the chapter is over-loaded — flag for pruning before integration.

### Step 2: Map relationships among perspectives
For each pair of perspectives, classify the relationship as one of:
- **Complementary** — they explain different layers of the same phenomenon (e.g., dynamic capabilities explains the firm level, micro-foundations explain the individual level).
- **Competing** — they offer rival explanations for the same outcome (e.g., resource-based view vs. dynamic capabilities on the source of competitive advantage).
- **Sequential** — one precedes the other in a causal chain.
- **Nested** — one is a special case of the other.
- **Disjoint** — currently no documented overlap; bridging them IS the contribution.

A simple matrix helps: rows × columns = perspectives; cells = relationship type.

### Step 3: Name the tensions
For every "competing" or "disjoint" pair, write the tension explicitly: "Perspective A predicts X. Perspective B predicts Y. They cannot both be right under conditions Z." Do not paper over disagreement — the tension is where the contribution lives.

### Step 4: Name the complementarities
For "complementary", "sequential", or "nested" pairs, write the integration: "Perspective A explains the firm-level capability for sensing AI advisory opportunities (Teece, 2007). Perspective B explains the individual-level micro-foundation (Felin et al., 2012). Together they predict that firms develop AI-advisory dynamic capabilities only when both firm-level routines and individual sensemaking align — which is what this thesis tests."

### Step 5: Position the thesis
Locate the user's research in the integrated map. Specifically: which gap does it fill? Phrase as a *named* contribution:
- "Bridging" — fills a disjoint by linking two literatures.
- "Refining" — adds a contingency or boundary condition to an existing theory.
- "Extending" — applies a theory to a new context.
- "Adjudicating" — uses empirical data to favor one of two competing predictions.
- "Building" — proposes a new construct or model.

For a master's thesis, "extending" or "refining" is the most defensible. "Building" is ambitious and rare at this level — discourage if the data is thin.

### Step 6: Draft the integrated framework
Produce a 1-2 paragraph synthesis statement that the user can drop into the lit review's closing section, and a conceptual model diagram outline that the `scientific-schematics` skill can render as Mermaid.

### Step 7: Write the integration paragraphs
Rewrite the lit review's closing paragraphs (or write new ones) that explicitly name the tensions, the complementarities, and the gap. This is the prose form of the integrated framework.

## Output format

A Markdown deliverable with five sections:

```
## Theoretical Integration — <thesis topic>

### 1. Perspectives inventory
| Perspective | Foundational author(s) | Core claim | Unit of analysis |
|---|---|---|---|

### 2. Relationship matrix
A small matrix (perspectives × perspectives) with relationship labels.

### 3. Tensions
- A vs B: <tension stated explicitly>
- C vs D: <tension stated explicitly>

### 4. Complementarities and integration
- A + B → <integrated argument>
- C + D → <integrated argument>

### 5. Thesis positioning
- Contribution type: <Bridging / Refining / Extending / Adjudicating / Building>
- Gap statement: <one sentence>
- Integrated synthesis paragraphs (drop into lit review):

   <2 paragraphs in the thesis voice — APA 7 citations included>

### 6. Conceptual model outline (for scientific-schematics)
- Boxes: <list>
- Arrows: <list with labels>
```

## Quality checklist
- [ ] Every perspective in the relationship matrix appears in the inventory.
- [ ] At least one tension is named explicitly (no smoothing-over).
- [ ] The contribution type is named (one of the five labels).
- [ ] The gap statement is in one sentence and is testable / addressable in the thesis scope.
- [ ] The synthesis paragraphs cite at minimum the foundational authors of each perspective.
- [ ] No new theory is invented — the integration draws on what already exists in the literature.

## Notes for the assistant
- The hardest part is admitting which perspectives are in tension. Master's students often try to harmonize everything; that produces vague theory. Push for tension where it exists.
- For AI advisory + dynamic capabilities + service quality specifically: dynamic capabilities is firm-level, SERVQUAL is dyadic (provider × customer), AI is socio-technical. Integration usually requires either multi-level theorizing or naming one as the focal lens with the others as supporting.
- If the user's data already shaped the framework (which is normal in inductive work), say so. Reverse-engineering theory to fit data is not dishonest as long as the methods chapter discloses inductive logic.
- "Conceptual model" boxes-and-arrows diagrams should not exceed ~8 nodes for a master's thesis. More than that signals the framework is doing too much.
- Pair with `claim-evidence-mapper` (verify the integrated claims have evidence) and `scientific-schematics` (render the conceptual model). Pair with `apa-style-enforcer` when finalizing the synthesis paragraphs.
- Do not produce a framework so generic that any thesis could use it. The framework is defensible only if it explains *this* phenomenon under *these* conditions.
