---
name: citation-integrity-checker
description: Verifies whether each in-text citation in an academic manuscript actually supports the claim it is attached to. Use whenever the user pastes a passage with citations, drafts a literature review section, integrates AI-generated text into a thesis, or asks "does this citation hold up?" / "check my references". Detects hallucinated citations (the highest-risk failure mode of AI-assisted academic writing) and flags weak, miscited, or strong support per citation.
---

# Citation Integrity Checker

Verifies whether each in-text citation in an academic manuscript actually supports the surrounding claim. Built for a UiS master's thesis in Management (AI advisory, dynamic capabilities, service quality) written in English under APA 7. The single largest risk of LLM-assisted academic writing is **hallucinated or miscited references** — this skill is the gate against that risk.

## When to use this skill
- A passage with citations needs verification before submission to supervisor
- A literature review chunk was drafted (or reshaped) with help from an LLM
- The user asks "is this citation real?" / "does this paper say that?" / "verify references"
- A reviewer (supervisor, peer, defense committee) flagged a citation as suspect
- Reusing notes from old reading where the original quote got lost

## Methodology

### Step 1: Extract every citation atom
Parse the text and produce a numbered list. Each atom = one (Author, Year) instance attached to one specific claim. A single sentence with three citations = three atoms. Note the page/section number if present (APA 7 requires it for direct quotes and is best practice for paraphrases of specific arguments).

### Step 2: Locate the cited source
For each atom: confirm the reference exists in the user's reference list. If a DOI is present, use it. If not, ask the user to attach the PDF, paste the abstract, or provide a verifiable link (Google Scholar, Semantic Scholar, OpenAlex, journal page, library record). Do NOT proceed to Step 3 with a fabricated guess about the source — explicitly mark the atom as `unverifiable: source_not_provided` and ask.

### Step 3: Locate the supporting passage
Inside the source, find the actual sentence(s) that justify the claim. Quote the relevant passage verbatim (with page number). If the source does not contain anything close to the claim, mark `hallucinated`. If it contains a related-but-different argument, mark `miscited`.

### Step 4: Score the atom
Apply this rubric and produce one label per atom:

- `strong` — the source contains an explicit, in-context statement of the claim.
- `moderate` — the source supports a near-version of the claim with reasonable interpretation; consider rewording.
- `weak` — the source is tangentially related; the claim leans on it more than the text supports. Recommend either softening the claim or adding a stronger source.
- `miscited` — the source exists but does not say what is attributed to it. Must be fixed.
- `hallucinated` — the source itself does not exist (no DOI, not findable in any database) OR the page/quote was invented. Must be removed.
- `unverifiable` — could not access the source; user must provide it.

### Step 5: Suggest a fix per problem atom
For `weak`/`miscited`/`hallucinated` atoms: propose either (a) a rewrite of the sentence that is honestly supportable by what the source actually says, or (b) suggest 1-2 alternative sources from the user's known reading list that DO support the claim. Never invent a fix that introduces a new uncited assertion.

### Step 6: Produce the audit report
A single table the user can paste into a doc, plus a short narrative summary highlighting any hallucinated citations FIRST (these are existential risks in a thesis defense).

## Output format

A Markdown report with three sections:

```
## Citation Integrity Audit — <document title>

### Summary
- Total citations checked: N
- Strong: X | Moderate: Y | Weak: Z | Miscited: A | Hallucinated: B | Unverifiable: C
- Critical issues: <bullet list of every miscited / hallucinated finding>

### Per-citation table
| # | Sentence (truncated) | Citation | Verdict | Evidence quote (with page) | Suggested fix |
|---|---|---|---|---|---|
| 1 | "Dynamic capabilities allow firms to..." | (Teece, 2007) | strong | "...sense, seize, and reconfigure..." (p. 1319) | — |

### Recommended next actions
1. Remove citation #X (hallucinated)
2. Replace citation #Y with <alternative> (miscited)
3. Soften claim attached to citation #Z (weak)
```

## Quality checklist
- [ ] Every citation in the input was extracted (no atom skipped).
- [ ] Hallucinated and miscited findings are listed FIRST in the summary.
- [ ] No fix introduces a new uncited assertion.
- [ ] Page numbers are preserved or requested when missing.
- [ ] Verdicts use only the six rubric labels — no novel terms.
- [ ] If any source could not be accessed, the atom is marked `unverifiable` rather than guessed.

## Notes for the assistant
- **Never invent a source to satisfy a citation.** If a reference cannot be found in any database AND the user did not provide the PDF, the only honest verdict is `hallucinated` or `unverifiable`. This is the entire point of the skill.
- LLM-generated text very frequently invents (a) plausible author names with wrong years, (b) real authors attached to papers they did not write, (c) real papers with wrong page numbers. Be skeptical of any citation whose paper-author-year triple has not been independently confirmed.
- Direct quotes require page numbers in APA 7. If a direct quote has no page number, flag it under "Recommended next actions" even if the citation is otherwise strong.
- For paraphrases of a *specific* argument (not a general field claim), page numbers are recommended best practice — note this gently, do not flag as an error.
- Keep the tone of the audit neutral and factual. The user is not being scolded; the goal is a defensible thesis.
- Do not rewrite the user's prose beyond the suggested fix for problem atoms.
