---
name: academic-tone-polisher
description: Polishes academic English prose for clarity, naturalness, hedging conventions of management research, and passive/active voice balance — without rewriting the user's argument. Strips "AI giveaway" phrasing (delve, tapestry, navigate the landscape, embark on a journey, etc.) that signals lazy LLM output. Does NOT mask AI assistance — only legitimate copyediting. Use when the user says "polish this", "make this sound more academic", "fix the writing", "remove AI tells", or "tighten this paragraph". Built for a UiS Management master's thesis (English, APA 7).
---

# Academic Tone Polisher

Refines academic English prose to the conventions of management research journals — clear, hedged appropriately, neither overconfident nor flabby — while staying inside the user's argument. The goal is the user's voice on a good day, not a generic AI-blob voice. Does not paraphrase, does not invent claims, does not mask AI assistance — disclosure is the user's responsibility, this skill is just copyediting.

## When to use this skill
- A paragraph reads OK but feels off and the user can't say why.
- A draft was produced with LLM help and now needs the AI tells removed.
- The user wants tighter sentences without changing the argument.
- Hedging language is wrong (overconfident or wishy-washy).
- A reviewer/supervisor said "the writing needs work" without specifics.

## Methodology

### Step 1: Confirm scope
Ask: paragraph, section, or full chapter? Heavy edit (rewrite for clarity) or light edit (polish only)? In Management research, hedging is expected; in some hard-science fields it isn't. Confirm.

### Step 2: Read for AI giveaways and remove them
Common LLM tells in academic writing — flag and replace:

- "**Delve into**" → "examine", "analyze", "investigate".
- "**Embark on a journey**" → just delete; nothing replaces it because it shouldn't be there.
- "**Navigate the landscape of**" → "review the literature on", "examine".
- "**Tapestry of**" → "set of", "range of", or just delete.
- "**Multifaceted**" / "**ever-evolving**" / "**dynamic landscape**" → use specific descriptors instead.
- "**It is important to note that**" → just state the thing.
- "**In conclusion**" / "**In summary**" → delete; the conclusion paragraph is itself the conclusion.
- "**Furthermore, moreover, additionally**" stacked across consecutive sentences → vary or remove.
- "**Robust**" used 8 times in a chapter → real word but overused by LLMs as filler praise.
- "**Underscores**" / "**highlights**" / "**sheds light on**" used as connectives → vary.
- "**Plays a crucial role**" → either name the role specifically or delete.
- "**A growing body of literature**" without citations → either cite or remove; this is the laziest LLM stock phrase.
- Excessive em-dash use (— — —) when commas / colons would do.
- Three-item lists with abstract nouns ("efficiency, effectiveness, and excellence") that pad without adding.

### Step 3: Calibrate hedging
Management research uses hedged claims by convention. Calibrate:

- **Overconfident** ("This proves...", "It is clear that...") → "These findings suggest that...", "The data are consistent with...".
- **Underconfident** / wishy-washy ("It might possibly be the case that perhaps...") → state what is supportable directly, then hedge with one device, not three.
- **Hedging vocabulary** (use sparingly): suggest, indicate, appear to, may, are consistent with, point toward, plausibly.
- **Strong claims are allowed** when supported. "Sensing capability is a precondition for transformation" — fine if Teece (2007) supports it directly. Hedging everything dilutes the contribution.

### Step 4: Voice — active vs passive
Management journals lean toward active voice in introduction and discussion, and accept passive voice in methods. Apply:

- **Methods**: passive often appropriate ("Interviews were conducted", "Data were coded thematically"). Don't force active.
- **Introduction / Lit review / Discussion**: active preferred where natural ("Teece (2007) argues" not "It has been argued by Teece (2007) that...").
- **Findings**: mixed. "Participants described..." (active) is good. "It was reported that..." (passive) is weak.
- **Avoid**: dangling agency ("This was investigated" — by whom?). Add the agent.

### Step 5: Sentence length and rhythm
- Average sentence length in academic Management writing: 18-25 words. Too long (40+) loses the reader; too short (<10) feels choppy.
- If three consecutive sentences exceed 30 words, split one.
- If five consecutive sentences are short and declarative, combine two.
- Avoid serial subordinate clauses that bury the verb.

### Step 6: Word choice and register
- Prefer specific over abstract: "8 of 12 participants" beats "many participants".
- Prefer Anglo-Saxon over Latinate when both work: "use" beats "utilize", "show" beats "demonstrate" when the meaning is identical.
- Avoid: literally, basically, very, really, quite (intensifiers that weaken).
- Cap "very" to zero uses per chapter unless quoting a participant.

### Step 7: Run the polish
Produce a side-by-side: original sentence → polished sentence → reason for change. This lets the user accept/reject per-edit and learn the pattern.

### Step 8: Final check
Re-read the polished version end-to-end. Does it still sound like the user, only sharper? If it sounds like generic academic mush, the polish went too far — back off.

## Output format

```
## Tone Polish — <section title>

### Heavy edits (substantive)
| Original | Polished | Reason |
|---|---|---|

### Light edits (word-level)
| Location | Change |
|---|---|

### AI giveaways removed
| Phrase removed | Replacement | Count |
|---|---|---|

### Hedging calibration
- Overconfident claims softened: <list>
- Wishy-washy claims firmed: <list>

### Polished version (full text)
<the rewritten section>
```

## Quality checklist
- [ ] Every change is logged so the user can review and reject.
- [ ] No new claim was introduced.
- [ ] No citation was added or removed.
- [ ] Hedging is calibrated to evidence strength, not blanket-applied.
- [ ] AI giveaway phrases are documented in the report (so the user can also avoid them in future drafts).
- [ ] The polished version still sounds like the user — not like a generic LLM rewrite.
- [ ] Methods sections retained appropriate passive voice.

## Notes for the assistant
- Do NOT mask AI use. The user's job is to disclose AI assistance per UiS policy. This skill is only doing the copyediting that any human editor would do — it does not "launder" AI prose.
- The user is non-native English at presumably advanced level (UiS thesis). Idioms that are slightly off, prepositions that drift — fix gently. Don't strip Norwegian-influenced rhythm if it reads natural.
- Resist the temptation to "improve" the user's argument. If a sentence is unclear because the *idea* is unclear, flag it ("this sentence is hard to follow — what are you trying to say?") instead of rewriting and possibly distorting.
- Common AI giveaways to watch beyond the list above: starting paragraphs with "In the realm of", over-using triadic structures, generic transitions ("It is also worth noting"), and conclusion paragraphs that recap rather than synthesize.
- For Discussion chapters, hedging is heavier than in Findings. "These findings suggest that..." in Discussion vs "Participants reported..." in Findings.
- Pair with `academic-paper-reviewer` (which catches structural issues) and `apa-style-enforcer` (formatting) — this skill is the prose layer.
- The user is a non-programmer building a startup; their natural voice may have business / strategy register. That's fine in a Management thesis — keep it, just elevate it.
