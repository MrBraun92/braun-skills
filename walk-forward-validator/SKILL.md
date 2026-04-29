---
name: walk-forward-validator
description: Valida estratégia em janelas móveis (in-sample / out-of-sample) para detectar overfitting. Saída revela estabilidade da estratégia através de regimes diferentes (alta, baixa, lateral, crise). Aciona depois de `backtesting-engineer`, quando estratégia passou no backtest e o usuário pergunta "vai funcionar fora da amostra", "isso é overfit", "como saber se realmente tem edge".
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Walk-Forward Validator

Esta skill é o segundo filtro depois de `backtesting-engineer`. Backtest passar é necessário, não suficiente. Estratégia que mostra Sharpe 2 num dataset único pode estar overfitada — parâmetros foram ajustados para encaixar no histórico específico. Walk-forward analysis (WFA) divide o histórico em janelas móveis: treina parâmetros no in-sample, testa no out-of-sample (que parâmetros nunca viram), avança a janela, repete. Estratégias **realmente** robustas mantêm performance OOS próxima do IS. Estratégias overfitadas desabam OOS. Inspirada em práticas de Robert Pardo (*The Evaluation and Optimization of Trading Strategies*).

## Quando usar esta skill
- Após `backtesting-engineer`, quando estratégia mostrou Sharpe ≥ 1 e usuário quer confirmar.
- Quando backtest tem parâmetros otimizáveis (EMA com 9? 13? 21?).
- Antes de operar capital real em estratégia nova.
- Em revisão trimestral de estratégia em produção (ainda tem edge?).
- Comparando duas variantes de estratégia.

## Metodologia

### Etapa 1: Confirmar pré-requisitos
Para WFA fazer sentido, precisa:
- Estratégia já passou em `backtesting-engineer` (Sharpe > 1, custos inclusos, dataset cobrindo regimes).
- Estratégia tem **parâmetros otimizáveis** (períodos, thresholds). Estratégia sem parâmetros otimizáveis tem WFA trivial — vira só split IS/OOS único.
- Dataset com pelo menos 5 anos para swing, 1 ano para intraday.

Se faltar pré-requisito, voltar para `backtesting-engineer`.

### Etapa 2: Definir janelas
Padrão sugerido:
- **In-sample (IS)**: 12 a 24 meses.
- **Out-of-sample (OOS)**: 3 a 6 meses.
- **Step**: avanço da janela = tamanho do OOS (anchored ou rolling).

Anchored vs Rolling:
- **Rolling**: janela IS desliza junto. Cada IS tem mesmo tamanho.
- **Anchored**: IS cresce a cada step (sempre começa no início do dataset). Útil quando dado é escasso.

Documentar a escolha.

### Etapa 3: Definir critério de otimização
Otimizar pelo quê?
- Sharpe ratio (mais comum).
- Sortino (penaliza só downside).
- Calmar (penaliza drawdown forte).
- Profit factor.

**Atenção**: otimizar Sharpe sem cap pode produzir Sharpes 5 que não generalizam. Sugestão: otimizar Sortino + restrição de max drawdown.

### Etapa 4: Rodar otimização in-sample
Para cada janela IS:
- Grid search ou random search nos parâmetros.
- Selecionar combinação que maximiza critério.
- Registrar parâmetros vencedores.

### Etapa 5: Aplicar OOS
Aplicar parâmetros vencedores na janela OOS imediatamente seguinte. Computar métricas no OOS.

### Etapa 6: Agregar resultados
Após todas as janelas:
- Concatenar OOS — vira a "curva real" da estratégia.
- Comparar IS médio vs OOS médio: degradação típica.
- **Walk-forward efficiency (WFE)** = OOS médio / IS médio. Acima de 50% = razoavelmente robusto. Abaixo de 30% = overfit severo.

### Etapa 7: Análise por regime
Marcar cada janela OOS por regime de mercado:
- Alta (IBOV +5% no período).
- Baixa (IBOV -5% no período).
- Lateral.
- Crise (vol > 2x média histórica, ou drawdown > 10%).

Apresentar performance por regime. Estratégia que só funciona em alta tem edge reduzido — só vai operar 40% do tempo.

### Etapa 8: Estabilidade de parâmetros
Os parâmetros vencedores em cada janela IS são estáveis? Ou pulam de EMA9 para EMA40 a cada janela? Parâmetros instáveis indicam que não há edge real — o "ótimo" é ruído.

### Etapa 9: Veredicto operacional
Após WFA:
- **Robusto**: OOS próximo de IS, parâmetros estáveis, performance positiva nos 4 regimes.
- **Frágil**: OOS desaba, parâmetros pulam, regime-dependente.
- **Inconcludente**: dataset curto demais para WFA significativa.

Não dizer "use X parâmetro". Dizer "estratégia parece robusta nas premissas testadas — próximo passo seria papel-trade por N meses antes de capital real".

## Formato de saída

```markdown
# Walk-Forward Analysis — [estratégia]

## Setup
- Janela IS: ... meses
- Janela OOS: ... meses
- Step: ...
- Modo: anchored / rolling
- Otimização por: Sharpe / Sortino / Calmar
- Range de parâmetros testados: ...

## Resultados agregados (concatenado OOS)
| Métrica | Valor IS médio | Valor OOS concatenado | Degradação |
|---|---|---|---|
| Sharpe | ... | ... | ... |
| CAGR | ... | ... | ... |
| Max DD | ... | ... | ... |
| Win rate | ... | ... | ... |

**Walk-forward efficiency**: ...% (interpretação: robusto / razoável / overfit).

## Performance por regime
| Regime | N janelas | Sharpe OOS | CAGR OOS |
|---|---|---|---|
| Alta | ... | ... | ... |
| Baixa | ... | ... | ... |
| Lateral | ... | ... | ... |
| Crise | ... | ... | ... |

## Estabilidade de parâmetros
| Janela | Parâmetro 1 vencedor | Parâmetro 2 vencedor |
|---|---|---|
| IS 1 (mar/2020 - mar/2021) | ... | ... |
| IS 2 (jun/2020 - jun/2021) | ... | ... |
| ... | ... | ... |

Variância dos parâmetros: [baixa / média / alta]
Interpretação: [parâmetro estável → edge real / parâmetro instável → ruído]

## Veredicto
[Robusto / Frágil / Inconcludente]

## Limitações
- Dataset cobre apenas [período X].
- WFA não captura mudança estrutural pós-fim do dataset.
- Custos premiscuos: [premissa].

## Próximo passo sugerido
[Se robusto] Considerar papel-trade por 3 meses antes de capital real, com `trade-journal-postmortem` registrando.
[Se frágil] Reformular estratégia ou abandonar.
[Se inconcludente] Aguardar mais dado.
```

## Checklist de qualidade
- [ ] IS / OOS / step explícitos.
- [ ] Anchored ou rolling escolhido conscientemente.
- [ ] OOS concatenado apresentado, não só IS médio.
- [ ] WFE calculada (OOS / IS).
- [ ] Performance por regime (alta, baixa, lateral, crise).
- [ ] Estabilidade de parâmetros vencedores avaliada.
- [ ] Veredicto categórico (robusto / frágil / inconcludente).
- [ ] Limitações honestas.

## Notas para o assistente
- **WFE > 70%** quase nunca acontece — desconfie, pode ser leak de dado.
- **WFE entre 50-70%** é o esperado para estratégia razoável.
- **WFE < 30%** = overfit severo. Não operar capital real.
- **Parâmetros que mudam radicalmente entre janelas** = não há edge, é busca de overfit.
- **Estratégia robusta + drawdown intolerável** = ainda não é operável. Trader desiste no -30% mesmo que matemática diga que volta.
- **Cripto / mercados nascentes**: dataset curto força WFA aproximada. Sinalize forte limitação.
- **Conecta com**: `backtesting-engineer` (passo anterior obrigatório), `position-sizing-simulator` (sizing após WFA passar), `trade-journal-postmortem` (validação final em paper-trade).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
