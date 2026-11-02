---
name: resume-tailoring
description: Use when creating tailored resumes for job applications - researches company/role, creates optimized templates, conducts branching experience discovery to surface undocumented skills, and generates professional multi-format resumes from user's resume library while maintaining factual integrity
---

# Resume Tailoring Skill

## Overview

Generates high-quality, tailored resumes optimized for specific job descriptions while maintaining factual integrity. Builds resumes around the holistic person by surfacing undocumented experiences through conversational discovery.

**Core Principle:** Truth-preserving optimization - maximize fit while maintaining factual integrity. Never fabricate experience, but intelligently reframe and emphasize relevant aspects.

**Mission:** A person's ability to get a job should be based on their experiences and capabilities, not on their resume writing skills.

## When to Use

Use this skill when:
- User provides a job description and wants a tailored resume
- User has multiple existing resumes in markdown format
- User wants to optimize their application for a specific role/company
- User needs help surfacing and articulating undocumented experiences

**DO NOT use for:**
- Generic resume writing from scratch (user needs existing resume library)
- Cover letters (different skill)
- LinkedIn profile optimization (different skill)

## Quick Start

**Required from user:**
1. Job description (text or URL)
2. Resume library location (defaults to `resumes/` in current directory)

**Workflow:**
1. Build library from existing resumes
2. Research company/role
3. Create template (with user checkpoint)
4. Optional: Branching experience discovery
5. Match content with confidence scoring
6. Generate MD + DOCX + PDF + Report
7. User review → Optional library update

## Implementation

See supporting files:
- `research-prompts.md` - Structured prompts for company/role research
- `matching-strategies.md` - Content matching algorithms and scoring
- `branching-questions.md` - Experience discovery conversation patterns

## Workflow Details


## Fases (carregue só a que estiver em curso)

Para não gastar contexto, este arquivo traz só visão geral e quick start. Cada fase fica em seu próprio arquivo e deve ser lida **quando for executada**, na ordem 0 → 1 → 2 → (2.5) → 3 → 4 → 5.

| Quando | Leia |
|---|---|
| Usuário passou mais de uma vaga | [references/phase-multi-job-detection.md](references/phase-multi-job-detection.md) |
| Início de toda execução | [references/phase-0-library-init.md](references/phase-0-library-init.md) |
| Pesquisar vaga e empresa | [references/phase-1-research.md](references/phase-1-research.md) |
| Montar o template do currículo | [references/phase-2-template.md](references/phase-2-template.md) |
| Lacunas no material do candidato | [references/phase-2-5-experience-discovery.md](references/phase-2-5-experience-discovery.md) |
| Montar conteúdo a partir da biblioteca | [references/phase-3-assembly.md](references/phase-3-assembly.md) |
| Gerar os arquivos finais | [references/phase-4-generation.md](references/phase-4-generation.md) |
| Após aprovação, atualizar a biblioteca | [references/phase-5-library-update.md](references/phase-5-library-update.md) |
| Algo falhou ou entrada incomum | [references/error-handling.md](references/error-handling.md) |
| Precisa de exemplos | [references/usage-examples.md](references/usage-examples.md) |
| Validar a skill | [references/testing-guidelines.md](references/testing-guidelines.md) |
