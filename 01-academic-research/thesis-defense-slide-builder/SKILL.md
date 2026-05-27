---
name: thesis-defense-slide-builder
description: Transforms a UiS master's thesis into a 45-60 minute defense presentation with narrative arc, slide-by-slide outline, and speaker notes per slide. Structures as: hook → problem → research question → theoretical lens → method → findings → contribution → limitations → future work. Outputs a deck outline (slide titles + bullets + visuals + speaker notes), NOT the .pptx itself — pair with anthropic-skills:pptx skill to render. Use when the user says "build my defense slides", "viva presentation", "thesis defense deck", "presentation for examiner". Built for a UiS Management thesis (English, APA 7) on AI advisory / dynamic capabilities / service quality.
---

# Thesis Defense Slide Builder

Builds the narrative architecture of a master's thesis defense — the 45-60 minute presentation a UiS examiner expects to hear. The output is a slide-by-slide outline with speaker notes, ready to hand to the `anthropic-skills:pptx` skill (or to design directly in Keynote / Google Slides). The arc matters more than any single slide: a defense that stays in narrative wins; a defense that recites chapters in order loses.

## When to use this skill
- Defense / viva is in 1-6 weeks and the user needs to convert thesis to slides.
- A draft deck exists but feels disjointed (recite-the-chapters syndrome).
- The user wants speaker notes that aren't AI-flavored.
- Time budget is unclear — this skill calibrates to 45-60 min standard.
- The user wants to rehearse possible Q&A — pair with `devils-advocate-research`.

## Methodology

### Step 1: Confirm format constraints
Ask:
- Total presentation time? (UiS default: ~45 min presentation + ~45 min Q&A.)
- Audience composition? (Supervisor + external examiner + chair, sometimes peers.)
- Language? (English, given thesis is in English.)
- In-person, hybrid, or remote? (Affects visual density.)
- Slide template required by faculty?

Confirm the time budget — slide count derives from it (typical ratio: 20-30 slides for 45 minutes).

### Step 2: Extract the contribution sentence
Get one sentence: "This thesis contributes <X> to <field> by showing <Y> in the context of <Z>." Everything in the deck serves this sentence. If the contribution is fuzzy, fix it FIRST — bad contribution sentence = bad deck.

### Step 3: Build the narrative spine
The defense follows this canonical arc (adapt order only if the supervisor specifies):

1. **Hook (1-2 slides, ~2 min)** — open with a specific, real situation that makes the problem palpable. NOT "AI is changing business". Yes "When a 14-person Norwegian advisory firm tried to scale, here's what their managing partner discovered..."
2. **Problem (1-2 slides, ~3 min)** — the puzzle the field has not yet resolved. Frame as a tension, gap, or paradox.
3. **Research question (1 slide, ~1 min)** — the specific RQ(s) verbatim from the thesis. State why each matters.
4. **Theoretical framing (3-5 slides, ~6 min)** — the lens(es) used (dynamic capabilities, SERVQUAL, etc.) and how they connect. End with the conceptual model figure.
5. **Method (3-5 slides, ~7 min)** — research design, sample, data collection, analysis. The Gioia tree or coding tree appears here.
6. **Findings (5-8 slides, ~12 min)** — the heart of the defense. One slide per major finding/theme, each with: a claim, a piece of evidence (quote, table row, statistic), and a connection to theory.
7. **Discussion / Contribution (3-5 slides, ~8 min)** — restate contribution sentence, name what's new, position against the literature.
8. **Limitations (1-2 slides, ~2 min)** — honest, not performative. "Sample of 12 Norwegian SMBs limits generalizability to other geographies; future work could extend to..."
9. **Future work (1 slide, ~1 min)** — 2-3 specific directions, not vague gestures.
10. **Practical implications (1-2 slides, ~2 min)** — for managers / practitioners. Concrete.
11. **Closing (1 slide, ~1 min)** — restate contribution sentence verbatim, thank examiners, hand over to questions.

Total: ~22-32 slides for 45 minutes.

### Step 4: Per-slide structure
Each slide gets:
- **Title** — declarative noun phrase (4-8 words). NOT a question, NOT a sentence.
- **3-5 bullets max** — even fewer ideal. Each bullet is a phrase, not a paragraph.
- **One visual element** — figure / table / quote pull / icon. Slides without visuals = wall of text = bad defense.
- **Speaker notes** — 2-4 sentences in the user's voice. What you'd say if you stood at the podium. Not what's on the slide.

### Step 5: Identify load-bearing slides
Mark 4-6 slides as load-bearing:
- The contribution-sentence slide (Discussion).
- The conceptual-model figure (Theoretical framing).
- The data-structure / Gioia tree (Method or Findings).
- The 2-3 most important findings.

These get extra attention in rehearsal because Q&A will land on them.

### Step 6: Build the speaker notes
For each slide, write 2-4 sentences in spoken English (contractions OK, sentence fragments OK if they're how you'd actually say it). The notes are NOT a script to read — they're the cue card for the user's natural speaking pattern.

### Step 7: Plan the time
Add a cumulative time column. If the deck exceeds the time budget, the cut goes to: extra theoretical sub-slides, extra methodology detail, extra limitations. The cut does NOT go to: contribution, findings, or hook. Those are non-negotiable.

### Step 8: Produce a Q&A appendix
Prepare 5-10 backup slides (NOT shown in the main flow but available if asked):
- Detailed methodology slides for tough method questions.
- Alternative-explanation slide for "couldn't this be explained by X?"
- Sample-detail slide for "tell me about your participants".
- Theory-rival slide for "why this lens not <other>?"
- Pair with `devils-advocate-research` to identify which questions get a backup.

## Output format

A Markdown deliverable structured as:

```
## Defense Deck Outline — <thesis title>
Time budget: ~<N> minutes presentation + ~<M> minutes Q&A
Total slides (main flow): <N>
Total slides (backup / Q&A appendix): <M>

### Contribution sentence (the deck serves this)
"This thesis contributes <X> to <field> by showing <Y> in <Z>."

### Slide-by-slide outline

#### Slide 1: <title>
- Bullet 1
- Bullet 2
- Bullet 3
**Visual:** <image / chart / quote pull>
**Speaker notes:** <2-4 sentences>
**Time:** 2:00 (cumulative 2:00)

#### Slide 2: <title>
...

### Q&A appendix slides
- B1: Detailed sample table
- B2: Alternative-explanation discussion
- B3: ...

### Rehearsal recommendations
1. Read the deck out loud once with a stopwatch.
2. Practice the load-bearing slides separately.
3. Rehearse Q&A using the questions from `devils-advocate-research`.
4. Day-before: rehearse only the hook and the closing — they need to land cleanly.
```

## Quality checklist
- [ ] Total time fits the budget within ±10%.
- [ ] Contribution sentence appears verbatim on at least one main-flow slide and the closing.
- [ ] Every slide has a visual (figure, table, quote, icon — NOT just text).
- [ ] Speaker notes are in spoken English, not written-academic English.
- [ ] Hook is specific (named context, named situation), not generic.
- [ ] Limitations are honest (real threats, not performative).
- [ ] Q&A appendix has at least 5 backup slides.
- [ ] Load-bearing slides are explicitly identified.

## Notes for the assistant
- The defense is a performance, not a recital. The user doesn't read the slides aloud — slides are the visual aid, the user is the source of the argument.
- Avoid: full-sentence bullets, citations on every bullet, slide titles like "Conclusion" or "Methods" (use specific declarative titles).
- The hook is the single most important slide for setting tone. Generic hooks ("AI is transforming business") signal an unconfident speaker. Specific hooks (real situation, real number, real quote) signal authority.
- For UiS Management theses on AI advisory, possible hooks: a quote from a real participant, a specific statistic from a credible report (McKinsey, BCG, etc.), a paradox in the literature.
- Slide design hygiene: max ~30 words per slide; consistent fonts; consistent color palette (max 3 colors); citations small but visible (Author, Year on the same slide as the claim).
- Pair with `anthropic-skills:pptx` to render the actual .pptx, with `scientific-schematics` for figures, with `devils-advocate-research` for Q&A prep, and with `apa-style-enforcer` to ensure citations on slides are formatted right.
- Practical implications matter at UiS — the program values applied research. Don't skip this section.
- Backup slides are the secret weapon of a confident defense. Examiner asks "tell me more about your sample" — user clicks to backup slide B1 — instant credibility.
- Speaker notes must NOT have AI giveaway phrases. The user is going to speak these. Pair with `academic-tone-polisher` if needed.
