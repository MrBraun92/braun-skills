---
name: research-ethics-sikt-reviewer
description: Reviews research ethics for a UiS (Norway) master's thesis under SIKT (Sikt - Kunnskapssektorens tjenesteleverandør, the Norwegian Agency for Shared Services in Education and Research). Covers informed consent, anonymization, data storage, cross-border data transfer, retention, and sensitive personal data classification under Norwegian and EU GDPR rules. NOT a Brazilian CEP review and NOT a generic IRB review — uses the actual SIKT framework. Use when the user says "ethics review", "SIKT", "consent form", "is this GDPR-safe", "anonymize my data", "ethics application", or before submitting an ethics notification. Built for a UiS Management master's thesis (English, APA 7).
---

# Research Ethics — SIKT Reviewer

Reviews research ethics for a UiS master's thesis under the **SIKT** framework (Norway's data protection service for the education and research sector, formerly NSD), aligned with EU GDPR. Critically: this is NOT the Brazilian CEP/CONEP system, NOT a US IRB, NOT a generic Helsinki Declaration review. The procedural rules and risk thresholds are different. This skill applies the actual rules a UiS supervisor and SIKT case officer will apply.

## When to use this skill
- Submitting a SIKT notification before data collection begins.
- Drafting or reviewing an informed consent form.
- A consent form was reused from a prior project and needs a rules check.
- Determining whether the project requires SIKT notification at all.
- Handling sensitive personal data (health, ethnicity, religion, sexual orientation, criminal records, etc.).
- Cross-border transfer concerns (interviewing participants in non-EU countries).
- Anonymization plan review — is it real anonymization or only pseudonymization?
- Retention period decisions and data destruction plans.

## Methodology

### Step 1: Determine if SIKT notification is required
A project triggers SIKT notification when it processes **personal data**. Personal data = any data that can identify a natural person directly or indirectly. Audio recordings, video recordings, IP addresses, names, employer + role combinations that uniquely identify someone — all personal data.

- If data is fully anonymous from collection (e.g., aggregate-only survey, no identifying metadata) — SIKT notification not required, but state the basis explicitly.
- If any phase includes personal data — notification required, even if the final dataset will be anonymized.
- If sensitive personal data (Article 9 GDPR special categories) is involved — extra requirements apply.

State the determination clearly with reasoning.

### Step 2: Validate the legal basis
SIKT requires a legal basis under GDPR Article 6 (and Article 9 for special categories). For research:
- **Article 6(1)(a) consent** — most common for master's theses. Voluntary, specific, informed, unambiguous.
- **Article 6(1)(e) public interest task** — sometimes used by institutional researchers; usually not for student theses.
- **Article 9(2)(a) explicit consent** — required for sensitive categories.
- **Article 9(2)(j) research exemption** — possible but requires institutional safeguards beyond a master's thesis scope.

For a UiS master's thesis: default to consent (Art. 6(1)(a)) and explicit consent (Art. 9(2)(a)) if sensitive data is involved.

### Step 3: Review the consent form
Required elements (SIKT consent template anchors these):

- **Project title and purpose** in plain English (not academic jargon).
- **What participation involves** — interview length, recording format, topics covered.
- **Voluntariness statement** — participation is voluntary, withdrawal possible at any time without consequences.
- **Right to withdraw consent** — including withdrawal of data already collected, up to a stated deadline.
- **Data controller** — usually the university (UiS).
- **Researcher identification** — name + contact + supervisor name + supervisor contact.
- **Data Protection Officer (DPO) contact** — UiS DPO email.
- **SIKT contact** — for complaints regarding data protection.
- **Storage** — where data is stored (UiS-managed cloud, encrypted local, etc.). NOT Google Drive personal account.
- **Who has access** — researcher, supervisor, possibly external transcription service (then DPA required).
- **Sharing** — whether data will be shared with third parties.
- **Anonymization plan** — when and how raw data becomes anonymous.
- **Retention** — how long data is kept and when it's deleted.
- **Rights** — access, rectification, erasure, restriction, objection, portability, complaint to Datatilsynet.
- **Signature block** — name + signature + date.

Flag any missing element.

### Step 4: Assess sensitive personal data classification
Article 9 special categories: racial/ethnic origin, political opinions, religious beliefs, trade-union membership, genetic data, biometric data, health data, sexual orientation, criminal convictions.

For a Management thesis on AI advisory / dynamic capabilities / service quality, sensitive data is **usually not** processed — but watch for:
- Interviews discussing health-services firms (health data risk).
- Participants disclosing union membership in HR-context interviews.
- Demographic surveys including ethnicity, religion, etc.
- Criminal-record discussions in compliance / fraud research.

If sensitive data is involved: additional requirements (explicit consent, heightened security, possible DPIA).

### Step 5: Anonymization vs pseudonymization
- **Pseudonymization** — names replaced with codes (P01, P02), but a key linking codes to identities exists. Still personal data. Must be protected.
- **Anonymization** — no key, no possibility of re-identification by anyone, even the researcher. Truly anonymous = no longer personal data.

The anonymization plan must specify: when the key is destroyed (often: at thesis submission or earlier), what additional fields are removed (employer name, exact role + city combinations, identifying anecdotes), and that the final dataset is genuinely non-re-identifiable.

For a small qualitative sample (8-15 interviews), perfect anonymization is hard — flag this realism. Note in the consent form that "anonymization protects against casual identification but not against someone who already knows the participant".

### Step 6: Storage and transfer
- Recordings, transcripts, consent forms must be stored on UiS-managed infrastructure (UiS OneDrive / SharePoint inside the institutional tenant; UiS-encrypted laptop). NOT personal Dropbox / personal Google Drive / personal iCloud.
- Cloud transcription services (Otter.ai, Trint, etc.) are processors — require a Data Processing Agreement (DPA). Many free services do NOT meet GDPR. Default position: do not use them for raw recordings.
- LLM use (ChatGPT, Claude, Gemini) on raw transcripts — same principle. Either fully anonymize first OR use an enterprise tool with DPA. The consent form must disclose AI processing if it occurs.
- Cross-border transfer: if any participant is outside EU/EEA, GDPR Chapter V rules apply (adequacy decision, SCCs, etc.). Flag.

### Step 7: Retention and destruction
- Retention period stated explicitly: "Data will be retained until [date] and destroyed after."
- Default for a master's thesis: data destroyed at thesis submission, OR 6-12 months after for follow-up clarifications, max ~3 years if SIKT-approved.
- Destruction plan: secure deletion of files, shredding of any paper, breaking of the pseudonymization key.

### Step 8: Produce the audit
Output a SIKT-style checklist with PASS / FAIL / NEEDS-WORK per item, plus a corrected consent form draft if requested.

## Output format

```
## SIKT / Research Ethics Audit — <project title>

### 1. Notification determination
Required: <Yes / No>. Reasoning: ...

### 2. Legal basis
Article: <6(1)(a) / 6(1)(e) / 9(2)(a) / 9(2)(j) / N/A>
Justification: ...

### 3. Sensitive data assessment
Special categories involved: <Yes / No>. If yes, which: ...

### 4. Consent form review
| Required element | Present? | Notes |
|---|---|---|

### 5. Anonymization plan
- Pseudonymization at: ...
- Key destruction at: ...
- Fields removed beyond names: ...
- Realism note: ...

### 6. Storage and transfer
| Aspect | Compliant? | Action needed |
|---|---|---|

### 7. Retention and destruction
Retention period: ...
Destruction plan: ...

### 8. Outstanding issues (must fix BEFORE data collection)
1. ...
2. ...

### 9. Corrected consent form draft (if requested)
<full English consent form following SIKT template>
```

## Quality checklist
- [ ] Notification determination is justified, not just stated.
- [ ] Legal basis is named with the specific GDPR article.
- [ ] Sensitive data assessment is explicit (Yes / No with reasoning).
- [ ] Consent form check covered every required element.
- [ ] Anonymization plan distinguishes pseudonymization from true anonymization.
- [ ] Storage location is UiS-managed; if not, the gap is flagged.
- [ ] Cloud processor (transcription, LLM) use is reviewed against DPA requirements.
- [ ] Retention period and destruction plan are concrete (dates / events).

## Notes for the assistant
- This is **SIKT / GDPR / Norwegian-and-EU** law. Do NOT import Brazilian CEP procedures, US IRB language, or generic "Helsinki Declaration" framing — the user is at UiS, the rules are different.
- Notification ≠ approval. SIKT primarily reviews data protection, not ethical permissibility per se. Some studies need both SIKT notification AND a separate research-ethics assessment by the UiS faculty / NESH (Norwegian Research Ethics Committees) for sensitive content. Flag the latter when relevant.
- For thesis projects, SIKT processing time is roughly 2-4 weeks. Build that into the project timeline — submit BEFORE the planned data collection start, not the day before.
- Be especially careful with **employer-disclosure risk**: even with pseudonymized name, "the head of digital transformation at a Norwegian regional bank" may be uniquely identifying. Anonymization plans must address this.
- LLM use on personal data is a fast-evolving area — current default position: anonymize first, then send to LLM. Disclose LLM use in methods chapter regardless.
- If the user has already collected data without SIKT notification and the data is personal, this is a serious problem. Recommend immediate consultation with the UiS DPO; do not normalize the lapse.
- This skill is not a replacement for the actual SIKT submission. It's the rehearsal that catches issues before submission.
- Consent forms should be in the participant's language. If interviews are in Norwegian or Portuguese, the consent form must be in that language — translate, don't force English.
