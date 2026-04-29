# Histórico técnico de importação e auditoria

## Estado atual (abril 2026)

| Métrica | Valor |
|---|---:|
| Skills ativas no repositório | **199** |
| Skills arquivadas em `archive/` | **9** |
| Skills v2 adicionadas (Phases 1-4) | **40** |
| Repositório | `MrBraun92/manus-skills` |
| Branch principal | `master` |
| Último commit de auditoria | (commit do reverso cirúrgico) |

---

## Histórico de operações

### abril 2026 — Auditoria em 3 etapas (Oliver + Claude Opus 4.7)

**Etapa A — Phase 0 (commit `e1615f8`)**: arquivamento amplo de 88 skills baseado em perfil inferido (job-search, RenderCV, jurídico, SOX, devops). **Posteriormente revertido pelo owner** após confirmar uso real.

**Etapa B — Phases 1-4 (commit `2e29711`)**: adição de 40 Skills v2 alinhadas ao perfil real:

| Fase | Tema | Idioma | Quantidade |
|---|---|---|---:|
| 1 | Tese acadêmica (APA 7 + SIKT) | English | 12 |
| 2 | EventPro / dev | English técnico | 9 |
| 3 | Produtividade (workflow Manus/Claude/GPT) | PT-BR | 7 |
| 4 | Trading com método (disclaimer obrigatório) | PT-BR | 12 |

Lista completa em `README.md`.

**Etapa C — Reverso cirúrgico**: escopo de `archive/` reduzido para **9 skills** apenas. As 79 demais voltaram para a raiz.

#### As 9 skills que ficaram em archive

**5 fusões óbvias** (duplicatas literais entre skills do próprio repo):
1. `accessibility-review` (duplica `accessibility-auditor`)
2. `sql-queries` (duplica `write-query`)
3. `data-visualization` (duplica `create-viz`)
4. `testing-strategy` (duplica `test-strategist`)
5. `code-review` (duplica `code-auditor`)

**4 substituições estratégicas** (saíram para dar lugar às v2 mais especializadas):
1. `research-synthesis` → substituída por `systematic-literature-review` + `citation-integrity-checker` + `claim-evidence-mapper`
2. `user-research` → substituída por `qualitative-coding-specialist`
3. `synthesize-research` → substituída por `systematic-literature-review`
4. `stock-analysis` → substituída por `b3-ibov-analyst-br` (foco BR)

Detalhes completos em [`archive/README.md`](./archive/README.md).

---

## Decisões de design

### Escopo de arquivamento — cirúrgico, não amplo
A primeira tentativa de arquivamento amplo (88 skills baseado em "fora do perfil inferido") foi revertida. **A regra final é estritamente:**
- Duplicata literal entre skills do próprio repo → arquivar a duplicata
- Skill substituída por v2 mais especializada → arquivar a antiga

Nada mais é arquivado por inferência. Skills aparentemente "fora do perfil" (job-search, RenderCV, jurídico, contábil, devops enterprise, etc.) **continuam na raiz** porque o owner pode usar.

### Skills nativas duplicadas — preservadas
Skills que duplicam plugins nativos do Claude Code (`anthropic-skills:*`, `productivity:*`, `product-management:*`) foram preservadas no repo a pedido do owner para autoria histórica e versão controlada.

### Idioma por bloco temático
- **Tese (Fase 1)** — English (output da skill é em inglês)
- **Dev (Fase 2)** — English técnico (convenção universal de skills de engenharia)
- **Produtividade (Fase 3)** — PT-BR (uso pessoal, contexto BR)
- **Trading (Fase 4)** — PT-BR (trader BR, contexto B3/CVM/IR-BR)

### Disclaimer travado em skills de trading
Toda skill da Fase 4 inclui blockquote `> ⚠️ Disclaimer:` no INÍCIO e no FIM do `SKILL.md`. Vocabulário banido do corpo: "compre", "venda", "garantido", "certo", "recomendo", "dica", "lucro garantido". A meta-skill `financial-compliance-guardrails` é a guardiã desse contrato.

---

## Histórico anterior (pré-auditoria)

### Importação inicial (data desconhecida)

Sincronização original do conjunto de skills do sistema, incluindo:
- Skills nativas do Claude (73 extraídas de `Claude_Native_Skills.rtf`)
- Pacotes `.skill` enviados pelo usuário ao Manus (skill-router, devops-sre-agent, revops-agent, secops-agent, interview-intelligence-analyst, positioning-strategist, retention-lifecycle-strategist, customer-signal-synthesizer, qa-executor)
- Correção manual de frontmatter incompatível (`data-context-extractor`)

Estado intermediário: 145 skills válidas, depois cresceu para 168 antes da auditoria de abril 2026.

---

## Como reagir a futuras auditorias

1. **Não arquivar por inferência.** Para arquivar uma skill, é preciso confirmação direta do owner ou um destes 2 critérios objetivos: (a) duplicata literal de outra skill do próprio repo, (b) substituída por v2 mais especializada.
2. **Skills nativas duplicadas continuam preservadas** a menos que o owner mude de opinião.
3. **Skill de trading sempre passa por `financial-compliance-guardrails`** (disclaimer obrigatório no início e fim).
4. **Idioma respeita o bloco temático** — não traduzir Fase 1/2 para PT-BR nem Fase 3/4 para inglês.
5. **Description em frontmatter** deve incluir palavras-chave de uso para o `skill-router` triggar corretamente.
6. **Ao arquivar, sempre `git mv archive/<nome>/`** (preserva histórico) — nunca `rm -rf`.
