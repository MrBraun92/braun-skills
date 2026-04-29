# Histórico técnico de importação e auditoria

## Estado atual (abril 2026)

| Métrica | Valor |
|---|---:|
| Skills ativas no repositório | **120** |
| Skills arquivadas em `archive/` | **88** |
| Skills v2 adicionadas (Phases 1-4) | **40** |
| Repositório | `MrBraun92/manus-skills` |
| Branch principal | `master` |
| Último commit de auditoria | `e1615f8` (Phase 0) |

---

## Histórico de operações

### abril 2026 — Auditoria completa (Oliver + Claude Opus 4.7)

**Phase 0** — arquivamento de 88 skills fora do perfil ou duplicatas:

- Cluster job-search (14): ai-job-scout, career-strategist, company-discovery, corpus-review, cover-letter, hidden-job-hunter, industry-research, job-coach, job-scan, job-scout, linkedin-algorithm-expert, linkedin-review, resume-tailoring, scoping-interview
- Cluster RenderCV (6): rendercv-development-context, rendercv-testing-context, review-rendercv-pr, solve-rendercv-issue, triage-rendercv-issue, publish-rendercv-typst-package
- Cluster legal enterprise (8 + 1): triage-nda, review-contract, legal-response, legal-risk-assessment, signature-request, vendor-check, vendor-review, meeting-briefing, brief
- Cluster SOX/contábil (8): audit-support, sox-testing, journal-entry, journal-entry-prep, reconciliation, variance-analysis, financial-statements, close-management
- Cluster devops enterprise (5): devops-sre-agent, secops-agent, incident-response, runbook, revops-agent
- Fusões duplicatas literais (4): accessibility-review, sql-queries, data-visualization, testing-strategy
- Outras fora-do-perfil (~33): flight-fare-hacker, travel-advisor, weather-api, video-generator, bgm-prompter, tiktok-specialist, blog-writer, seo-audit, email-sequence, campaign-plan, performance-report, brand-review, competitive-brief, capacity-plan, compliance-tracking, compliance-check, change-request, risk-assessment, sprint-planning, roadmap-update, metrics-review, standup, task-management, status-report, stakeholder-update, start, update, init, audit, github-gem-seeker, pdf-tools, excel-generator, gws-best-practices, deep-module-architect, module-interface-designer, process-doc, process-optimization
- Substituições estratégicas (4): research-synthesis → sub. por systematic-literature-review + citation-integrity-checker + claim-evidence-mapper; user-research → sub. por qualitative-coding-specialist; synthesize-research → sub. por systematic-literature-review; stock-analysis → sub. por b3-ibov-analyst-br

Rationale completo em [`archive/README.md`](./archive/README.md).

**Phases 1-4** — adição de 40 Skills v2:

| Fase | Tema | Idioma | Quantidade |
|---|---|---|---:|
| 1 | Tese acadêmica (APA 7 + SIKT) | English | 12 |
| 2 | EventPro / dev | English técnico | 9 |
| 3 | Produtividade (workflow Manus/Claude/GPT) | PT-BR | 7 |
| 4 | Trading com método (disclaimer obrigatório) | PT-BR | 12 |

Detalhes de cada skill em `README.md`.

---

## Decisões de design

### Skills nativas duplicadas — preservadas a pedido do owner
Skills que duplicam plugins nativos do Claude Code (`anthropic-skills:*`, `productivity:*`, `product-management:*`) **foram preservadas no repo** mesmo com sobreposição funcional. O owner mantém para autoria histórica e versão controlada, mesmo que o plugin nativo cubra a mesma funcionalidade.

### Idioma por bloco
- **Tese (Fase 1):** English — output da skill será em inglês porque a tese é em inglês.
- **Dev (Fase 2):** English técnico — convenção universal de skills de engenharia.
- **Produtividade (Fase 3):** PT-BR — uso pessoal, contexto BR.
- **Trading (Fase 4):** PT-BR — trader BR, contexto B3/CVM/IR-BR.

### Disclaimer travado em skills de trading
Toda skill da Fase 4 inclui blockquote `> ⚠️ Disclaimer:` no INÍCIO e no FIM do `SKILL.md`. Vocabulário banido do corpo: "compre", "venda", "garantido", "certo", "recomendo", "dica", "lucro garantido". A meta-skill `financial-compliance-guardrails` é a guardiã desse contrato.

---

## Histórico anterior (pré-auditoria)

### Importação inicial (data desconhecida)

Sincronização original do conjunto de skills do sistema, incluindo:
- Skills nativas do Claude (73 extraídas de `Claude_Native_Skills.rtf`)
- Pacotes `.skill` enviados pelo usuário ao Manus (skill-router, devops-sre-agent, revops-agent, secops-agent, interview-intelligence-analyst, positioning-strategist, retention-lifecycle-strategist, customer-signal-synthesizer, qa-executor)
- Correção manual de frontmatter incompatível (`data-context-extractor`)

Estado intermediário: 145 skills válidas, depois cresceu organicamente para 168 antes da auditoria de abril 2026.

---

## Como reagir a futuras auditorias

1. Antes de adicionar uma skill nova, conferir se já existe equivalente nativa em `anthropic-skills:*`, `productivity:*`, `product-management:*` ou outro plugin. Se sim — ou usa a nativa, ou justifica a duplicação.
2. Skill de trading sempre passa por `financial-compliance-guardrails` (disclaimer obrigatório no início e fim).
3. Skill que produz output em inglês → SKILL.md em inglês. Skill que produz output em PT-BR → SKILL.md em PT-BR.
4. Description em frontmatter deve incluir palavras-chave de uso (verbos de ação, sinônimos, gatilhos multilíngues quando relevante) para o `skill-router` triggar corretamente.
5. Ao arquivar, sempre `git mv archive/<nome>/` (preserva histórico) — nunca `rm -rf`.
