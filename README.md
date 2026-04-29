# Manus Skills Repository

**Owner:** Oliver ([@MrBraun92](https://github.com/MrBraun92))
**Última auditoria:** abril 2026
**Skills ativas:** 199 · **Arquivadas:** 9 (em [`archive/`](./archive))

Este repositório contém o stack pessoal de **Agent Skills** do Oliver — capacidades modulares carregadas no Manus, no Claude Code e no GPT. Cada skill vive em sua própria pasta com um `SKILL.md` no formato canônico (frontmatter YAML + corpo Markdown).

---

## Sobre esta auditoria

Em abril de 2026 o repo passou por uma revisão de 3 etapas:

1. **Phase 0 — Arquivamento amplo** (commit [`e1615f8`](https://github.com/MrBraun92/manus-skills/commit/e1615f8), 88 skills): proposta inicial baseada em perfil inferido. **Revertida** após o owner confirmar que usa o conteúdo do dia-a-dia.

2. **Phases 1-4 — Skills v2** (commit [`2e29711`](https://github.com/MrBraun92/manus-skills/commit/2e29711), 40 skills novas): adicionadas em 4 fases temáticas alinhadas ao perfil real:
   - **Fase 1 — Tese acadêmica** (12 skills, em inglês): tese 100% em inglês, padrão APA 7, na UiS/Noruega, ética via SIKT, tema em gestão / AI advisory / dynamic capabilities / service quality
   - **Fase 2 — EventPro / dev** (9 skills, em inglês técnico): SaaS BR em React 19 + tRPC + Drizzle/MySQL (TiDB) + AWS S3 + OpenAI
   - **Fase 3 — Produtividade** (7 skills, em PT-BR): solopreneur AI com workflow paralelo Claude/Manus/GPT
   - **Fase 4 — Trading com método** (12 skills, em PT-BR com disclaimer obrigatório): trader retail BR sofisticado

3. **Reverso cirúrgico** — escopo do `archive/` reduzido para **9 skills** (5 fusões duplicatas + 4 substituições estratégicas pelas v2). Tudo o que estava genuinamente em uso foi restaurado para a raiz. Detalhes em [`archive/README.md`](./archive/README.md).

---

## Como usar

- **Editar uma skill:** abra a pasta da skill e edite o `SKILL.md` direto no GitHub.
- **Re-importar para o Manus / Claude:** compartilhe a URL raw do `SKILL.md` ou o link do repositório com o agente.
- **Adicionar uma skill nova:** crie uma pasta nova com o nome da skill e adicione `SKILL.md` dentro, seguindo o formato canônico.
- **Reativar skill arquivada:** `git mv archive/<nome>/ ./<nome>/` e push.

---

## Skills v2 (novas — abril 2026)

### 🎓 Fase 1 — Tese (em inglês, padrão APA 7 + SIKT)

| Skill | Descrição |
|---|---|
| [citation-integrity-checker](./citation-integrity-checker/SKILL.md) | Anti-citação inventada/errada — verifica se cada citação realmente sustenta a frase |
| [claim-evidence-mapper](./claim-evidence-mapper/SKILL.md) | Mapeia cada argumento da tese a uma evidência (forte/médio/especulativo) |
| [systematic-literature-review](./systematic-literature-review/SKILL.md) | Revisão sistemática estilo PRISMA, output em APA 7 |
| [qualitative-coding-specialist](./qualitative-coding-specialist/SKILL.md) | Codificação qualitativa (open / axial / thematic) — substitui parcialmente NVivo |
| [theoretical-integration](./theoretical-integration/SKILL.md) | Força integração teórica real quando a literature review virou "lista de autores" |
| [academic-paper-reviewer](./academic-paper-reviewer/SKILL.md) | Revisa capítulos como parecerista de Tier-1 management journal |
| [devils-advocate-research](./devils-advocate-research/SKILL.md) | Ataca o próprio trabalho do ângulo contrário — antecipa banca de defesa |
| [scientific-schematics](./scientific-schematics/SKILL.md) | Gera diagramas científicos (PRISMA, conceptual model, framework) |
| [apa-style-enforcer](./apa-style-enforcer/SKILL.md) | Padrão APA 7 estrito: in-text, references, headings, tables, figures |
| [academic-tone-polisher](./academic-tone-polisher/SKILL.md) | Polimento de inglês acadêmico com hedging apropriado, sem mascarar uso de IA |
| [research-ethics-sikt-reviewer](./research-ethics-sikt-reviewer/SKILL.md) | Revisão ética conforme regras SIKT (Noruega) — não CEP brasileiro |
| [thesis-defense-slide-builder](./thesis-defense-slide-builder/SKILL.md) | Tese → apresentação de defesa (45-60min) com narrativa estruturada |

### 🛠️ Fase 2 — EventPro / dev (em inglês técnico)

| Skill | Descrição |
|---|---|
| [test-automator-playwright](./test-automator-playwright/SKILL.md) | E2E para EventPro com Playwright — login, BudgetTable DnD, payment flow, share modal |
| [verification-before-completion](./verification-before-completion/SKILL.md) | Gate operacional: agente NÃO pode declarar "pronto" antes de provar com evidência |
| [database-optimizer](./database-optimizer/SKILL.md) | TiDB-specific (online DDL, optimistic txn, EXPLAIN ANALYZE) — não MySQL genérico |
| [react-expert](./react-expert/SKILL.md) | React 19 + shadcn + Vite + Tailwind 4 — re-render reduction, Suspense, transitions |
| [refactoring-specialist](./refactoring-specialist/SKILL.md) | Refatorações em pequenos passos seguros — Dashboard.tsx (987 linhas), BudgetTable.tsx (1093) |
| [rag-architect](./rag-architect/SKILL.md) | RAG para EventPro AI Chat — chunking, embedding, retrieval, eval |
| [repomix-safe-mixer](./repomix-safe-mixer/SKILL.md) | Empacota repo para Claude/Manus/GPT sem vazar segredos |
| [error-detective](./error-detective/SKILL.md) | Root-cause em produção — cruza stacktrace, logs, git log, schema TiDB |
| [continue-work](./continue-work/SKILL.md) | Briefing "onde paramos" entre sessões Claude/Manus/GPT — multilingual triggers |

### ⚡ Fase 3 — Produtividade (em PT-BR)

| Skill | Descrição |
|---|---|
| [doc-to-markdown](./doc-to-markdown/SKILL.md) | PDF/DOCX/PPTX/HTML → Markdown limpo |
| [transcript-fixer](./transcript-fixer/SKILL.md) | Corrige transcrições automáticas (Teams/Tactiq/Otter) |
| [meeting-to-actions](./meeting-to-actions/SKILL.md) | Reunião → decisões + próximos passos com responsável e prazo |
| [decision-journal](./decision-journal/SKILL.md) | Registra decisões com hipótese e critério de sucesso para revisar depois |
| [weekly-review](./weekly-review/SKILL.md) | Revisão semanal estilo GTD |
| [voice-memo-to-doc](./voice-memo-to-doc/SKILL.md) | Áudio solto → documento estruturado |
| [cost-metering](./cost-metering/SKILL.md) | Monitora custo/tempo de workflows IA — Claude/OpenAI/Manus |

### 💰 Fase 4 — Trading com método (em PT-BR, disclaimer obrigatório)

| Skill | Descrição |
|---|---|
| [financial-compliance-guardrails](./financial-compliance-guardrails/SKILL.md) ⚠️ | Skill meta — força disclaimers em qualquer skill de trading. Pré-requisito |
| [trader-psychology-coach](./trader-psychology-coach/SKILL.md) | Identifica viés (FOMO, revenge trade, overconfidence) e sugere correção |
| [portfolio-risk-manager](./portfolio-risk-manager/SKILL.md) | Mede risco total: drawdown, exposição, correlação, VaR/CVaR |
| [trade-journal-postmortem](./trade-journal-postmortem/SKILL.md) | Registra cada trade e identifica padrões emocionais/estatísticos |
| [backtesting-engineer](./backtesting-engineer/SKILL.md) | Backtest honesto com custos + slippage + IR |
| [position-sizing-simulator](./position-sizing-simulator/SKILL.md) | Kelly fracionário, fixed fractional, vol-targeting — só simulação |
| [walk-forward-validator](./walk-forward-validator/SKILL.md) | Valida estratégia em janelas móveis — detecta overfitting |
| [macro-economic-analyst](./macro-economic-analyst/SKILL.md) | Lê dados macro (Fed, Selic, IPCA, payroll) e traduz em vento de fundo |
| [economic-calendar-prep](./economic-calendar-prep/SKILL.md) | Agenda macro da semana com sensibilidade do mercado por evento |
| [b3-ibov-analyst-br](./b3-ibov-analyst-br/SKILL.md) | Analista B3 — IBOV, BDR, leilões, Selic, fluxo gringo |
| [tax-aware-trade-accounting](./tax-aware-trade-accounting/SKILL.md) | IR sobre Day Trade (20%) e Swing (15%), DARF mensal — não substitui contador |
| [earnings-call-analyst](./earnings-call-analyst/SKILL.md) | Lê transcrição de teleconferência: tom, guidance, sinais de risco |

---

## Demais skills do repo (159 skills mantidas)

O repo preserva 159 skills além das 40 v2 acima. A grande maioria foi mantida porque o owner usa o conteúdo eventualmente — não cabe arquivar pelo critério "fora do perfil inferido". Skills marcadas com 🔁 duplicam plugin nativo do Claude Code (preservadas para autoria histórica e versão controlada).

Para a lista completa navegue pelos diretórios na raiz do repo. Categorias principais (com tamanho aproximado):

- **💼 Trading — stack pessoal BR (7):** `bbb-strategist`, `equity-fundamental-analyst`, `order-flow-microstructure`, `pine-script-quant`, `risk-regime-portfolio`, `technical-price-action`, `trading-thesis-orchestrator`
- **🎓 Acadêmico (3):** 🔁 `thesis-supervisor`, 🔁 `evidence-researcher`, 🔁 `interview-intelligence-analyst`
- **🛠️ Dev / arquitetura / qualidade (~30):** `code-architect`, `code-auditor`, `data-modeler`, `system-design`, `architecture`, `tech-debt`, `documentation`, `debug`, `domain-language-cartographer`, `implementation-engineer`, `requirements-analyst`, `prd-issue-writer`, `vertical-slice-planner`, `refactor-plan-writer`, `tdd-implementation-runner`, `bug-triage-tdd-planner`, `test-strategist`, `qa-executor`, `release-verifier`, `production-reviewer`, `performance-reviewer`, `security-reviewer`, `accessibility-auditor`, `coding-agent-safety-guardrails`, `repo-quality-setup`, `deploy-checklist`, `interface-designer`, `ux-writer`, `ux-copy`, `design-critique`, `design-handoff`, `design-system`
- **📊 Produto / negócio / marketing (~20):** `persona-analyst`, `product-strategist`, `product-brainstorming`, `pricing-strategist`, `packaging-reviewer`, `monetization-analyst`, `retention-lifecycle-strategist`, `customer-signal-synthesizer`, `analytics-reviewer`, `competitive-reviewer`, `competitive-brief`, `market-analyst`, `positioning-strategist`, `content-creation`, `draft-content`, `blog-writer`, `seo-audit`, `email-sequence`, `campaign-plan`, `performance-report`, `brand-review`
- **⚙️ Ops / processo / project (~15):** `audit-orchestrator`, `audit`, `delivery-coordinator`, `execution-planner`, `launch-coordinator`, `process-auditor`, `process-doc`, `process-optimization`, `workflow-designer`, `capacity-plan`, `change-request`, `risk-assessment`, `sprint-planning`, `roadmap-update`, `metrics-review`, `standup`, `task-management`, `status-report`, `stakeholder-update`, `meeting-briefing`, `compliance-tracking`, `compliance-check`
- **🛠️ Job-search / RenderCV / negócio especializado (~25):** clusters preservados a pedido do owner — usar quando o caso de uso aparecer
- **🧾 Jurídico / contábil (~15):** `triage-nda`, `review-contract`, `legal-response`, `legal-risk-assessment`, `signature-request`, `vendor-check`, `vendor-review`, `audit-support`, `sox-testing`, `journal-entry`, `journal-entry-prep`, `reconciliation`, `variance-analysis`, `financial-statements`, `close-management`, `brief`
- **🔧 DevOps / SRE / RevOps (~5):** `devops-sre-agent`, `secops-agent`, `incident-response`, `runbook`, `revops-agent`
- **📊 Data / analytics (8):** `analyze`, `build-dashboard`, `explore-data`, `validate-data`, `data-context-extractor`, `statistical-analysis`, `create-viz`, `write-query`
- **🔧 Meta-skills (6):** `skill-router`, `skill-creator`, `skill-auditor`, `skill-installer`, `internet-skill-finder`, `memory-management`
- **🛟 Utilitários e outros (~15):** `canva-mcp`, `similarweb-analytics`, `prompt-engineer`, `grammar-auditor`, `pdf-tools`, `excel-generator`, `gws-best-practices`, `flight-fare-hacker`, `travel-advisor`, `weather-api`, `video-generator`, `bgm-prompter`, `tiktok-specialist`, `start`, `update`, `init`, `github-gem-seeker`, `deep-module-architect`, `module-interface-designer`, `scoping-interview`

---

## Estrutura do repositório

```
manus-skills/
├── README.md                       ← este arquivo
├── IMPORTACAO_SKILLS_RESUMO.md     ← changelog estruturado
├── TRADING_STACK_OVERVIEW.md       ← visão do stack de trading
├── MEMO_TO_MANUS.md                ← orientação para o Manus sincronizar
├── archive/                        ← 9 skills arquivadas (escopo cirúrgico)
│   ├── README.md                   ← rationale do arquivamento
│   └── <skill-name>/
└── <skill-name>/                   ← 199 skills ativas
    └── SKILL.md
```

---

## Histórico de auditoria

- **abril 2026** — Auditoria em 3 etapas: Phase 0 amplo (88 arquivadas) → revertido após confirmação do owner → escopo cirúrgico final (9 arquivadas: 5 fusões + 4 substituições estratégicas) + 40 skills v2 adicionadas. Resultado: **199 ativas + 9 arquivadas**.
- **Antes** — repo cresceu organicamente com adições do Manus, Claude e GPT misturando skills nativas + customizadas + experimentais.

Para detalhes ver [`IMPORTACAO_SKILLS_RESUMO.md`](./IMPORTACAO_SKILLS_RESUMO.md) e [`archive/README.md`](./archive/README.md).
