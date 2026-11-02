# Fase 4: Geração

> Extraído sem alteração de conteúdo do SKILL.md original (linhas 677-865).

### Phase 4: Generation Phase

**Goal:** Create professional multi-format outputs

**Inputs:**
- Approved content mapping (from Phase 3)
- User's formatting preferences (from library analysis)
- Target role information (from Phase 1)

**Process:**

**4.1 Markdown Generation:**

**Compile mapped content into clean markdown:**

```markdown
# {User_Name}

{Contact_Info}

---

## Professional Summary

{Summary_from_template}

---

## Key Skills

**{Category_1}:**
- {Skills_from_library_matching_profile}

**{Category_2}:**
- {Skills_from_library_matching_profile}

{Repeat for all categories}

---

## Professional Experience

### {Job_Title}
**{Company} | {Location} | {Dates}**

{Role_summary_if_applicable}

• {Bullet_1_from_mapping}
• {Bullet_2_from_mapping}
...

### {Next_Role}
...

---

## Education

**{Degree}** | {Institution} ({Year})
**{Degree}** | {Institution} ({Year})
```

**Use user's preferences:**
- Formatting style from library analysis
- Bullet structure pattern
- Section ordering
- Typical length (1-page vs 2-page)

**Output:** `{Name}_{Company}_{Role}_Resume.md`

**4.2 DOCX Generation:**

**Use document-skills:docx:**

```
REQUIRED SUB-SKILL: Use document-skills:docx

Create Word document with:
- Professional fonts (Calibri 11pt body, 12pt headers)
- Proper spacing (single within sections, space between)
- Clean bullet formatting (proper numbering config, NOT unicode)
- Header with contact information
- Appropriate margins (0.5-1 inch)
- Bold/italic emphasis (company names, titles, dates)
- Page breaks if 2-page resume

See docx skill documentation for:
- Paragraph and TextRun structure
- Numbering configuration for bullets
- Heading levels and styles
- Spacing and margins
```

**Output:** `{Name}_{Company}_{Role}_Resume.docx`

**4.3 PDF Generation (Optional):**

**If user requests PDF:**

```
OPTIONAL SUB-SKILL: Use document-skills:pdf

Convert DOCX to PDF OR generate directly
Ensure formatting preservation
Professional appearance for direct submission
```

**Output:** `{Name}_{Company}_{Role}_Resume.pdf`

**4.4 Generation Summary Report:**

**Create metadata file:**

```markdown
# Resume Generation Report
**{Role} at {Company}**

**Date Generated:** {timestamp}

## Target Role Summary
- Company: {Company}
- Position: {Role}
- IC Level: {If known}
- Focus Areas: {Key areas}

## Success Profile Summary
- Key Requirements: {top 5}
- Cultural Fit Signals: {themes}
- Risk Factors Addressed: {mitigations}

## Content Mapping Summary
- Total bullets: {N}
- Direct matches: {N} ({percentage}%)
- Transferable: {N} ({percentage}%)
- Adjacent: {N} ({percentage}%)
- Gaps identified: {list}

## Reframing Applied
- {bullet}: {original} → {reframed} [Reason: {why}]
...

## Source Resumes Used
- {resume1}: {N} bullets
- {resume2}: {N} bullets
...

## Gaps Addressed

### Before Experience Discovery:
{Gap analysis showing initial state}

### After Experience Discovery:
{Gap analysis showing final state}

### Remaining Gaps:
{Any unresolved gaps with recommendations}

## Key Differentiators for This Role
{What makes user uniquely qualified}

## Recommendations for Interview Prep
- Stories to prepare
- Questions to expect
- Gaps to address
```

**Output:** `{Name}_{Company}_{Role}_Resume_Report.md`

**Present to user:**
```
"Your tailored resume has been generated!

FILES CREATED:
- {Name}_{Company}_{Role}_Resume.md
- {Name}_{Company}_{Role}_Resume.docx
- {Name}_{Company}_{Role}_Resume_Report.md
{- {Name}_{Company}_{Role}_Resume.pdf (if requested)}

QUALITY METRICS:
- JD Coverage: {percentage}%
- Direct Matches: {percentage}%
- Newly Discovered: {N} experiences

Review the files and let me know:
1. Save to library (recommended)
2. Need revisions
3. Save but don't add to library"
```

