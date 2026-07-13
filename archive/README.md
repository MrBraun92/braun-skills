# archive/ — Skills arquivadas (escopo final)

Esta pasta contém skills desativadas do auto-loading mas **preservadas para histórico**. Cada uma foi removida da raiz por uma razão documentada.

**Como reativar:** mover a pasta correspondente de `archive/` para a categoria ativa apropriada e atualizar os READMEs.

---

## Princípio editorial

A auditoria de abril de 2026 foi conduzida em 2 fases. A primeira tentou um arquivamento amplo (88 skills) baseado em perfil inferido. **O owner reverteu o escopo amplo** após confirmar que usa muitas dessas skills no dia-a-dia. A regra final ficou estritamente cirúrgica:

**Só vão para `archive/` skills que se encaixam em UM destes critérios:**

1. **Duplicata literal ou semântica** entre skills do próprio repo.
2. **Substituída por uma skill v2 ou pack ativo** mais especializado e alinhado ao stack real.
3. **Desativada explicitamente pelo owner** para evitar conflito de roteamento entre agentes.

Nada mais. Skills que apenas "parecem fora do perfil" são preservadas no repo principal porque o owner pode estar usando.

---

## Skills arquivadas — 11 total

### Bloco 1 — Fusões óbvias (5 skills)

Duplicatas literais entre skills do próprio repo. Mantida a versão mais limpa, arquivada a duplicata.

| Skill arquivada | Mantida (na raiz) | Razão |
|---|---|---|
| `accessibility-review` | `accessibility-auditor` | Mesmo escopo (WCAG audit) |
| `sql-queries` | `write-query` | Duplicata literal de SQL writing |
| `data-visualization` | `create-viz` | Duplicata literal de Python visualization |
| `testing-strategy` | `test-strategist` | Duplicata semântica |
| `code-review` | `code-auditor` | Mesmo escopo (review de PR/diff) |

### Bloco 2 — Substituições estratégicas (4 skills)

Estas saíram para dar lugar a versões mais focadas no stack real do owner.

| Skill arquivada | Substituída por | Razão |
|---|---|---|
| `research-synthesis` | `systematic-literature-review` + `citation-integrity-checker` + `claim-evidence-mapper` | Tese exige rigor APA + integridade de citação explícita |
| `user-research` | `qualitative-coding-specialist` | Tese qualitativa precisa de coding formal |
| `synthesize-research` | `systematic-literature-review` | Substituído por método PRISMA-friendly |
| `stock-analysis` | `b3-ibov-analyst-br` | Foco BR (B3, IBOV, BDR, FII) > genérico US |

### Bloco 3 — LinkedIn legacy (2 skills)

Arquivadas explicitamente para evitar conflito de gatilhos e recomendações com o pack ativo.

| Skill arquivada | Substituída por | Razão |
|---|---|---|
| `linkedin-algorithm-expert` | `09-career-job-search/linkedin-pack/` | Misturava perfil, algoritmo, SSI e conteúdo; continha heurísticas antigas e sobreposição com o novo pack. Referências auxiliares foram preservadas junto da skill. |
| `linkedin-review` | `09-career-job-search/linkedin-pack/linkedin-profile-optimizer/` | Workflow anterior de revisão de perfil substituído pelo otimizador integrado. O workflow externo referenciado não estava presente no repositório no momento do arquivamento. |

As duas ficam em [`archive/linkedin-legacy/`](./linkedin-legacy/) e **não devem ser carregadas junto com o pack ativo**.

---

## O que NÃO foi arquivado

Praticamente tudo o resto. Skills mantidas na raiz mesmo que aparentem estar fora do perfil:

- **Cluster job-search** — owner usa quando aplicável.
- **Cluster RenderCV** — owner usa quando aplicável.
- **Cluster legal enterprise** — owner usa quando aplicável.
- **Cluster contabilidade SOX** — owner usa quando aplicável.
- **Cluster devops enterprise** — owner usa quando aplicável.
- **Skills genéricas como `audit`, `init`, `start`, `update`, `brief`** — owner usa quando aplicável.
- **Skills nativas duplicadas com plugins do Claude Code** — preservadas para autoria histórica e versão controlada.

Se em alguma auditoria futura o owner sinalizar que parou de usar algum cluster, esse cluster pode ser candidato a arquivamento — mas **só com aprovação explícita por skill ou por cluster**, não por inferência.

---

## Histórico

- **Julho 2026** — `linkedin-algorithm-expert` e `linkedin-review` arquivadas após substituição pelo novo LinkedIn Skills Pack de cinco módulos.
- **Abril 2026** — Auditoria com escopo amplo proposto (88 skills) revertida. Escopo final cirúrgico de 9 skills.