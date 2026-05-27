---
name: qualitative-coding-specialist
description: Performs rigorous qualitative coding of interview transcripts, focus groups, or open-ended survey data. Runs open coding, axial coding, and thematic analysis (Braun & Clarke or Gioia methodology) and outputs an auditable codebook plus theme map. Partial replacement for NVivo/Atlas.ti when the user just needs the analysis output, not the software UI. Use when the user says "code my interviews", "thematic analysis", "open coding", "Gioia method", "build my codebook", or pastes interview transcripts asking what's in them. Built for a UiS Management master's thesis in English under APA 7.
---

# Qualitative Coding Specialist

Performs auditable qualitative coding of interview transcripts and open-text data for a UiS master's thesis in Management. Implements the methodologies that thesis examiners actually accept (Braun & Clarke 2006/2022 for thematic analysis; Gioia, Corley & Hamilton 2013 for grounded theory style coding) and produces the artifacts a methods chapter requires: codebook, theme map, exemplar quotes per theme, audit trail.

## When to use this skill
- User has 1-N interview transcripts, focus group transcripts, or open-ended survey responses.
- Thesis methods chapter requires "open coding", "axial coding", "thematic analysis", or "Gioia 1st-order / 2nd-order / aggregate dimensions".
- User wants to defend "where did this theme come from?" with traceable evidence.
- User wants a partial substitute for NVivo / Atlas.ti / MAXQDA without the software.
- User is building the Findings chapter and needs structure, not just summary.

## Methodology

### Step 1: Confirm the methodology
Ask the user (or infer from the methods chapter draft) which approach is being used:
- **Braun & Clarke reflexive thematic analysis** — six phases: familiarization, initial codes, generating themes, reviewing, defining, writing up. Acknowledges researcher subjectivity.
- **Gioia methodology** — 1st-order concepts (informant terms) → 2nd-order themes (researcher concepts) → aggregate dimensions. Particularly common for grounded theory in management.
- **Template analysis** (King) — when the codebook is partly pre-defined from theory.
- **Framework analysis** — common in applied/policy research with a pre-existing framework.

If the user does not know, default to **reflexive thematic analysis** for an inductive thesis or **Gioia** if the contribution is a process model — and explain the choice.

### Step 2: Familiarization
Read each transcript end-to-end first. Produce a one-paragraph memo per interview: who, what role, key moments, surprises. This becomes the audit trail and helps the user remember context later.

### Step 3: Open coding (1st-order codes)
Code line-by-line or meaning-unit-by-meaning-unit. A code is a short descriptive label staying close to the participant's language (Gioia: "in-vivo" / informant terms). For each code, record: code label, definition, exemplar quote, participant ID, transcript line. Aim for 60-150 1st-order codes for a typical master's thesis dataset; collapse near-duplicates only after Step 5.

### Step 4: Axial coding (2nd-order themes)
Group 1st-order codes by conceptual relatedness. Each theme gets: theme name (researcher's analytic term, may use theoretical vocabulary), definition, list of contributing 1st-order codes, list of supporting participants, 2-3 exemplar quotes. Aim for 8-20 2nd-order themes.

### Step 5: Aggregate dimensions (Gioia) or Final themes (Braun & Clarke)
Cluster 2nd-order themes into 3-6 aggregate dimensions / final themes. Each dimension links to the conceptual framework of the thesis (e.g., "Sensing capability", "Seizing capability", "Transformation capability" if dynamic capabilities is the lens; or "Reliability", "Responsiveness", "Empathy" if SERVQUAL is the lens — but only if the data actually supports those buckets, not because theory says so).

### Step 6: Build the data structure
Produce the canonical Gioia data structure visualization (3-column tree: 1st-order → 2nd-order → aggregate). Even for Braun & Clarke, a similar artifact helps examiners see provenance.

### Step 7: Quote selection for the Findings chapter
For each 2nd-order theme, select 1-3 quote candidates that are: vivid, representative, brief, and span multiple participants. Mark each with participant pseudonym + line number.

### Step 8: Write the audit trail
A short methods sub-section: how codes were generated, by whom (the user), how disagreements were handled (single coder is acceptable for a master's thesis if reflexivity is acknowledged), what software/tool was used (if any), whether saturation was reached.

## Output format

A Markdown deliverable with five sections:

```
## Qualitative Coding — <project name>

### 1. Methodology used
<Braun & Clarke / Gioia / Template / Framework — and why>

### 2. Familiarization memos
- Interview P01: <2-3 sentences>
- Interview P02: <2-3 sentences>
...

### 3. Codebook (master table)
| Code ID | 1st-order code | Definition | Participants | Example quote (P, line) | 2nd-order theme | Aggregate dimension |
|---|---|---|---|---|---|---|

### 4. Data structure (Gioia tree)
- Aggregate dimension A
  - 2nd-order theme A1
    - 1st-order code a1, a2, a3
  - 2nd-order theme A2
    - 1st-order code a4, a5
- Aggregate dimension B
  ...

### 5. Selected quotes for Findings chapter
- Theme A1: "..." (P03, line 142)
- Theme A2: "..." (P07, line 89)

### 6. Audit trail / methods note
<3-4 sentences for the methods chapter>
```

## Quality checklist
- [ ] Methodology is named explicitly (Braun & Clarke OR Gioia OR ...).
- [ ] Every 1st-order code traces to at least one participant + line number.
- [ ] No 2nd-order theme exists without ≥2 contributing 1st-order codes.
- [ ] No aggregate dimension exists without ≥2 contributing 2nd-order themes.
- [ ] Quotes are verbatim (no smoothing, no edits beyond `[...]` for elision).
- [ ] Participant pseudonyms are consistent (P01, P02, ... — never real names).
- [ ] Saturation status is stated honestly.
- [ ] Reflexivity note is included (single-coder bias acknowledged for a master's thesis).

## Notes for the assistant
- **Anonymize aggressively.** If a transcript still contains real names, employer names, locations that could deanonymize a participant — flag them and ask the user to confirm replacement. SIKT (UiS ethics body) requires this.
- Coding is interpretive. Two coders would produce slightly different codebooks. State this in the audit trail rather than pretending to objectivity.
- Do not force theory onto data. If SERVQUAL was the planned lens but the data is screaming about trust and emotion, name what the data actually says and let the Discussion chapter reconcile it.
- Code definitions matter — a vague definition lets one code absorb everything. Each definition should be 1-2 sentences and exclude what the code is NOT.
- For a master's thesis, 5-15 interviews is normal. Do not invent saturation if the corpus is small — say "indicative themes, not saturated" if that's the truth.
- Pair with `theoretical-integration` skill when the themes need to connect to the literature, and `research-ethics-sikt-reviewer` skill when ensuring participant data handling is compliant.
- Do not produce findings the data does not support. The thesis is defended by traceability, not by elegance.
