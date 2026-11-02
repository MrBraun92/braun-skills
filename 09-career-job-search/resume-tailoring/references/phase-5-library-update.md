# Fase 5: Atualização da biblioteca (condicional)

> Extraído sem alteração de conteúdo do SKILL.md original (linhas 866-996).

### Phase 5: Library Update (CONDITIONAL)

**Goal:** Optionally add successful resume to library for future use

**When:** After user reviews and approves generated resume

**Checkpoint Question:**
```
"Are you satisfied with this resume?

OPTIONS:
1. YES - Save to library
   → Adds resume to permanent location
   → Rebuilds library database
   → Makes new content available for future resumes

2. NO - Need revisions
   → What would you like to adjust?
   → Make changes and re-present

3. SAVE BUT DON'T ADD TO LIBRARY
   → Keep files in current location
   → Don't enrich database
   → Useful for experimental resumes

Which option?"
```

**If Option 1 (YES - Save to library):**

**Process:**

1. **Move resume to library:**
   ```
   Source: {current_directory}/{Name}_{Company}_{Role}_Resume.md
   Destination: {resume_library}/{Name}_{Company}_{Role}_Resume.md

   Also move:
   - .docx file
   - .pdf file (if exists)
   - _Report.md file
   ```

2. **Rebuild library database:**
   ```
   Re-run Phase 0 library initialization
   Parse newly created resume
   Add bullets to experience database
   Update keyword/theme indices
   Tag with metadata:
     - target_company: {Company}
     - target_role: {Role}
     - generated_date: {timestamp}
     - jd_coverage: {percentage}
     - success_profile: {reference to profile}
   ```

3. **Preserve generation metadata:**
   ```json
   {
     "resume_id": "{Name}_{Company}_{Role}",
     "generated": "{timestamp}",
     "source_resumes": ["{resume1}", "{resume2}"],
     "reframings": [
       {
         "original": "{text}",
         "reframed": "{text}",
         "reason": "{why}"
       }
     ],
     "match_scores": {
       "bullet_1": 95,
       "bullet_2": 87,
       ...
     },
     "newly_discovered": [
       {
         "experience": "{description}",
         "bullet": "{text}",
         "addresses_gap": "{gap}"
       }
     ]
   }
   ```

4. **Announce completion:**
   ```
   "Resume saved to library!

   Library updated:
   - Total resumes: {N}
   - New content variations: {N}
   - Newly discovered experiences added: {N}

   This resume and its new content are now available for future tailoring sessions."
   ```

**If Option 2 (NO - Need revisions):**

```
"What would you like to adjust?"

[Collect user feedback]
[Make requested changes]
[Re-run relevant phases]
[Re-present for approval]

[Repeat until satisfied or user cancels]
```

**If Option 3 (SAVE BUT DON'T ADD TO LIBRARY):**

```
"Resume files saved to current directory:
- {Name}_{Company}_{Role}_Resume.md
- {Name}_{Company}_{Role}_Resume.docx
- {Name}_{Company}_{Role}_Resume_Report.md

Not added to library - you can manually move later if desired."
```

**Benefits of Library Update:**
- Grows library with each successful resume
- New bullet variations become available
- Reframings that work can be reused
- Discovered experiences permanently captured
- Future sessions start with richer library
- Self-improving system over time

**Output:** Updated library database + metadata preservation (if Option 1)

