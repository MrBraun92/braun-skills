---
name: backtesting-engineer
description: Desenha backtest honesto de estratégia — escolhe dataset adequado, lookback realista, custos (corretagem, slippage, IR), métrica primária (Sharpe, Sortino, Calmar, max DD) e secundária (win rate, profit factor). Saída inclui código Python rodável (vectorbt ou backtrader). Aciona quando o usuário descreve estratégia e pede "backtest", "testar", "validar histórico".
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Backtesting Engineer

Esta skill desenha **backtest honesto** — porque backtest desonesto é o vício do trader retail. Sem custos, sem slippage, sem IR, com lookahead bias e dataset cherry-picked, qualquer estratégia parece milagre. Esta skill força disciplina: dataset adequado ao horizonte, custos realistas para B3, métricas múltiplas (não só Sharpe), análise de overfitting. Output é dual: relatório executivo + código Python que o usuário roda localmente. Inspirada em práticas de Marcos Lopez de Prado (*Advances in Financial Machine Learning*) e Ernest Chan.

## Quando usar esta skill
- O usuário descreveu uma estratégia textualmente ("quero testar setup B3 abertura com pullback").
- O usuário tem indicador customizado e quer ver como funcionou no passado.
- Avaliação de estratégia copiada de canal / livro / paper antes de operar.
- Comparação entre duas variantes de estratégia.
- Validação prévia antes de `walk-forward-validator` (passo seguinte natural).

## Metodologia

### Etapa 1: Operacionalizar a estratégia
A estratégia precisa virar regras objetivas. Pergunte até estar claro:
- **Universo**: quais ativos? (IBOV completo? ações específicas? FIIs?)
- **Sinal de entrada**: condição exata, sem ambiguidade. ("EMA9 cruza acima EMA21 + RSI < 70").
- **Sinal de saída**: stop loss + take profit + saída por tempo.
- **Sizing**: fixo, % do capital, vol-targeting, Kelly.
- **Frequência**: quantos sinais por mês esperados.
- **Horizonte**: intraday, swing (dias), position (semanas).

Se o usuário não consegue descrever a regra exata, a estratégia não está pronta para backtest — sinalize.

### Etapa 2: Escolher dataset
Critérios:
- **Janela mínima**: 5+ anos para estratégia swing; 1+ ano para intraday (precisa cobrir regimes diferentes — alta, baixa, lateral, crise).
- **Granularidade**: diário, intraday 5min, tick.
- **Fonte**: para B3, dados gratuitos limitados (Yahoo Finance OK para EOD; intraday exige fonte paga ou MetaTrader).
- **Survivorship bias**: incluir empresas deslistadas! Backtest no IBOV atual é cherry-picking — empresas que faliram não estão no índice hoje.
- **Splits e dividendos**: ajustar histórico.

Listar o dataset escolhido e por quê. Se houver compromisso (ex: usar EOD ajustado e perder intraday), sinalizar limitação.

### Etapa 3: Definir custos realistas para B3
- **Corretagem**: para retail, hoje 0 a R$ 5 por ordem. Para day trade, considerar slippage > corretagem.
- **Emolumentos B3**: ~0,03% por operação.
- **Slippage**: para liquidez alta (PETR4, VALE3), 1-2 ticks; para small cap, pode ser muito mais.
- **IR**: day trade 20% sobre lucro; swing 15% sobre lucro acima de R$ 20k/mês.
- **Custo de oportunidade**: capital parado rende algo (CDI ~ Selic).

Listar premissa de custo no relatório. Sem custos = backtest desonesto.

### Etapa 4: Implementar com cuidado de viés
Atenção a:
- **Lookahead bias**: usar dado que só estaria disponível no fechamento daquele dia (não no início).
- **Lookback de indicador** definido na entrada do candle, não no fechamento.
- **Slippage modelado**: preço de execução ≠ preço de fechamento.
- **Sinais sobrepostos**: o que fazer se entrada chega quando posição anterior ainda está aberta?
- **Capital alocado em paralelo**: se múltiplos sinais ativos, como ratear?

### Etapa 5: Métricas primárias e secundárias
**Primárias** (sempre apresentar):
- **Sharpe ratio** anualizado.
- **Sortino ratio** (Sharpe penaliza só downside).
- **Calmar ratio** (CAGR / max drawdown).
- **Max drawdown** (% e duração em dias).
- **CAGR** (Compound Annual Growth Rate).

**Secundárias**:
- Win rate.
- Profit factor.
- Expectancy por trade.
- Trades por mês (frequência).
- Tempo médio em posição.
- % do tempo investido vs em caixa.

Comparar contra benchmark (CDI, IBOV).

### Etapa 6: Análise de robustez
Antes de declarar estratégia "funciona":
- **Estabilidade ano a ano**: P&L positivo em todos os anos? Concentrado em um único ano?
- **Sensibilidade de parâmetros**: muda EMA9 para EMA8 e EMA10 — resultado quebra? Se sim, **overfit**.
- **Out-of-sample**: separar 20% final do dataset, treinar nos 80%, validar nos 20%.
- **Monte Carlo**: embaralhar ordem dos trades — distribuição de outcomes.

### Etapa 7: Gerar código rodável
Output Python autossuficiente. Stack sugerida:
- `vectorbt` para backtest vetorial rápido (intraday e diário).
- `backtrader` para event-driven (mais flexível, mais lento).
- `pandas` + `yfinance` para dado EOD gratuito.

Código deve incluir: download de dado, computação de sinal, simulação com custos, métricas, plot de equity curve.

### Etapa 8: Relatório honesto
Estrutura fixa (ver "Formato de saída"). Honestidade radical sobre limitações: dataset curto? sinaliza. Custos estimados? sinaliza. Sem out-of-sample? sinaliza.

## Formato de saída

**Parte 1 — Relatório**:
```markdown
# Backtest — [nome da estratégia]

## Estratégia (regras)
- Universo: ...
- Entrada: ...
- Saída (stop / alvo / tempo): ...
- Sizing: ...

## Dataset
- Período: [DD/MM/YYYY a DD/MM/YYYY]
- Granularidade: ...
- Fonte: ...
- Survivorship bias tratado? sim / não — explicar.

## Premissas de custo
- Corretagem: R$ ...
- Emolumentos: 0,03%
- Slippage: ...
- IR: 15% (swing) / 20% (day)
- Custo de oportunidade (CDI): ...% a.a.

## Resultado
| Métrica | Valor | Benchmark (CDI) | Benchmark (IBOV) |
|---|---|---|---|
| CAGR | ... | ... | ... |
| Sharpe | ... | ... | ... |
| Sortino | ... | ... | ... |
| Calmar | ... | ... | ... |
| Max drawdown | -X% | - | - |
| Win rate | Y% | - | - |
| Profit factor | Z | - | - |
| Trades / mês | N | - | - |

## Estabilidade
- P&L ano a ano: [ano-X: +Y%, ano-Z: -W%, ...]
- Sensibilidade a parâmetros: [robusto / frágil]
- Out-of-sample (20% final): [retorno OOS / IS]

## Limitações
- [limitação 1]
- [limitação 2]

## Próximo passo recomendado
[Se passou nesta etapa, levar para `walk-forward-validator`. Se não passou, descartar ou refinar.]
```

**Parte 2 — Código Python**: arquivo `.py` rodável local com `pip install vectorbt yfinance` ou similar.

## Checklist de qualidade
- [ ] Estratégia operacionalizada em regras objetivas.
- [ ] Dataset cobre múltiplos regimes de mercado.
- [ ] Survivorship bias tratado ou sinalizado.
- [ ] Custos B3 realistas inclusos (corretagem, emolumentos, slippage, IR).
- [ ] Sharpe E Sortino E Calmar E Max DD apresentados (não só Sharpe).
- [ ] Estabilidade ano a ano analisada.
- [ ] Sensibilidade de parâmetros testada.
- [ ] Out-of-sample reportado.
- [ ] Código Python rodável incluído.
- [ ] Limitações listadas honestamente.

## Notas para o assistente
- **Desconfie de Sharpe > 3.** Quase sempre overfit ou bug.
- **Desconfie de hit rate > 70%.** Setups raros têm hit rate alto mas trade é raro.
- **Estratégia só com retorno positivo no ano X**: provavelmente sorte. Estabilidade ano a ano é crítica.
- **Não aprovar para `walk-forward`** se max drawdown ultrapassa o que o usuário tolera emocionalmente. Backtest perfeito é inútil se o trader vende no -20%.
- **B3 vs US**: regras de IR completamente diferentes. Não traduzir simulação US para BR sem ajuste.
- **Cripto**: dataset 24/7, sem corretagem fixa, mas slippage alto em altcoins. Tratar separadamente.
- **Conecta com**: `walk-forward-validator` (validação fora de amostra), `position-sizing-simulator` (ajustar sizing após backtest), `trade-journal-postmortem` (confrontar backtest com real depois).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
