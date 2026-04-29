# Manus Skills Repository

**Owner:** Oliver ([@MrBraun92](https://github.com/MrBraun92))
**Última auditoria:** abril 2026
**Skills ativas:** 120 · **Arquivadas:** 88 (em [`archive/`](./archive))

Este repositório contém o stack pessoal de **Agent Skills** do Oliver — capacidades modulares carregadas no Manus, no Claude Code e no GPT. Cada skill vive em sua própria pasta com um `SKILL.md` no formato canônico (frontmatter YAML + corpo Markdown).

---

## Sobre esta auditoria

Em abril de 2026 o repo passou por uma revisão completa em duas fases:

1. **Phase 0 — Arquivamento** (commit [`e1615f8`](https://github.com/MrBraun92/manus-skills/commit/e1615f8)): 88 skills movidas para `archive/` por estarem fora do perfil real do owner (job-search, RenderCV, jurídico enterprise, contabilidade SOX, devops enterprise) ou por serem duplicatas literais. Rationale completo em [`archive/README.md`](./archive/README.md).

2. **Phases 1-4 — Skills v2**: 40 skills novas adicionadas, distribuídas em 4 fases temáticas alinhadas ao perfil real:
   - **Fase 1 — Tese acadêmica** (12 skills, em inglês): tese 100% em inglês, padrão APA 7, na UiS/Noruega, ética via SIKT, tema em gestão / AI advisory / dynamic capabilities / service quality
   - **Fase 2 — EventPro / dev** (9 skills, em inglês técnico): SaaS BR em React 19 + tRPC + Drizzle/MySQL (TiDB) + AWS S3 + OpenAI
   - **Fase 3 — Produtividade** (7 skills, em PT-BR): solopreneur AI com workflow paralelo Claude/Manus/GPT
   - **Fase 4 — Trading com método** (12 skills, em PT-BR com disclaimer obrigatório): trader retail BR sofisticado

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

## Skills core preservadas (80 skills)

Skills marcadas com 🔁 duplicam plugin nativo do Claude Code (preservadas no repo a pedido do owner para autoria histórica).

### 💼 Trading — stack pessoal BR (7 skills)

| Skill | Descrição |
|---|---|
| [bbb-strategist](./bbb-strategist/SKILL.md) | Estrategista de Big Brother Brasil |
| [equity-fundamental-analyst](./equity-fundamental-analyst/SKILL.md) | Análise fundamentalista de ações |
| [order-flow-microstructure](./order-flow-microstructure/SKILL.md) | Fluxo, VWAP, microestrutura |
| [pine-script-quant](./pine-script-quant/SKILL.md) | Pine Script para TradingView — quant strategies |
| [risk-regime-portfolio](./risk-regime-portfolio/SKILL.md) | Risco e regime de mercado |
| [technical-price-action](./technical-price-action/SKILL.md) | Análise técnica e price action |
| [trading-thesis-orchestrator](./trading-thesis-orchestrator/SKILL.md) | Orquestra teses de trading |

### 🎓 Acadêmico — base preservada (3 skills)

| Skill | Descrição |
|---|---|
| 🔁 [thesis-supervisor](./thesis-supervisor/SKILL.md) | Supervisão de tese (orientação geral) |
| 🔁 [evidence-researcher](./evidence-researcher/SKILL.md) | Busca peer-reviewed e síntese geral |
| 🔁 [interview-intelligence-analyst](./interview-intelligence-analyst/SKILL.md) | Análise de transcrições |

### 🛠️ EventPro / dev (~28 skills)

Code & arquitetura: 🔁 `code-architect`, 🔁 `code-auditor`, 🔁 `data-modeler`, `system-design`, `architecture`, `code-review`, `tech-debt`, 🔁 `documentation`, 🔁 `debug`, `domain-language-cartographer`

Implementação: 🔁 `implementation-engineer`, 🔁 `requirements-analyst`, `prd-issue-writer`, `vertical-slice-planner`, `refactor-plan-writer`, `tdd-implementation-runner`, `bug-triage-tdd-planner`

Qualidade & segurança: 🔁 `test-strategist`, 🔁 `qa-executor`, 🔁 `release-verifier`, 🔁 `production-reviewer`, 🔁 `performance-reviewer`, 🔁 `security-reviewer`, 🔁 `accessibility-auditor`, `coding-agent-safety-guardrails`, `repo-quality-setup`, `deploy-checklist`

Design: 🔁 `interface-designer`, 🔁 `ux-writer`, `ux-copy`

### 📊 Produto / negócio / marketing (14 skills)

🔁 `persona-analyst`, 🔁 `product-strategist`, `product-brainstorming`, 🔁 `pricing-strategist`, 🔁 `packaging-reviewer`, 🔁 `monetization-analyst`, 🔁 `retention-lifecycle-strategist`, 🔁 `customer-signal-synthesizer`, 🔁 `analytics-reviewer`, 🔁 `competitive-reviewer`, 🔁 `market-analyst`, 🔁 `positioning-strategist`, `content-creation`, `draft-content`

### ⚙️ Ops / processo (6 skills)

🔁 `audit-orchestrator`, 🔁 `delivery-coordinator`, 🔁 `execution-planner`, 🔁 `launch-coordinator`, 🔁 `process-auditor`, 🔁 `workflow-designer`

### 📊 Data / analytics (8 skills)

`analyze`, `build-dashboard`, `explore-data`, `validate-data`, `data-context-extractor`, `statistical-analysis`, `create-viz`, `write-query`

### 🔧 Meta-skills (6 skills)

🔁 `skill-router`, 🔁 `skill-creator`, 🔁 `skill-auditor`, `skill-installer`, `internet-skill-finder`, 🔁 `memory-management`

### 🛟 Outros úteis (4 skills)

`canva-mcp`, `similarweb-analytics`, 🔁 `prompt-engineer`, 🔁 `grammar-auditor`

---

## Estrutura do repositório

```
manus-skills/
├── README.md                       ← este arquivo
├── IMPORTACAO_SKILLS_RESUMO.md     ← changelog estruturado
├── TRADING_STACK_OVERVIEW.md       ← visão do stack de trading
├── archive/                        ← 88 skills arquivadas (Phase 0)
│   ├── README.md                   ← rationale completo do arquivamento
│   └── <skill-name>/
└── <skill-name>/                   ← 120 skills ativas
    └── SKILL.md
```

---

## Histórico de auditoria

- **abril 2026** — Auditoria completa (Phase 0 + Phases 1-4): 168 → 120 ativas; 40 skills v2 adicionadas; 88 arquivadas
- **Antes** — repo cresceu organicamente com adições do Manus, Claude e GPT misturando skills nativas + customizadas + experimentais

Para detalhes ver [`IMPORTACAO_SKILLS_RESUMO.md`](./IMPORTACAO_SKILLS_RESUMO.md) e [`archive/README.md`](./archive/README.md).
