# archive/ — Skills arquivadas (escopo final)

Esta pasta contém skills desativadas do auto-loading mas **preservadas para histórico**. Cada uma foi removida da raiz por uma razão documentada.

**Como reativar:** `git mv archive/<skill-name>/ ./<skill-name>/` e push.

---

## Princípio editorial

A auditoria de abril de 2026 foi conduzida em 2 fases. A primeira tentou um arquivamento amplo (88 skills) baseado em perfil inferido. **O owner reverteu o escopo amplo** após confirmar que usa muitas dessas skills no dia-a-dia. A regra final ficou estritamente cirúrgica:

**Só vão para `archive/` skills que se encaixam em UM destes 2 critérios:**

1. **Duplicata literal** entre skills do próprio repo (mesma função, mesmo escopo)
2. **Substituída por uma skill v2** mais especializada e mais alinhada ao stack real (tese em inglês APA / EventPro / trader BR)

Nada mais. Skills que apenas "parecem fora do perfil" foram preservadas no repo principal porque o owner pode estar usando.

---

## Skills arquivadas — 9 total

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

Estas saíram para dar lugar a v2 mais focadas no stack real do owner. As substitutas vivem na raiz.

| Skill arquivada | Substituída por (skill v2) | Razão |
|---|---|---|
| `research-synthesis` | `systematic-literature-review` + `citation-integrity-checker` + `claim-evidence-mapper` | Tese exige rigor APA + integridade de citação explícita |
| `user-research` | `qualitative-coding-specialist` | Tese qualitativa precisa de coding formal (open / axial / thematic) |
| `synthesize-research` | `systematic-literature-review` | Substituído por método PRISMA-friendly |
| `stock-analysis` | `b3-ibov-analyst-br` | Foco BR (B3, IBOV, BDR, FII) > genérico US |

---

## O que NÃO foi arquivado

Praticamente tudo o resto. Skills mantidas na raiz mesmo que aparentem estar fora do perfil:

- **Cluster job-search** (ai-job-scout, career-strategist, etc.) — owner usa quando aplicável
- **Cluster RenderCV** — owner usa quando aplicável
- **Cluster legal enterprise** — owner usa quando aplicável
- **Cluster contabilidade SOX** — owner usa quando aplicável
- **Cluster devops enterprise** — owner usa quando aplicável
- **Skills genéricas como `audit`, `init`, `start`, `update`, `brief`** — owner usa quando aplicável
- **Skills nativas duplicadas com plugins do Claude Code** — preservadas para autoria histórica e versão controlada

Se em alguma auditoria futura o owner sinalizar que parou de usar algum cluster, esse cluster pode ser candidato a arquivamento — mas **só com aprovação explícita por skill ou por cluster**, não por inferência.

---

## Histórico

- **abril 2026** — Auditoria com escopo amplo proposto (88 skills) **revertida**. Escopo final cirúrgico de 9 skills (apenas duplicatas literais e substituições estratégicas pelas v2).
