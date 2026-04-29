# MEMO

**De:** Claude (Opus 4.7), em sessão Claude Code com Oliver
**Para:** Manus
**Data:** 29 de abril de 2026
**Assunto:** Auditoria completa do repo `manus-skills` — o que mudou, e o que você precisa fazer para sua biblioteca refletir o repo

---

## Contexto rápido

Oliver pediu uma auditoria completa do repo `MrBraun92/manus-skills` em sessão Claude Code. O repo cresceu organicamente acumulando skills nativas do Claude (que ele copiou e colou), skills criadas por ele via Customize > Skills, skills experimentais adicionadas em algum momento e nunca removidas, e duplicatas.

Resultado: o repo tinha **168 skills** mas só ~40 eram realmente alinhadas ao perfil de uso real dele (solopreneur AI + tese de mestrado em inglês na UiS/Noruega + EventPro como SaaS BR + trader retail BR sofisticado).

A auditoria foi conduzida em duas fases consecutivas. Os dois commits estão em `origin/master`:
- `e1615f8` — Phase 0: arquivamento de 88 skills
- `2e29711` — Phases 1-4: adição de 40 skills v2

Branch atual: `master`. Repo final: **120 skills ativas + 88 arquivadas** em `archive/`.

---

## O que aconteceu no repo

### Phase 0 — Arquivamento

Foram movidas **88 skills da raiz para a pasta `archive/`** via `git mv` (preserva histórico, reversível). Nada foi deletado.

Critérios de arquivamento:
1. **Fora do perfil real do owner** (job-search, RenderCV, jurídico enterprise, contabilidade SOX, devops enterprise)
2. **Duplicatas literais** (ex: `accessibility-review` duplicava `accessibility-auditor`)
3. **Skills substituídas por v2 mais focadas** (ex: `stock-analysis` → `b3-ibov-analyst-br`)

Detalhes completos em `archive/README.md`.

**Skills nativas que duplicam plugin do Claude Code (`anthropic-skills:*`, `productivity:*`, etc.) foram PRESERVADAS na raiz** a pedido do owner. O Oliver mantém esse paralelismo intencional para autoria histórica.

### Phases 1-4 — Skills v2

Foram criadas **40 skills novas** distribuídas em 4 fases temáticas alinhadas ao perfil real do owner:

| Fase | Tema | Idioma | Quantidade |
|---|---|---|---:|
| 1 | Tese acadêmica (APA 7 + SIKT) | English | 12 |
| 2 | EventPro / dev | English técnico | 9 |
| 3 | Produtividade (workflow Manus/Claude/GPT) | PT-BR | 7 |
| 4 | Trading com método (disclaimer obrigatório) | PT-BR | 12 |

**Lista completa das 40 skills v2:**

Fase 1 (tese, English): `citation-integrity-checker`, `claim-evidence-mapper`, `systematic-literature-review`, `qualitative-coding-specialist`, `theoretical-integration`, `academic-paper-reviewer`, `devils-advocate-research`, `scientific-schematics`, `apa-style-enforcer`, `academic-tone-polisher`, `research-ethics-sikt-reviewer`, `thesis-defense-slide-builder`

Fase 2 (dev, English técnico): `test-automator-playwright`, `verification-before-completion`, `database-optimizer`, `react-expert`, `refactoring-specialist`, `rag-architect`, `repomix-safe-mixer`, `error-detective`, `continue-work`

Fase 3 (produtividade, PT-BR): `doc-to-markdown`, `transcript-fixer`, `meeting-to-actions`, `decision-journal`, `weekly-review`, `voice-memo-to-doc`, `cost-metering`

Fase 4 (trading, PT-BR com disclaimer): `financial-compliance-guardrails`, `trader-psychology-coach`, `portfolio-risk-manager`, `trade-journal-postmortem`, `backtesting-engineer`, `position-sizing-simulator`, `walk-forward-validator`, `macro-economic-analyst`, `economic-calendar-prep`, `b3-ibov-analyst-br`, `tax-aware-trade-accounting`, `earnings-call-analyst`

### Decisões de design importantes para você

1. **Idioma por bloco temático** — não é uniforme:
   - Tese (Fase 1) e dev (Fase 2): SKILL.md em inglês porque o output dessas skills é em inglês
   - Produtividade (Fase 3) e trading (Fase 4): SKILL.md em PT-BR porque o owner e o contexto operacional são BR

2. **Disclaimer obrigatório em skills de trading** — toda skill da Fase 4 tem blockquote `> ⚠️ Disclaimer:` no INÍCIO e no FIM do SKILL.md. Vocabulário banido do corpo: `compre`, `venda`, `garantido`, `recomendo`, `dica`, `lucro garantido`. A skill meta `financial-compliance-guardrails` é a guardiã desse contrato — é pré-requisito para qualquer skill de trading.

3. **Frontmatter `description` com palavras-chave de gatilho** — para o `skill-router` triggar corretamente, as descriptions têm verbos de ação, sinônimos e gatilhos multilíngues quando relevante (ex: `continue-work` aceita "continue", "where were we", "onde paramos", "catch me up").

4. **Stack-specific guidance baked in** — as skills da Fase 2 referenciam explicitamente o stack do EventPro (TiDB Serverless quirks, Drizzle patterns, shadcn/ui, wouter, @dnd-kit, Sprint invariants em `shared/financial.ts` etc.). Não são genéricas.

5. **Skill `continue-work` foi criada na Fase 2 e na Fase 3** — conflito identificado e resolvido: a versão final é a English técnica do Agente 1 com triggers multilíngues. Sobrescreveu uma versão PT-BR que tinha sido criada antes pelo outro agente. A versão atual cobre ambos os casos de uso.

---

## O que VOCÊ (Manus) precisa fazer

Sua biblioteca de skills no Manus precisa espelhar o estado atual do repo. Roteiro:

### 1. Sincronizar o repo
```
Pull origin/master
git log --oneline | head -3
# Deve mostrar: 2e29711, e1615f8, e9e8064 (ou mais recente)
```

### 2. Remover do seu cache de skills as 88 arquivadas
Se sua biblioteca ainda está carregando skills da raiz (não da pasta `archive/`), você precisa parar de carregar tudo o que está em `archive/`. Lista canônica em `archive/README.md`.

**Skills mais importantes que saíram (não use mais):**
- Job-search inteiro: `ai-job-scout`, `career-strategist`, `job-coach`, `job-scan`, `job-scout`, `linkedin-algorithm-expert`, `linkedin-review`, `resume-tailoring`, `cover-letter`, `hidden-job-hunter`, `industry-research`, `corpus-review`, `company-discovery`, `scoping-interview`
- RenderCV: `rendercv-development-context`, `rendercv-testing-context`, `review-rendercv-pr`, `solve-rendercv-issue`, `triage-rendercv-issue`, `publish-rendercv-typst-package`
- Legal enterprise: `triage-nda`, `review-contract`, `legal-response`, `legal-risk-assessment`, `signature-request`, `vendor-check`, `vendor-review`, `meeting-briefing`, `brief`
- Contabilidade SOX: `audit-support`, `sox-testing`, `journal-entry`, `journal-entry-prep`, `reconciliation`, `variance-analysis`, `financial-statements`, `close-management`
- DevOps enterprise: `devops-sre-agent`, `secops-agent`, `incident-response`, `runbook`, `revops-agent`
- Substituídas: `research-synthesis` (use `systematic-literature-review`), `user-research` (use `qualitative-coding-specialist`), `synthesize-research` (use `systematic-literature-review`), `stock-analysis` (use `b3-ibov-analyst-br`)

### 3. Adicionar à sua biblioteca as 40 novas (Phases 1-4)
Lista completa acima em "Phases 1-4". Cada skill está em `/<skill-name>/SKILL.md` na raiz do repo, com frontmatter `name` + `description` no padrão canônico.

**Sugestão de carga prioritária para o owner:**
1. Tese (urgente, deadline ativo): toda a Fase 1
2. EventPro (continuo): toda a Fase 2
3. Produtividade (alto ROI imediato): toda a Fase 3
4. Trading (apenas quando o owner pedir, pois é foco futuro): Fase 4 com `financial-compliance-guardrails` carregado SEMPRE primeiro

### 4. Atualizar seu skill-router
Se você roteia skills por description, as 40 v2 têm descriptions enriquecidas com gatilhos multilíngues. Reindexe.

Se você usa `skill-router` do próprio repo: ele está mantido (continua na raiz), mas considere que existem versões nativas dele em plugins do Claude Code — podemos ter divergência se Anthropic atualizar a versão nativa. O owner optou por manter o paralelismo histórico. Se você quiser garantir paridade futura, sugiro versionar o `skill-router` local com `version:` no frontmatter.

### 5. Conferência rápida
Após sincronizar:
- `find /repo -maxdepth 1 -type d ! -name '.*' ! -name 'archive' | wc -l` deve dar 120 (ou 121 se contar a raiz)
- `ls /repo/archive | wc -l` deve dar 89 (88 skills + README.md)
- `cat /repo/IMPORTACAO_SKILLS_RESUMO.md` traz o histórico completo da auditoria

---

## Pontos de atenção para sua próxima execução

1. **Não recriar skills arquivadas.** Se em alguma sessão futura o owner pedir uma skill genérica tipo "blog-writer" ou "task-management", confira primeiro `archive/README.md` — provavelmente foi arquivada por motivo. Pergunte antes de recriar.

2. **Skills de trading precisam do guardião.** Antes de carregar qualquer skill da Fase 4, `financial-compliance-guardrails` precisa estar disponível. Se você criar uma skill de trading nova, ela precisa do disclaimer no início e fim do SKILL.md, sem exceção.

3. **Idioma intencional.** Tese e dev em inglês não é descuido — é decisão. Não traduza para PT-BR.

4. **`anthropic-skills:*` é nativo do Claude Code.** Se em alguma hora o owner reclamar que uma skill "está duplicada", lembre que muitas skills nele duplicam plugins nativos por escolha — não são bugs.

5. **Workflow do owner é paralelo.** Ele edita local → push para GitHub → você roda → ele abre nova sessão Claude. A skill `continue-work` é a ponte entre essas sessões — ela espera encontrar git log atualizado, CLAUDE.md, MEMORY.md.

---

## Resumo executivo

- Repo passou de 168 → 120 skills ativas (-29%)
- Arquivamento total preservou tudo em `archive/` (88 skills, com rationale)
- 40 skills novas criadas alinhadas a 4 fases temáticas
- Disclaimer obrigatório em todas as 12 skills de trading (top + bottom)
- Skills v2 referenciam stack real (EventPro components, TiDB quirks, APA 7, SIKT)
- 0 skills perdidas, 0 conflitos restantes, 0 erros de frontmatter

**Branch:** `master`
**Commits relevantes:** `e1615f8` (Phase 0), `2e29711` (Phases 1-4)
**Documentação:** `README.md`, `IMPORTACAO_SKILLS_RESUMO.md`, `archive/README.md`

Qualquer dúvida, o Oliver tem o histórico completo da sessão Claude Code que conduziu essa auditoria.

— Claude (Opus 4.7)
