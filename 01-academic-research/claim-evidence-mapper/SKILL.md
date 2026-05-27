---
name: claim-evidence-mapper
description: Maps every argument in a thesis chapter or paper to the specific evidence that backs it, classifying support strength as strong/moderate/speculative. Use when drafting or auditing a Discussion section, a Literature Review, or a Findings chapter, when the user says "is my argument supported?" / "what's my evidence for X?" / "build my claim ladder", or before sending a chapter to a thesis supervisor. Built for a UiS Management master's thesis in English on AI advisory, dynamic capabilities and service quality.
---

# Claim-Evidence Mapper

Decomposes an academic chapter into discrete claims, attaches the specific evidence that backs each one, and rates the support so the author sees — at a glance — which arguments are load-bearing and which are floating. Designed for the Discussion and Literature Review chapters of a UiS master's thesis (English, APA 7, Management field).

## When to use this skill
- The user is auditing a chapter before sending it to the supervisor.
- A reviewer flagged "this needs more support" / "where does this come from?"
- The user is restructuring an argument and needs to see what's load-bearing.
- A Discussion section was drafted from interview data and needs traceability.
- The user wants to know which claims to soften vs which to defend.

## Methodology

### Step 1: Extract claims
Read the chapter and pull every assertion that takes a position (excluding pure summary of someone else's work — that's already a citation, not a claim). A claim is anything that could plausibly be challenged in a viva. Number each claim. Keep the original sentence verbatim alongside the extracted claim for traceability.

### Step 2: Classify claim type
For each claim, tag one of:
- `theoretical` — derives from the conceptual framework (e.g., "dynamic capabilities require sensing, seizing, transforming").
- `empirical-literature` — derives from prior empirical studies.
- `empirical-own` — derives from the user's own data (interviews, survey, archival).
- `interpretive` — the user's synthesis on top of either of the above.
- `methodological` — about how the study was done.

This matters because evidence requirements differ by type.

### Step 3: Attach evidence
For each claim, list the specific evidence that supports it:
- For `empirical-literature`: cite the paper + page. Reuse the citation-integrity-checker skill if uncertain whether the citation actually says what's attributed.
- For `empirical-own`: name the participant ID + interview line/quote, OR the table/figure number, OR the survey item.
- For `theoretical`: name the foundational source (Teece 2007, Eisenhardt & Martin 2000, Parasuraman et al. 1988 — whichever applies).
- For `interpretive`: name the underlying claims (#3 + #7) that the interpretation rests on.

### Step 4: Rate support strength
Per claim, assign one of:
- `strong` — multiple independent sources OR a clear, named primary source AND consistent with the user's own data.
- `moderate` — one good source OR a partial pattern in the data; defensible but reviewers may push back.
- `speculative` — no direct source; interpretive leap; "in our view"; could be challenged in the viva.
- `unsupported` — no evidence found. Must either be cut, supported, or explicitly framed as a research question / proposition.

### Step 5: Flag the load-bearing chain
Identify which claims the chapter's main contribution depends on. If a `speculative` claim is load-bearing — that is the single most important finding of this audit. Make it visible.

### Step 6: Suggest fixes
For `speculative` and `unsupported` load-bearing claims, suggest one of:
- Find a supporting source (and where to look).
- Soften the claim to match the available evidence.
- Reframe as a proposition / hypothesis for future work.
- Cut.

## Output format

A two-part Markdown deliverable:

```
## Claim-Evidence Map — <chapter title>

### Master table
| # | Claim (verbatim) | Type | Evidence | Strength | Load-bearing? |
|---|---|---|---|---|---|

### Load-bearing chain
A short narrative: "The chapter's main contribution is X. It depends on claims #2, #5, #11. Of these, claim #5 is currently `speculative` — see fix below."

### Recommended fixes
1. Claim #5 → ...
2. Claim #11 → ...
```

## Quality checklist
- [ ] Every assertive sentence in the chapter became a numbered claim (no skipped ground).
- [ ] Claim types are assigned consistently (no mixing theoretical and empirical-own).
- [ ] Evidence pointers are specific (paper + page, participant ID + line, NOT "see chapter 4").
- [ ] At least one claim is identified as load-bearing for the contribution.
- [ ] Speculative load-bearing claims are listed FIRST under "Recommended fixes".
- [ ] No new citations are invented to make a weak claim look strong.

## Notes for the assistant
- This skill is not a writing skill. Do not rewrite prose. Output is an audit table the author uses to revise.
- "Load-bearing" is a judgement call. State the chain explicitly so the user can disagree: "I treated claim #5 as load-bearing because the contribution sentence in §6.1 references it directly."
- In Management research, interpretive claims are normal and expected — but they must be flagged as interpretive, not laundered as empirical.
- For interview-based claims, the participant pseudonym + line number is the evidence. Suggest the user paste the relevant transcript chunk if it isn't accessible.
- Be willing to tell the user that a beloved claim is unsupported. The thesis is improved by cutting one weak argument, not by pretending it's strong.
- This skill pairs with `theoretical-integration` (when the claim chain is built but the synthesis is missing) and `devils-advocate-research` (to stress-test the claims after they're mapped).
