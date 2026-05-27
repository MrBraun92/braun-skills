---
name: systematic-literature-review
description: Runs a PRISMA-style systematic literature review for a UiS Management master's thesis (English, APA 7) on topics like AI advisory, dynamic capabilities, service quality, or related management constructs. Accepts PDFs from Google Drive, lists of DOIs, and structured searches across Semantic Scholar, OpenAlex, Elicit, Scopus, Web of Science, and Google Scholar. Outputs an APA 7 reference list, an inclusion/exclusion table, a PRISMA flow, and a thematic synthesis. Use when the user says "do a literature review", "build my SLR", "PRISMA", "find papers on X", "systematic search".
---

# Systematic Literature Review

Executes a transparent, auditable systematic literature review (SLR) following PRISMA-style reporting, suitable for a UiS master's thesis in Management (English, APA 7) on themes such as AI advisory, dynamic capabilities, service quality, and related constructs. Outputs a defensible search log, screening trail, and thematic synthesis — not a vibes-based summary.

## When to use this skill
- The user is starting or rebuilding the Literature Review chapter of the thesis.
- The user wants to defend "I covered the field" to a thesis supervisor or examiner.
- A research gap claim needs a transparent search to back it up.
- The supervisor asked for a PRISMA flow diagram or an SLR appendix.
- An existing reading pile needs to be turned into a structured corpus with thematic analysis.

## Methodology

### Step 1: Define the protocol
Before any search runs, write the protocol explicitly. Confirm with the user:
- **Research question(s)** — phrased so they can be answered with literature.
- **Population / Concepts / Context (PCC)** — e.g., Population = SMB service firms; Concepts = AI advisory + dynamic capabilities + service quality; Context = post-2018 digital transformation.
- **Inclusion criteria** — language (English), date range (e.g., 2014-present), peer-reviewed only, study type (empirical / conceptual / both), field (management/IS/marketing).
- **Exclusion criteria** — opinion pieces, non-English, pre-2014, unpublished theses, etc.
- **Databases to query** — at minimum two of: Scopus, Web of Science, Semantic Scholar, OpenAlex, Elicit, Google Scholar.
- **Search string** — Boolean with synonyms; show it to the user before running.

### Step 2: Execute the search
For each database, record: search string used, date of search, number of hits. Save the raw export (CSV/RIS) when possible. If the user is providing a pile of PDFs from Google Drive, treat that as the corpus and skip to Step 4 — but mark the SLR as "purposive sample, not exhaustive search" so the limitation is documented honestly.

### Step 3: Deduplicate
Merge databases. Deduplicate by DOI first, then by (title + first-author + year) fuzzy match. Record the count of duplicates removed.

### Step 4: Screen by title + abstract
Apply inclusion/exclusion to the title + abstract. Record exclusion reasons in a structured way (e.g., "wrong context", "not empirical", "language", "duplicate"). Output the count of articles excluded at this stage.

### Step 5: Full-text screen
For survivors: read full text (or have the user provide PDFs). Apply criteria again. Record exclusion reasons per paper. The remaining set is the **final corpus**.

### Step 6: Extract data
For each paper in the corpus, populate a row in the extraction table with: author(s), year, title, journal, country/context, theoretical lens, methodology, sample, key constructs, key findings, relevance to the thesis RQ.

### Step 7: Thematic synthesis
Group findings into 4-7 themes. For each theme: name it, list the papers contributing, summarize the consensus and the disagreements, and identify the gap that the thesis can address. This is what becomes the Literature Review narrative — not a paper-by-paper recitation.

### Step 8: Build the deliverables
Produce all six artifacts listed under Output format.

## Output format

Six artifacts, all in Markdown, ready to paste into the thesis appendix or main text:

1. **Protocol summary** — RQ, PCC, criteria, databases, search string, search date.
2. **PRISMA flow numbers** — Identification → Screening → Eligibility → Included, with counts at each stage and exclusion reasons. (The visual diagram itself is produced by the `scientific-schematics` skill from these numbers.)
3. **Search log table** — | Database | Date | Search string | Hits |
4. **Extraction table** — one row per included paper, columns as in Step 6.
5. **Thematic synthesis narrative** — 4-7 themes with consensus, disagreement, and gap per theme.
6. **APA 7 reference list** — every included paper formatted strictly per APA 7 (ampersand, italicized journal name, volume(issue), pages, DOI as `https://doi.org/...`). Pair with the `apa-style-enforcer` skill to verify.

## Quality checklist
- [ ] Protocol was confirmed with the user BEFORE any search ran.
- [ ] Every database query is logged with date and exact string.
- [ ] Deduplication count is reported.
- [ ] Screening exclusion reasons are categorized (not free text).
- [ ] Final corpus size is justifiable for a master's thesis (typically 30-80 papers; depends on scope).
- [ ] Thematic synthesis names a research gap that the thesis can plausibly fill.
- [ ] APA 7 reference list passes formal validation (use `apa-style-enforcer`).
- [ ] PRISMA numbers reconcile (Identified - Duplicates - Excluded at TitleAbstract - Excluded at FullText = Included).

## Notes for the assistant
- This skill is doing **honest** systematic review, not curating a flattering reading list. If a study contradicts the thesis's hypothesis, include it and engage with it.
- The thesis is in English. Default search language is English. If the user wants Norwegian or Portuguese sources for a specific reason (e.g., cultural context), say so explicitly in the protocol.
- For a master's thesis (not a doctoral SLR), it is acceptable to use 2 databases + Google Scholar for snowballing rather than the full PRISMA 2020 multi-database protocol. State the choice in the protocol so the supervisor can approve.
- If the user provides a pile of PDFs without a search step, the deliverable is a **purposive review**, not a systematic one. Be explicit about this in the protocol summary so the limitation is documented.
- For AI advisory + dynamic capabilities + service quality, anchor authors are usually: Teece (1997, 2007, 2014), Eisenhardt & Martin (2000), Parasuraman, Zeithaml & Berry (1985, 1988), Davenport & Ronanki (2018) on AI in business, Brynjolfsson & McAfee for digital transformation. If these don't appear after a search, double-check the search string.
- Pair this skill with `apa-style-enforcer` (for citations) and `scientific-schematics` (for the PRISMA diagram).
- Do NOT fabricate papers. If a search returns nothing on a thread, say so.
