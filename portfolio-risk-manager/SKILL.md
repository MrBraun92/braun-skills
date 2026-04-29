---
name: portfolio-risk-manager
description: Mede risco total do portfólio — concentração, drawdown máximo histórico, exposição setorial, correlação intra-portfólio, VaR (95% e 99%) e CVaR. Aceita planilha de posições ou input manual. Output em PT-BR com disclaimer e cenários de estresse. Aciona quando o usuário pergunta "qual meu risco", "qual minha exposição", "quanto posso perder", ou cola lista de posições.
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Portfolio Risk Manager

Esta skill mede o risco do portfólio do trader retail brasileiro — Oliver opera B3 (ações, FIIs), considera opções, e possivelmente cripto. Trader retail típico olha P&L, ignora risco. Esta skill traz métricas profissionais (concentração, drawdown, VaR, CVaR, correlação) traduzidas em linguagem operacional e em moeda brasileira. Não é otimização de portfólio (Markowitz / Black-Litterman), é diagnóstico — "onde está o risco escondido?".

## Quando usar esta skill
- Mensalmente, como parte do `weekly-review` quando vira fim de mês.
- Antes de aumentar posição (entender concentração resultante).
- Após queda de mercado, para confrontar drawdown real vs esperado.
- Quando o usuário sente que "está exposto demais" mas não sabe quantificar.
- Antes de mudança grande (rebalance, evento macro, IPO, ciclo eleitoral).

## Metodologia

### Etapa 1: Coletar dados do portfólio
Pedir:
- Lista de posições: ticker, quantidade, preço médio, preço atual, mercado (B3 / cripto / US).
- Setor / categoria de cada posição (ações: setor IBOV; FIIs: tipo — tijolo, papel, fundo de fundos).
- Capital total alocado e capital disponível em caixa.
- Histórico de retornos diários por ativo (ideal: últimos 252 dias úteis).

Sem histórico, métricas como VaR e drawdown ficam aproximadas — sinalize.

### Etapa 2: Calcular concentração
- **% de cada posição** sobre o total.
- **Top 5 posições** somam quanto?
- **Posição maior** vs posição mediana — desvio.
- **Threshold de alerta**: posição > 15% do portfólio = concentração alta; > 25% = concentração extrema (justificar).

### Etapa 3: Calcular exposição setorial
Para B3, agrupar por setor IBOV:
- Bancário, Petróleo, Mineração, Consumo, Energia Elétrica, Saneamento, Saúde, Tecnologia, Imobiliário (FIIs), etc.
Threshold: setor > 30% = concentração setorial alta.

### Etapa 4: Calcular correlação intra-portfólio
Usar matriz de correlação 1Y entre ativos do portfólio. Identificar:
- Pares com correlação > 0,8 (movem juntos — diversificação ilusória).
- Posições com correlação > 0,9 com IBOV (basicamente são proxy do índice).
- Posições com correlação negativa (hedge real).

### Etapa 5: Calcular drawdown
- **Drawdown atual**: distância do pico histórico do portfólio (%).
- **Drawdown máximo histórico** dos últimos 1 e 3 anos.
- **Tempo médio de recuperação** após drawdowns.

### Etapa 6: Calcular VaR e CVaR
- **VaR 95% / 1 dia**: pior perda esperada em 19 de 20 dias normais.
- **VaR 99% / 1 dia**: pior perda em 99 de 100 dias.
- **CVaR (Expected Shortfall) 95%**: média das perdas piores que o VaR.
- Método: histórico (recomendado para retail) ou paramétrico (assume normalidade — sinalizar limitação).

Em BRL absoluto, não só em %. Trader retail entende melhor "posso perder R$ 12.300 num dia ruim de 1 em 20" do que "VaR é 2,4%".

### Etapa 7: Cenários de estresse
Aplicar cenários históricos relevantes ao BR:
- **Joesley day (maio/2017)**: IBOV -8,8% no dia.
- **Março/2020 (covid)**: IBOV -45% em ~30 dias.
- **2008 (crise sub-prime)**: IBOV -50% em 6 meses.
- **Eleição polarizada**: dólar +10% / IBOV -8% em poucos dias.

Aplicar cada cenário ao portfólio atual: quanto perderia em BRL?

### Etapa 8: Identificar riscos escondidos
- **Cripto sem disclaimer extra**: risco de perda total — sinalizar.
- **Opções vendidas a descoberto**: perda potencial ilimitada.
- **Margem usada**: alavancagem efetiva do portfólio.
- **FIIs muito alavancados**: alavancagem indireta.
- **Concentração regional/cambial**: tudo em BRL? Tudo em US?
- **Posições ilíquidas**: small caps com volume diário < posição (não dá para sair).

### Etapa 9: Sumarizar com semáforo
Devolver dashboard com 5 dimensões em verde / amarelo / vermelho:
- Concentração
- Diversificação setorial
- Drawdown atual
- Exposição cambial
- Liquidez

## Formato de saída

```markdown
# Diagnóstico de Risco do Portfólio — [data]

## Snapshot
- Capital total: R$ ...
- Posições abertas: N
- Caixa: R$ ... (Y%)
- Drawdown atual vs pico: -X%

## Semáforo de risco
| Dimensão | Status | Comentário |
|---|---|---|
| Concentração | 🟢 / 🟡 / 🔴 | ... |
| Setorial | ... | ... |
| Drawdown | ... | ... |
| Cambial | ... | ... |
| Liquidez | ... | ... |

## Concentração
- Top 5 posições: X% do portfólio.
- Maior posição: TICKER (Y%).
- Mediana: Z%.

## Setorial
| Setor | % portfólio |
|---|---|
| ... | ... |

## Correlação
- Pares com corr > 0,8: [PAR1, PAR2]
- Hedges reais (corr < 0): [...]

## VaR / CVaR (1 dia)
- VaR 95%: -R$ ... (-X%)
- VaR 99%: -R$ ... (-Y%)
- CVaR 95%: -R$ ...

## Drawdown
- Atual: -X%
- Máximo 3 anos: -Y%
- Tempo médio de recuperação histórico: Z dias.

## Cenários de estresse
| Cenário histórico | Perda projetada (R$) | % portfólio |
|---|---|---|
| Joesley day | -R$ ... | -X% |
| Covid mar/2020 | ... | ... |
| Crise 2008 | ... | ... |

## Riscos escondidos
- [risco 1]
- [risco 2]

## Premissas
- Histórico usado: últimos N dias úteis.
- VaR método: histórico / paramétrico.
- Correlação calculada sobre janela de M meses.
- Custos não inclusos.
```

## Checklist de qualidade
- [ ] Métricas em BRL absoluto, não só em %.
- [ ] Premissas listadas explicitamente.
- [ ] Cenários de estresse são históricos reais brasileiros.
- [ ] Riscos escondidos (cripto, opções, alavancagem) sinalizados.
- [ ] Semáforo de 5 dimensões presente.
- [ ] Sem recomendação de "vender X" — apenas diagnóstico.

## Notas para o assistente
- **Trader retail BR raramente tem dados completos.** Aceite portfólio com 6 meses de histórico e sinalize que VaR fica menos confiável.
- **FIIs**: tratar como classe separada de ações comuns. Volatilidade menor mas não zero. Considerar risco de liquidez do FII específico.
- **Cripto**: não calcular VaR paramétrico (caudas gordas demais). Usar VaR histórico ou cenários de estresse com -50% / -80%.
- **Opções**: sizing de risco precisa considerar delta-gamma. Para retail, simplificar: posição vendida a descoberto → tratar como concentrada infinita.
- **Não recomendar rebalance específico**: skill é diagnóstico. Se usuário quiser plano de ação, usar `bbb-strategist` ou `risk-regime-portfolio` em sequência.
- **Dado faltante**: marcar com `?` em vez de inventar.

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
