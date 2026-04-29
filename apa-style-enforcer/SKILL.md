---
name: apa-style-enforcer
description: Enforces APA 7th edition formatting strictly across in-text citations, reference list, headings, tables, figures, statistics reporting (p, η², CI, M, SD), and DOIs. Validates an existing draft and fixes violations, OR formats a new reference list / citation set from scratch. Use when the user says "check APA", "fix my references", "APA 7", "format my citations", "is this APA-compliant", "verify reference list". Built for a UiS Management master's thesis in English where APA 7 is the required style.
---

# APA Style Enforcer

The single source of truth for APA 7th edition compliance in a UiS Management master's thesis (English). Catches the violations that cost marks: ampersand vs "and" rules, italics vs roman, DOI as URL, page-number requirements for direct quotes, statistical notation, heading levels, table notes, figure captions. Replaces the casual "looks APA-ish" pass with a defensible audit.

## When to use this skill
- Final pass before submission to the supervisor or examiner.
- Reference list assembled from multiple sources and consistency is suspect.
- A statistical results section needs review (p-value notation, effect sizes, CIs).
- A citation cluster has multiple authors and the user is unsure of "et al." rules.
- DOIs need conversion from "doi:10.x" to APA 7 "https://doi.org/10.x" format.

## Methodology

### Step 1: Confirm scope
Ask: full document, or a section? Reference list only, or in-text + reference list? With or without statistical results review? The deliverable depends on the answer.

### Step 2: Validate in-text citations
Apply APA 7 rules:

- **Single author**: (Teece, 2007).
- **Two authors**: always cite both, with `&` inside parentheses, "and" in narrative — `(Eisenhardt & Martin, 2000)` vs "Eisenhardt and Martin (2000) argued...".
- **3+ authors**: first citation AND every subsequent citation use `et al.` — `(Parasuraman et al., 1988)`. Do NOT spell all authors on first use (that was APA 6).
- **Same author multiple works same year**: `(Teece, 2007a, 2007b)`.
- **Multiple sources in same parens**: alphabetical, semicolon-separated — `(Eisenhardt & Martin, 2000; Teece, 2007)`.
- **Direct quote**: must include page number — `(Teece, 2007, p. 1319)`. Best practice for paraphrases of specific arguments too.
- **Group/organizational author**: spell out first time with abbreviation — `(World Health Organization [WHO], 2020)`, then `(WHO, 2020)`.
- **No author**: cite by title (italicized for books/reports, in quotes for articles).
- **Personal communication**: in-text only, never in reference list.

Flag every violation with location reference.

### Step 3: Validate the reference list
Apply APA 7 rules:

- **Order**: alphabetical by first author surname.
- **Hanging indent**: 0.5 inch / 1.27 cm.
- **Author format**: Last, F. M. (with initials, period after each).
- **Up to 20 authors**: list all. **21+ authors**: first 19, then `…`, then last author.
- **Year**: in parentheses immediately after authors — `Teece, D. J. (2007).`
- **Title of article**: sentence case (capitalize only first word + proper nouns + first word after colon). NOT title case.
- **Title of journal**: title case AND italicized.
- **Volume**: italicized, no "vol." prefix. Issue: in parentheses, NOT italicized — `Strategic Management Journal, 28(13), 1319-1350.`
- **Page numbers**: en-dash, no "pp." for journals.
- **DOI**: `https://doi.org/10.1002/smj.640` — full URL, lowercase "doi", no period after.
- **Books**: Publisher name only, no city — APA 7 dropped the location requirement.
- **Edited books / chapters**: `In F. Editor (Ed.), Book title (pp. 100-120). Publisher.`
- **Reports / grey literature**: include URL if online; institutional author allowed.
- **Online sources**: include retrieval date ONLY if the content is expected to change (wiki, news feed). For static documents, no retrieval date.

### Step 4: Validate headings
APA 7 heading levels (used in thesis chapters):

- Level 1: Centered, Bold, Title Case.
- Level 2: Flush Left, Bold, Title Case.
- Level 3: Flush Left, Bold Italic, Title Case.
- Level 4: Indented, Bold, Title Case, Period (paragraph runs on).
- Level 5: Indented, Bold Italic, Title Case, Period (paragraph runs on).

Most master's theses use Levels 1-3 only. Flag if user mixes levels inconsistently.

### Step 5: Validate tables and figures
- Tables and figures both number sequentially across the whole thesis (Table 1, Table 2 ... Figure 1, Figure 2 ...).
- Table number bold, on its own line. Title italicized, title case, on next line. Body of the table follows.
- Figure number bold, on its own line. Title italicized, title case, next line. Image. Note below in plain text starting with italicized "Note." (period).
- Every table/figure must be referenced in body text by number ("As shown in Table 3...").

### Step 6: Validate statistical notation
- Means and SDs: `M = 4.32, SD = 0.81`. Italicize letters, space around `=`.
- t-test: `t(df) = value, p = .xxx, d = value`. Italicize t, p, d.
- ANOVA: `F(df1, df2) = value, p = .xxx, η² = value`.
- p-values: drop leading zero, three decimals — `p = .032`, not `p = 0.032`. For p < .001, write `p < .001`.
- Confidence intervals: `95% CI [lower, upper]`. Always state level.
- Correlations: `r(df) = .43, p = .002`.
- Effect sizes always reported alongside significance tests.

### Step 7: Produce the audit report
A diff-style list of violations with line/section references and corrected versions. Group by category: in-text, reference list, headings, tables/figures, stats.

### Step 8: Optionally produce a corrected version
If the user wants the document fixed, not just audited: produce a clean rewrite of the reference list and a tracked-change list of in-text citation corrections. Headings and table formatting are typically guidance only since they depend on Word/LaTeX styling.

## Output format

```
## APA 7 Audit — <document title>

### Summary
- In-text citation violations: N
- Reference list violations: N
- Heading violations: N
- Table/figure violations: N
- Statistical notation violations: N

### In-text citation issues
| Location | Current | APA 7 corrected | Rule |
|---|---|---|---|

### Reference list issues
| Entry | Issue | Corrected entry |
|---|---|---|

### Heading issues
| Section | Current | Corrected |
|---|---|---|

### Table / figure issues
| Number | Issue | Corrected |
|---|---|---|

### Statistical notation issues
| Location | Current | Corrected |
|---|---|---|

### Clean reference list (if requested)
<full corrected list, hanging-indent ready>
```

## Quality checklist
- [ ] Every in-text citation in the document was checked.
- [ ] Reference list is alphabetically ordered.
- [ ] All DOIs are in the `https://doi.org/...` format.
- [ ] All journal titles are italicized; all article titles are sentence case.
- [ ] `et al.` is used from the FIRST citation for 3+ authors.
- [ ] Direct quotes have page numbers.
- [ ] Statistics use italicized symbols and APA 7 punctuation.
- [ ] Headings use the correct APA 7 level format.
- [ ] No personal communications appear in the reference list.

## Notes for the assistant
- APA 7 vs APA 6 differences that trip up users: (a) `et al.` from first citation, (b) DOI as URL not "doi:", (c) up to 20 authors listed, (d) no publisher city for books, (e) no "Retrieved from" for stable URLs.
- When in doubt about a journal, use the journal's own DOI page or Crossref to confirm volume/issue formatting.
- Sentence case in article titles is the most common mistake — `Dynamic capabilities and strategic management` (correct), not `Dynamic Capabilities and Strategic Management` (wrong).
- Em-dash vs en-dash: page ranges use en-dash (`100-120`), not hyphen.
- The thesis is in English. If the user has occasional Norwegian or Portuguese sources, transliterate titles per APA 7 rules (translation in brackets if helpful) but keep original-language title intact.
- This skill validates form, not fact. Pair with `citation-integrity-checker` to verify the citation actually says what's attributed to it.
- Some examiners are stricter than the actual APA 7 manual. If the supervisor has a personal style preference, log it and apply consistently — do not argue with the supervisor.
- Word's built-in APA tool is unreliable. Zotero/Mendeley with the official APA 7 CSL is acceptable; trust-but-verify against this skill.
