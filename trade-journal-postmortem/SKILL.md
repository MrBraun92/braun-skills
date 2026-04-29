---
name: trade-journal-postmortem
description: Registra cada trade com motivo de entrada, emoção, resultado e tese, depois identifica padrões recorrentes — "perde mais nas segundas", "FOMO custou X% no mês", "trades grandes têm hit-rate menor". Evolução real do trader baseada em dado próprio. Aciona quando o usuário pede "registrar trade", "post-mortem", "padrão dos meus trades", "como fui no mês".
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Trade Journal Postmortem

Esta skill é o diário operacional do trader Oliver. Cada trade tem dois resultados: o financeiro (P&L) e o operacional (cumpriu o plano? respeitou o stop? entrou no setup?). Trader que só registra P&L acha que aprende, mas só está confirmando viés. Esta skill estrutura o registro completo e — o passo crítico — **agrega ao longo do tempo para identificar padrões recorrentes**. Inspirada em journals do Brett Steenbarger e Mike Bellafiore (SMB Capital). Output bilíngue não — é puramente PT-BR.

## Quando usar esta skill
- Imediatamente após cada trade fechado (registro).
- Final do dia, semana ou mês (agregação e análise de padrões).
- Antes de aumentar tamanho de posição (verificar se hit-rate justifica).
- Quando o trader sente que "está perdendo o ritmo" (busca por padrão).
- Em revisão trimestral / anual.

## Metodologia

### Etapa 1: Registro de trade individual
Para cada trade, capturar:

**Dados objetivos:**
- Data e hora de entrada / saída.
- Ativo (ticker, mercado, opção?).
- Lado (compra / venda / put / call).
- Tamanho (quantidade + financeiro em BRL).
- Preço médio de entrada e de saída.
- Custos (corretagem, emolumentos).
- P&L bruto e líquido.
- Day trade ou swing.
- Tempo em posição.

**Dados subjetivos (críticos):**
- **Tese** (uma frase): por que entrou?
- **Setup** (técnico, fundamentalista, fluxo, evento, intuição).
- **Confiança** na entrada (baixa / média / alta).
- **Emoção** na entrada (calmo / ansioso / FOMO / após perda anterior).
- **Stop pré-definido** (preço e %).
- **Alvo pré-definido** (preço e %).
- **Cumpriu o plano?** (sim / não — e o porquê se não).
- **Lição** em uma frase.

### Etapa 2: Tagear o trade
Tags sugeridas para análise depois:
- **Setup**: B3 abertura, leilão, rompimento, pullback, gap, volatilidade implícita, dividendo, evento.
- **Mercado**: IBOV, IBRX, FII, ADR, opção, cripto.
- **Tamanho**: P (pequeno), M (médio), G (grande), GG (anômalo).
- **Estado emocional**: limpo, cansado, irritado, confiante demais.
- **Hora**: pré-mercado, abertura, miolo, fechamento, after.
- **Dia**: segunda... sexta.
- **Catalisador**: nenhum, resultado, macro, evento corporativo.

### Etapa 3: Agregar histórico
Quando o usuário pede análise de padrão:
- **Hit rate global** e por tag (setup, dia, hora, tamanho).
- **Profit factor** (ganhos brutos / perdas brutas) global e por tag.
- **Expectancy** por trade (R$).
- **Sequências**: maior win streak, maior loss streak.
- **Drawdown intra-período** (máximo).
- **Hit rate condicional**: hit rate de trades P vs G — se G tem hit rate menor, sizing está errado.

### Etapa 4: Identificar padrões recorrentes
Cruzar dimensões:
- "Trades às segundas têm hit rate X% vs Y% nos outros dias."
- "Trades em estado 'cansado' têm expectancy negativa."
- "Setup de gap aberto tem profit factor 0,8 — está perdendo dinheiro."
- "Trades depois de uma perda têm hit rate -15pp vs baseline."
- "Trades GG (anômalos) tiveram 2 wins e 3 losses, mas as losses foram catastróficas."

Padrão precisa de **n mínimo** (>= 10 trades) para ser estatisticamente sugestivo. Abaixo disso, é observação, não padrão.

### Etapa 5: Confrontar com plano de trading
Comparar comportamento real vs plano escrito:
- Tamanho médio respeita o que foi planejado?
- Stops foram cumpridos?
- Setups estão dentro do escopo do plano?

Desvios viram regras escritas (conecta com `trader-psychology-coach`).

### Etapa 6: Sugerir ajustes operacionais
Não emocionais. Operacionais:
- "Setup X tem profit factor < 1 nos últimos 30 trades — pausar e reavaliar."
- "Trades GG têm pior hit rate — reduzir tamanho máximo."
- "Segunda-feira tem hit rate 35% — pular segundas por 30 dias e reavaliar."
- "Após perda, próximo trade vem com viés — regra: pausar 1h após qualquer loss."

### Etapa 7: Persistir o journal
Sugerir formato: planilha ou arquivo Markdown estruturado, com uma linha por trade, em local versionado. Idealmente exportável para análise externa (Python / Excel).

## Formato de saída

**Modo registro (1 trade)**:
```markdown
# Trade #[N] — [TICKER] — [data]

| Campo | Valor |
|---|---|
| Lado | Compra |
| Tamanho | 100 @ R$ 32,40 = R$ 3.240 |
| Saída | R$ 33,10 (lucro R$ 70 bruto, R$ 60 líquido) |
| Tempo | 2h35 |
| Setup | Pullback EMA9 |
| Confiança | Alta |
| Emoção | Calma |
| Stop | R$ 31,80 (cumprido? sim) |
| Alvo | R$ 33,10 (atingido? sim) |
| Cumpriu plano? | Sim |
| Lição | "Pullback funcionou. Repetir." |
| Tags | #pullback #M #segunda #abertura #IBOV |
```

**Modo análise (período)**:
```markdown
# Análise de [período]

## Resumo
- Trades: N (X day, Y swing)
- Hit rate: Z%
- Profit factor: W
- Expectancy: R$ ... por trade
- Maior loss streak: M trades
- Drawdown intra-período: -Q%

## Por dia da semana
| Dia | Trades | Hit rate | P&L |
|---|---|---|---|
| Seg | ... | ... | ... |
| ... | ... | ... | ... |

## Por setup
| Setup | Trades | Hit rate | Profit factor |
|---|---|---|---|
| ... | ... | ... | ... |

## Por tamanho
| Tamanho | Trades | Hit rate |
|---|---|---|
| P | ... | ... |
| M | ... | ... |
| G | ... | ... |
| GG | ... | ... |

## Por estado emocional
| Estado | Trades | Hit rate | Expectancy |
|---|---|---|---|
| Calmo | ... | ... | ... |
| Cansado | ... | ... | ... |
| Pós-perda | ... | ... | ... |

## Padrões identificados (n >= 10)
1. [padrão com dado]
2. ...

## Padrões observados (n < 10, ainda não conclusivo)
1. [observação]

## Ajustes operacionais sugeridos
1. ...

## Premissas
- Período analisado: [datas]
- Custos inclusos: sim
- Dados-fonte: planilha do usuário
```

## Checklist de qualidade
- [ ] Cada trade tem tese e lição (não só P&L).
- [ ] Tags consistentes ao longo do tempo (não mudar nomenclatura).
- [ ] Padrões com n < 10 marcados como observação, não padrão.
- [ ] Hit rate condicional calculado (não só global).
- [ ] Comportamento real vs plano confrontado.
- [ ] Premissas explícitas no fim do output.
- [ ] Ajustes sugeridos são operacionais, não emocionais.

## Notas para o assistente
- **Hit rate sem profit factor é meio diagnóstico.** Trader pode ter 70% hit rate e perder dinheiro (perdas grandes, ganhos pequenos). Sempre apresentar os dois.
- **Não fazer cherry-picking de período**: se o usuário quer "ver o último mês", olhar também o mês anterior para comparar.
- **Trader pode resistir a ver dado ruim.** Tom firme: "esse setup não está pagando há 30 trades — mérito de pausar não é desistir, é higiene."
- **Dado escasso (< 30 trades total)**: análise é exploratória, não conclusiva. Sinalizar.
- **Conecta com**: `trader-psychology-coach` (viés identificado), `decision-journal` (regra nova após padrão), `position-sizing-simulator` (ajustar sizing após hit rate de tamanho), `weekly-review` (registrar lições da semana).
- **Privacidade**: P&L em BRL é dado pessoal sensível. Não exportar para fora.

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
