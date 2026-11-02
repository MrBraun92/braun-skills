# Fase 3: Montagem

> Extraído sem alteração de conteúdo do SKILL.md original (linhas 541-676).

### Phase 3: Assembly Phase

**Goal:** Fill approved template with best-matching content, with transparent scoring

**Inputs:**
- Approved template (from Phase 2)
- Resume library + discovered experiences (from Phase 0 + 2.5)
- Success profile (from Phase 1)

**Process:**

**3.1 For Each Template Slot:**

1. **Extract all candidate bullets from library**
   - All bullets from library database
   - All newly discovered experiences
   - Include source resume for each

2. **Score each candidate** (see matching-strategies.md)
   - Direct match (40%): Keywords, domain, technology, outcome
   - Transferable (30%): Same capability, different context
   - Adjacent (20%): Related tools, methods, problem space
   - Impact (10%): Achievement type alignment

   Overall = (Direct × 0.4) + (Transfer × 0.3) + (Adjacent × 0.2) + (Impact × 0.1)

3. **Rank candidates by score**
   - Sort high to low
   - Group by confidence band:
     * 90-100%: DIRECT
     * 75-89%: TRANSFERABLE
     * 60-74%: ADJACENT
     * <60%: WEAK/GAP

4. **Present top 3 matches with analysis:**
   ```
   TEMPLATE SLOT: {Role} - Bullet {N}
   SEEKING: {Requirement description}

   MATCHES:
   [DIRECT - 95%] "{bullet_text}"
     ✓ Direct: {what matches directly}
     ✓ Transferable: {what transfers}
     ✓ Metrics: {quantified impact}
     Source: {resume_name}

   [TRANSFERABLE - 78%] "{bullet_text}"
     ✓ Transferable: {what transfers}
     ✓ Adjacent: {what's adjacent}
     ⚠ Gap: {what's missing}
     Source: {resume_name}

   [ADJACENT - 62%] "{bullet_text}"
     ✓ Adjacent: {what's related}
     ⚠ Gap: {what's missing}
     Source: {resume_name}

   RECOMMENDATION: Use DIRECT match (95%)
   ALTERNATIVE: If avoiding repetition, use TRANSFERABLE (78%) with reframing
   ```

5. **Handle gaps (confidence <60%):**
   ```
   GAP IDENTIFIED: {Requirement}

   BEST AVAILABLE: {score}% - "{bullet_text}"

   REFRAME OPPORTUNITY: {If applicable}
   Original: "{text}"
   Reframed: "{adjusted_text}" (truthful because {reason})
   New confidence: {score}%

   OPTIONS:
   1. Use reframed version ({new_score}%)
   2. Acknowledge gap in cover letter
   3. Omit bullet slot (reduce allocation)
   4. Use best available with disclosure

   RECOMMENDATION: {Most appropriate option}
   ```

**3.2 Content Reframing:**

When good match (>60%) but terminology misaligned:

**Apply strategies from matching-strategies.md:**
- Keyword alignment (preserve meaning, adjust terms)
- Emphasis shift (same facts, different focus)
- Abstraction level (adjust technical specificity)
- Scale emphasis (highlight relevant aspects)

**Show before/after for transparency:**
```
REFRAMING APPLIED:
Bullet: {template_slot}

Original: "{original_bullet}"
Source: {resume_name}

Reframed: "{reframed_bullet}"
Changes: {what changed and why}
Truthfulness: {why this is accurate}
```

**Checkpoint:**
```
"I've matched content to your template. Here's the complete mapping:

COVERAGE SUMMARY:
- Direct matches: {N} bullets ({percentage}%)
- Transferable: {N} bullets ({percentage}%)
- Adjacent: {N} bullets ({percentage}%)
- Gaps: {N} ({percentage}%)

REFRAMINGS APPLIED: {N}
- {Example 1}
- {Example 2}

GAPS IDENTIFIED:
- {Gap 1}: {Recommendation}
- {Gap 2}: {Recommendation}

OVERALL JD COVERAGE: {percentage}%

Review the detailed mapping below. Any adjustments to:
- Match selections?
- Reframings?
- Gap handling?"

[Present full detailed mapping]

Wait for user approval before generation.
```

**Output:** Complete bullet-by-bullet mapping with confidence scores and reframings

