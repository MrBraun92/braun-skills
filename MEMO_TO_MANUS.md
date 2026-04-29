# MEMO

**De:** Claude (Opus 4.7), em sessão Claude Code com Oliver
**Para:** Manus
**Data:** 29 de abril de 2026 (atualizado)
**Assunto:** Auditoria do repo `manus-skills` — escopo final cirúrgico (9 arquivadas) + 40 skills v2

---

## Contexto rápido

Oliver pediu uma auditoria do repo `MrBraun92/manus-skills` em sessão Claude Code.

A auditoria passou por 3 etapas:

1. **Phase 0** — proposta inicial de arquivamento amplo (88 skills) baseada em perfil inferido. **Revertida** após o owner confirmar que usa o conteúdo do dia-a-dia.
2. **Phases 1-4** — 40 skills v2 adicionadas em 4 fases temáticas alinhadas ao perfil real.
3. **Reverso cirúrgico** — escopo de `archive/` reduzido para **9 skills** (5 fusões duplicatas + 4 substituições estratégicas).

**Estado final:** **199 skills ativas + 9 arquivadas em `archive/`**.

---

## O que aconteceu no repo (escopo final)

### As 9 skills que ficaram em archive

**5 fusões óbvias** (duplicatas literais entre skills do próprio repo):

| Arquivada | Mantida (na raiz) |
|---|---|
| `accessibility-review` | `accessibility-auditor` |
| `sql-queries` | `write-query` |
| `data-visualization` | `create-viz` |
| `testing-strategy` | `test-strategist` |
| `code-review` | `code-auditor` |

**4 substituições estratégicas** (saíram para dar lugar às v2):

| Arquivada | Substituída por |
|---|---|
| `research-synthesis` | `systematic-literature-review` + `citation-integrity-checker` + `claim-evidence-mapper` |
| `user-research` | `qualitative-coding-specialist` |
| `synthesize-research` | `systematic-literature-review` |
| `stock-analysis` | `b3-ibov-analyst-br` |

Tudo o mais que estava em `archive/` no commit `e1615f8` foi **restaurado para a raiz**. O owner confirmou que usa cluster job-search, cluster RenderCV, jurídico, SOX e devops enterprise quando o caso aparece — então NÃO devem ser tratados como descartados.

### As 40 skills v2 adicionadas

**Fase 1 (tese, English):** `citation-integrity-checker`, `claim-evidence-mapper`, `systematic-literature-review`, `qualitative-coding-specialist`, `theoretical-integration`, `academic-paper-reviewer`, `devils-advocate-research`, `scientific-schematics`, `apa-style-enforcer`, `academic-tone-polisher`, `research-ethics-sikt-reviewer`, `thesis-defense-slide-builder`

**Fase 2 (dev, English técnico):** `test-automator-playwright`, `verification-before-completion`, `database-optimizer`, `react-expert`, `refactoring-specialist`, `rag-architect`, `repomix-safe-mixer`, `error-detective`, `continue-work`

**Fase 3 (produtividade, PT-BR):** `doc-to-markdown`, `transcript-fixer`, `meeting-to-actions`, `decision-journal`, `weekly-review`, `voice-memo-to-doc`, `cost-metering`

**Fase 4 (trading, PT-BR com disclaimer):** `financial-compliance-guardrails`, `trader-psychology-coach`, `portfolio-risk-manager`, `trade-journal-postmortem`, `backtesting-engineer`, `position-sizing-simulator`, `walk-forward-validator`, `macro-economic-analyst`, `economic-calendar-prep`, `b3-ibov-analyst-br`, `tax-aware-trade-accounting`, `earnings-call-analyst`

### Decisões de design importantes

1. **Idioma por bloco** — Tese (Fase 1) e dev (Fase 2) em inglês porque o output dessas skills é em inglês. Produtividade (Fase 3) e trading (Fase 4) em PT-BR porque o owner e contexto operacional são BR.

2. **Disclaimer obrigatório em skills de trading** — toda skill da Fase 4 tem blockquote `> ⚠️ Disclaimer:` no INÍCIO e no FIM. Vocabulário banido: `compre`, `venda`, `garantido`, `recomendo`, `dica`, `lucro garantido`. `financial-compliance-guardrails` é a guardiã.

3. **Skills nativas duplicadas continuam preservadas** — `anthropic-skills:*`, `productivity:*`, etc. já presentes no repo a pedido do owner.

4. **Stack-specific guidance baked in** — Fase 2 referencia explicitamente TiDB Serverless quirks, Drizzle patterns, shadcn/ui, wouter, @dnd-kit, invariantes da Sprint 5/6/7.

5. **Não arquivar por inferência.** Daqui pra frente, só arquivar com confirmação direta do owner ou se for (a) duplicata literal do próprio repo, ou (b) substituição direta por skill v2 mais especializada.

---

## O que VOCÊ (Manus) precisa fazer

### 1. Sincronizar o repo
```
git pull origin master
git log --oneline | head -5
```

### 2. Garantir que sua biblioteca tem 199 skills ativas
- Restaurar todas as 79 skills que estavam em `archive/` no commit `e1615f8` mas voltaram para a raiz no reverso cirúrgico (são todas as job-search, RenderCV, jurídico, SOX, devops enterprise, etc. que tinham sido arquivadas).
- Manter na sua biblioteca apenas como ARQUIVADAS as 9 skills listadas acima.

### 3. Adicionar à sua biblioteca as 40 v2 (Phases 1-4)
Lista completa acima. Cada skill tem `SKILL.md` na raiz com frontmatter padrão (`name` + `description`).

**Sugestão de carga prioritária:**
1. Tese (urgente, deadline ativo): toda a Fase 1
2. EventPro (continuo): toda a Fase 2
3. Produtividade (alto ROI imediato): toda a Fase 3
4. Trading: Fase 4 com `financial-compliance-guardrails` carregado SEMPRE primeiro

### 4. Atualizar seu skill-router
As 40 v2 têm descriptions enriquecidas com gatilhos multilíngues. Reindexe.

### 5. Conferência rápida
Após sincronizar:
- `find /repo -maxdepth 1 -type d ! -name '.*' ! -name 'archive' | wc -l` deve dar **199**
- `ls /repo/archive | grep -v README.md | wc -l` deve dar **9**
- `cat /repo/IMPORTACAO_SKILLS_RESUMO.md` traz o histórico completo

---

## Pontos de atenção

1. **Skills do cluster job-search, RenderCV, jurídico, SOX, devops** — o owner confirmou que usa eventualmente. **NÃO arquivar de novo sem aprovação explícita.**

2. **Skills de trading precisam do guardião.** Antes de carregar qualquer skill da Fase 4, `financial-compliance-guardrails` precisa estar disponível. Skill de trading nova → disclaimer no início e fim do `SKILL.md`, sem exceção.

3. **Idioma intencional.** Tese e dev em inglês não é descuido — é decisão. Não traduzir.

4. **Workflow do owner é paralelo.** Ele edita local → push para GitHub → você roda → ele abre nova sessão Claude. A skill `continue-work` é a ponte entre essas sessões — espera encontrar git log atualizado, CLAUDE.md, MEMORY.md.

5. **Skills nativas com 🔁 no README** — duplicam plugins nativos do Claude Code. Preservadas por escolha. Não tratar como bug.

---

## Resumo executivo

- Repo passou por arquivamento amplo (88) → revertido → arquivamento cirúrgico final (9)
- 40 skills v2 adicionadas em 4 fases temáticas
- Disclaimer obrigatório em todas as 12 skills de trading (top + bottom)
- Skills v2 referenciam stack real (EventPro components, TiDB quirks, APA 7, SIKT)
- 0 skills perdidas, 0 conflitos restantes, 0 erros de frontmatter
- **199 ativas + 9 arquivadas**

**Branch:** `master`
**Documentação:** `README.md`, `IMPORTACAO_SKILLS_RESUMO.md`, `archive/README.md`

— Claude (Opus 4.7)
