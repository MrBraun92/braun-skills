---
name: financial-compliance-guardrails
description: Skill meta de pré-requisito para qualquer análise de mercado, trading ou investimento. Força disclaimers, premissas explícitas, linguagem responsável. Bloqueia recomendação direta, garantia de resultado e cherry-picking de cenários. Outras skills de trading consultam esta. Aciona automaticamente em qualquer skill da Fase 4 e quando o usuário pede análise financeira.
---

> ⚠️ **Disclaimer obrigatório:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Financial Compliance Guardrails

Esta skill é **meta** — ela não produz análise por si só, ela garante que toda outra skill de trading do stack respeite limites de linguagem responsável e regulação. No Brasil, recomendação de investimento é atividade regulada pela CVM (Resolução 20/2021, agentes autônomos e analistas) e linguagem como "compre" ou "garantido" expõe o usuário a problemas legais — mesmo em ferramenta pessoal. Esta skill define o vocabulário aceitável, o conjunto mínimo de disclaimers e os anti-padrões a bloquear. Outras skills de trading (`bbb-strategist`, `position-sizing-simulator`, `b3-ibov-analyst-br`, etc.) **devem consultar esta antes de produzir output**.

## Quando usar esta skill
- Qualquer skill da Fase 4 (trading) ao começar.
- Quando o usuário pede análise de ativo, fundo, FII, opção, cripto.
- Antes de qualquer skill que poderia, sem cuidado, virar "tip de trade".
- Quando o usuário cola análise externa (relatório de banco, post de Twitter) e pede para revisar.
- Em revisão final de qualquer documento de mercado antes de publicar.

## Metodologia

### Etapa 1: Verificar contexto regulatório
Identifique:
- O usuário é trader pessoal (default — Oliver) ou está produzindo conteúdo público?
- Conteúdo vai ficar privado ou ser publicado (Twitter, LinkedIn, newsletter)?
- Mercado abordado: BR (CVM), US (SEC), cripto (jurisdição variada).

Se for **conteúdo público**, regras são mais duras — não basta disclaimer, precisa de linguagem condicional consistente.

### Etapa 2: Aplicar disclaimer obrigatório
Toda saída de skill de trading deve abrir e fechar com disclaimer. Versão mínima:

> ⚠️ **Disclaimer:** Esta análise é educacional e simulada. NÃO é recomendação de investimento. Resultados passados não garantem resultados futuros. Decisões de aporte são de responsabilidade exclusiva do usuário. Consulte profissional habilitado pela CVM para recomendação personalizada.

Versão estendida quando há cálculo de retorno projetado, sizing ou backtest:

> ⚠️ **Disclaimer estendido:** Esta análise pressupõe premissas explícitas (listadas adiante). Mudança nas premissas muda o resultado. Custos de corretagem, slippage, IR e oportunidade não estão simulados (ou estão simulados em cenário base — sinalizado adiante). Esta análise não considera situação financeira pessoal, horizonte ou perfil de risco do usuário.

### Etapa 3: Vocabulário a evitar e substituir
| ❌ Não usar | ✅ Usar |
|---|---|
| "Compre X" | "Cenário de entrada em X seria avaliado caso..." |
| "Venda Y" | "Critério para sair da posição em Y poderia ser..." |
| "Garantido" / "certo" | "Probabilisticamente provável" / "histórico sugere" |
| "Vai subir" | "Pode subir caso..." / "histórico mostra alta nesse cenário" |
| "Recomendo" | "Para fins de simulação, considere..." |
| "Tip" / "dica" | "Hipótese para estudo" |
| "Lucro X%" | "Cenário hipotético de retorno X%, sem custos" |
| "Operação certeira" | "Configuração com edge histórico de Z%" |

### Etapa 4: Bloquear anti-padrões
Recuse ou ajuste quando detectar:
- **Cherry-picking de cenário**: análise mostra apenas o cenário otimista. Forçar cenário base + estresse.
- **Curva de equity sem custos**: backtest sem corretagem, slippage e IR. Forçar inclusão.
- **Promessa absoluta**: qualquer frase com "garantido", "sem risco", "certeza".
- **Sizing exagerado**: skill sugerir alocar > 25% do portfólio em uma posição sem alerta extremo.
- **Confundir educacional com recomendação**: deixar implícito "vou fazer isso por você".
- **Linguagem urgente**: "agora ou nunca", "última chance" — induz FOMO.
- **Cripto sem disclaimer extra**: cripto tem volatilidade extrema; exigir disclaimer adicional sobre risco de perda total.

### Etapa 5: Forçar premissas explícitas
Toda projeção numérica deve listar pressupostos. Mínimo:
- Custo de corretagem assumido.
- Slippage assumido (% ou ticks).
- IR considerado (sim / não — qual alíquota).
- Período histórico usado e por que.
- Capital base assumido.
- Frequência de rebalance.

Sem premissas explícitas, o output pode ser bonito mas é falso.

### Etapa 6: Validar tom final
Antes de entregar, releia o output como se fosse um leitor cético:
- Tem alguma frase que pareceria "tip de Telegram"? Reescreva.
- Tem urgência artificial? Remova.
- O cenário base assume tudo dando certo? Adicione cenário pessimista.
- Falta o disclaimer no fim? Adicione.

## Formato de saída

Esta skill produz dois artefatos:

**1. Bloco de disclaimer pronto** (para outras skills incorporarem):
```markdown
> ⚠️ **Disclaimer:** [versão mínima ou estendida].
```

**2. Checklist de validação** que outras skills aplicam ao output delas:
```markdown
## Checklist de compliance
- [ ] Disclaimer no início e no fim.
- [ ] Zero uso de "compre", "venda", "garantido", "certo", "recomendo".
- [ ] Premissas explícitas listadas.
- [ ] Cenário base + cenário pessimista (não só otimista).
- [ ] Custos incluídos ou marcados como ausentes.
- [ ] Sem urgência artificial.
- [ ] Conteúdo público? Tom condicional consistente.
```

Se algum item falhar, esta skill devolve a lista de correções específicas.

## Checklist de qualidade
- [ ] Disclaimer presente no início e no fim do output revisado.
- [ ] Vocabulário banido foi removido / substituído.
- [ ] Premissas estão listadas explicitamente.
- [ ] Cenários múltiplos (não só otimista) foram exigidos quando aplicável.
- [ ] Avisos extras para cripto e opções (volatilidade alta) foram adicionados se aplicável.
- [ ] Distinção clara entre "educacional" e "recomendação".

## Notas para o assistente
- **Esta skill é defensiva por design.** Erra no lado do conservadorismo. Melhor diluir um output do que expor o usuário a risco regulatório.
- **Não é juridicamente vinculante** — esta skill ajuda com higiene, não substitui parecer legal. Se o usuário vai publicar conteúdo de mercado em escala, recomendar consulta com advogado / contabilidade.
- **CVM 20/2021**: distinção legal no BR é entre analista (recomenda) e educador (analisa sem recomendar). Esta skill mantém o usuário do lado educador.
- **US (SEC)**: regras semelhantes; mesma disciplina aplica.
- **Cripto**: não regulada uniformemente; risco extra de perda total deve ser explicitado.
- **Opções**: alavancagem implícita; risco assimétrico (perda potencial > prêmio em vendidas a descoberto). Forçar destaque.
- **FIIs**: tributação isenta de IR sobre rendimento mensal para PF (sob condições) — não confundir com tributação de ganho de capital na venda.

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
