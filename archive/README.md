# archive/ — Skills arquivadas (Fase 0 + 0.5)

Esta pasta contém skills que foram desativadas do auto-loading do Claude Code mas **preservadas para histórico**. Cada uma foi removida da pasta raiz por uma razão documentada abaixo.

**Quando consultar este arquivo:** se você quiser entender por que uma skill saiu do uso ativo, ou recuperar uma skill arquivada (basta mover de volta para a raiz).

**Como reativar uma skill:** `git mv archive/<skill-name>/ ./<skill-name>/` e dar push.

---

## Princípio editorial da auditoria

Esta auditoria foi conduzida em **abril de 2026** com 4 critérios:

1. **Fora do perfil real do usuário (Oliver):** skills que cobrem casos de uso que não existem no dia-a-dia dele (busca de emprego, RenderCV, jurídico enterprise, contabilidade SOX, devops enterprise).
2. **Duplicatas literais:** skills com escopo idêntico onde manter as duas só polui o roteamento.
3. **Sobreposição forte com plugin nativo do Claude Code:** algumas skills foram preservadas no repo a pedido do owner mesmo duplicando plugin nativo (preservar autoria histórica), mas as duplicatas literais entre skills do próprio repo foram fundidas.
4. **Skills substituídas por v2 mais especializadas:** quando a Fase 1-4 trouxe uma skill mais focada para o stack real (EventPro / tese APA / trading BR), a versão genérica anterior foi arquivada.

O perfil considerado foi:

- **Solopreneur AI** com foco em construção de SaaS BR (`EventPro`)
- **Mestrando** com tese em **inglês**, padrão **APA 7**, na **UiS (Noruega)**, ética via **SIKT**, tema em gestão / AI advisory / dynamic capabilities / service quality
- **Trader retail BR** sofisticado com stack já madura (Pine Script, price action, fundamentalista, microestrutura)
- **Não-desenvolvedor profissional** — interessa o que vira artefato, não abstrações enterprise

---

## Skills arquivadas — agrupadas por cluster

### Cluster 1 — Job-search (14 skills)

Solopreneur autônomo não busca emprego. Mantido o cluster apenas para histórico.

| Skill | Razão |
|---|---|
| `ai-job-scout` | Job-search |
| `career-strategist` | Job-search |
| `company-discovery` | Job-search |
| `corpus-review` | Job-search |
| `cover-letter` | Job-search |
| `hidden-job-hunter` | Job-search |
| `industry-research` | Escopo job-search (research de mercado de empregos) |
| `job-coach` | Job-search |
| `job-scan` | Job-search |
| `job-scout` | Job-search |
| `linkedin-algorithm-expert` | Marketing pessoal — fora do foco |
| `linkedin-review` | Marketing pessoal — fora do foco |
| `resume-tailoring` | Job-search |
| `scoping-interview` | Job-search |

### Cluster 2 — RenderCV (6 skills)

CLI específico (RenderCV / Typst) que o usuário não mantém.

| Skill | Razão |
|---|---|
| `rendercv-development-context` | RenderCV não é projeto ativo |
| `rendercv-testing-context` | RenderCV não é projeto ativo |
| `review-rendercv-pr` | RenderCV não é projeto ativo |
| `solve-rendercv-issue` | RenderCV não é projeto ativo |
| `triage-rendercv-issue` | RenderCV não é projeto ativo |
| `publish-rendercv-typst-package` | RenderCV não é projeto ativo |

### Cluster 3 — Legal enterprise (8 skills)

Sem volume jurídico real no dia-a-dia.

| Skill | Razão |
|---|---|
| `triage-nda` | Sem fluxo de NDA |
| `review-contract` | Sem volume contratual |
| `legal-response` | Sem demanda jurídica recorrente |
| `legal-risk-assessment` | Sem demanda jurídica recorrente |
| `signature-request` | Sem fluxo de assinatura formal |
| `vendor-check` | Procurement enterprise |
| `vendor-review` | Procurement enterprise |
| `meeting-briefing` | Específico de meetings jurídicos |
| `brief` | Específico jurídico (briefing legal) |

### Cluster 4 — Contabilidade / SOX (8 skills)

Contabilidade enterprise / SOX 404 não se aplica a SaaS BR solopreneur nem a tese de mestrado.

| Skill | Razão |
|---|---|
| `audit-support` | SOX enterprise |
| `sox-testing` | SOX enterprise |
| `journal-entry` | Contabilidade enterprise |
| `journal-entry-prep` | Duplicata de journal-entry |
| `reconciliation` | Contabilidade enterprise |
| `variance-analysis` | CFO enterprise |
| `financial-statements` | Contabilidade enterprise |
| `close-management` | Close mensal enterprise |

### Cluster 5 — DevOps enterprise (5 skills)

EventPro é stack simples (Vite + tRPC + TiDB Cloud + S3). DevOps enterprise é overkill por enquanto.

| Skill | Razão |
|---|---|
| `devops-sre-agent` | Overkill para SaaS solo |
| `secops-agent` | Overkill para SaaS solo |
| `incident-response` | Overkill para SaaS solo |
| `runbook` | Overkill para ops solo |
| `revops-agent` | Enterprise RevOps |

---

## Fusões — duplicatas literais (4 skills)

Mantida a versão mais limpa, arquivada a duplicata.

| Skill arquivada | Mantida | Razão |
|---|---|---|
| `accessibility-review` | `accessibility-auditor` | Mesmo escopo (WCAG audit) |
| `sql-queries` | `write-query` | Duplicata literal de SQL writing |
| `data-visualization` | `create-viz` | Duplicata literal de visualization |
| `testing-strategy` | `test-strategist` | Duplicata semântica |

---

## Outros arquivamentos por fora-do-perfil (29 skills)

| Skill | Razão |
|---|---|
| `flight-fare-hacker` | Utilidade marginal |
| `travel-advisor` | Utilidade marginal |
| `weather-api` | Trivial demais para virar skill |
| `video-generator` | Fora do perfil atual |
| `bgm-prompter` | Música/BGM — utilidade marginal |
| `tiktok-specialist` | Sem evidência de uso |
| `blog-writer` | Sobreposição com `content-creation` |
| `seo-audit` | EventPro é SaaS B2B BR — SEO é marginal |
| `email-sequence` | Marketing avançado — não é foco |
| `campaign-plan` | Marketing avançado — fora foco solopreneur |
| `performance-report` | Escopo agência marketing |
| `brand-review` | Sem brand voice formal documentada |
| `competitive-brief` | Sobreposição com `competitive-reviewer` |
| `capacity-plan` | Headcount enterprise |
| `compliance-tracking` | SOC2 / ISO enterprise |
| `compliance-check` | Sobreposição com `compliance-tracking` |
| `change-request` | Escopo CAB enterprise |
| `risk-assessment` | Risk register enterprise |
| `sprint-planning` | Solo dev sem sprint formal |
| `roadmap-update` | Solopreneur sem roadmap formal |
| `metrics-review` | Metric review enterprise |
| `standup` | Solo — sem standup |
| `task-management` | Conflito com CLAUDE.md / memória ativa |
| `status-report` | Cadência corporate, não pessoal |
| `stakeholder-update` | Cadência corporate |
| `start` | Comando produtividade interno |
| `update` | Comando produtividade interno |
| `init` | Comando produtividade interno |
| `audit` | Comando genérico — substituído por `audit-orchestrator` |
| `github-gem-seeker` | Sobreposição com `internet-skill-finder` |
| `pdf-tools` | MCPs de PDF já instalados |
| `excel-generator` | Skill nativa `xlsx` cobre o caso |
| `gws-best-practices` | Só faria sentido com Workspace ativo |
| `deep-module-architect` | Sobreposição com `code-architect` |
| `module-interface-designer` | Sobreposição com `code-architect` |
| `process-doc` | Process enterprise |
| `process-optimization` | Process enterprise |
| `process-auditor` | Process enterprise |

---

## Substituições estratégicas (4 skills)

Estas saíram para dar lugar a v2 mais focadas no stack real do Oliver. A substituta vive na raiz do repo.

| Skill arquivada | Substituída por | Razão |
|---|---|---|
| `research-synthesis` | `systematic-literature-review` + `citation-integrity-checker` + `claim-evidence-mapper` | Tese exige rigor APA + integridade de citação explícita |
| `user-research` | `qualitative-coding-specialist` | Tese qualitativa precisa de coding formal (aberta/axial/temática) |
| `synthesize-research` | `systematic-literature-review` | Substituído por método PRISMA-friendly |
| `stock-analysis` | `b3-ibov-analyst-br` | Foco BR (B3, IBOV, BDR, FII) > genérico US |

---

## O que NÃO foi arquivado (preservado mesmo duplicando plugin nativo)

A pedido do owner, **skills que duplicam plugins nativos** do Claude Code (`anthropic-skills:*`, `productivity:*`, `product-management:*`, etc.) **foram preservadas na raiz do repo** mesmo com sobreposição funcional. Razão: o owner copiou esses arquivos para o próprio repo no passado para preservar autoria histórica e versão controlada, e pretende mantê-los assim.

Lista de duplicatas preservadas (informativo apenas):

- `code-architect`, `code-auditor`, `security-reviewer`, `performance-reviewer`, `data-modeler`, `implementation-engineer`, `test-strategist`, `qa-executor`, `release-verifier`, `production-reviewer`, `requirements-analyst`
- `thesis-supervisor`, `evidence-researcher`, `interview-intelligence-analyst`
- `persona-analyst`, `product-strategist`, `pricing-strategist`, `packaging-reviewer`, `monetization-analyst`, `retention-lifecycle-strategist`, `customer-signal-synthesizer`
- `audit-orchestrator`, `skill-router`, `skill-creator`, `skill-auditor`
- `memory-management`, `product-brainstorming`

Estas serão consideradas para arquivamento numa próxima auditoria, se o owner mudar de opinião sobre preservar duplicatas.
