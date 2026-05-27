---
name: position-sizing-simulator
description: Calcula tamanho hipotético de posição via Kelly fracionário, fixed fractional ou volatility-targeting. Inputs: capital, risco por trade, edge esperado. Output: cenários e curva de capital projetada. NUNCA diz "compre X reais", apenas simula. Aciona quando o usuário pergunta "qual tamanho", "quanto por trade", "Kelly", "como dimensionar posição".
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Position Sizing Simulator

Esta skill calcula **simulações de tamanho de posição** sob diferentes critérios de gestão de risco. Trader retail tipicamente usa "intuição" para sizing — entra com mais quando está confiante, com menos quando está cauteloso. Resultado: maximiza perda nos piores momentos. Esta skill apresenta os métodos canônicos (fixed fractional, Kelly, vol-targeting) com equações explícitas e simulação Monte Carlo, em moeda brasileira. **Nunca recomenda valor específico** — apresenta cenários para o trader escolher conscientemente.

## Quando usar esta skill
- Antes de definir tamanho de posição em estratégia recém-validada (após `backtesting-engineer`).
- Após mudança de capital (aporte ou retirada).
- Após mudança de edge percebido (estratégia que estava funcionando começou a falhar).
- Em revisão mensal de plano de trading.
- Quando trader sente que "está apostando demais" ou "de menos".

## Metodologia

### Etapa 1: Coletar parâmetros
Pedir:
- **Capital total alocado a trading** (R$).
- **Risco máximo por trade** que o trader aceita (% do capital, ex: 1%, 2%).
- **Hit rate esperado** da estratégia (do backtest ou journal).
- **Win/loss ratio** médio (R-múltiplo: ganho médio / perda média).
- **Stop loss padrão** em % do preço de entrada.
- **Volatilidade do ativo** (ATR diário ou desvio-padrão histórico).
- **Frequência** de trades (por mês).

Sem esses dados (especialmente hit rate e R-múltiplo), Kelly não pode ser calculado — sinalize.

### Etapa 2: Calcular fixed fractional
Mais simples e mais usado por retail:
- Tamanho da posição = (Capital × % risco por trade) / (Stop em % × Preço de entrada).
- Exemplo: capital R$ 100.000, risco 1%, stop 2% → posição máxima R$ 50.000 por trade.
- Não depende de hit rate; protege contra ruína.

### Etapa 3: Calcular Kelly Criterion
Fórmula:
- f* = (bp - q) / b
- Onde: b = odds (R-múltiplo), p = probabilidade de win (hit rate), q = 1-p.

Kelly puro é **agressivo demais para retail** (assume probabilidades exatas). Sempre apresentar **Kelly fracionário**:
- Half-Kelly (50%) — mais comum entre profissionais.
- Quarter-Kelly (25%) — para casos com incerteza alta no edge.

Avisar: edge percebido != edge real. Se hit rate é estimado com viés, Kelly fica errado e a curva de capital pode ruinar.

### Etapa 4: Calcular volatility-targeting
Tamanho dimensionado para que cada trade tenha o mesmo risco em vol diária:
- Tamanho = (Capital × % vol-target) / (ATR diário do ativo / preço × multiplicador).
- Útil para portfólio multi-ativo: ações com vol diferente recebem alocações diferentes para igualar contribuição de risco.

### Etapa 5: Simulação Monte Carlo
Para cada método, simular 1000 trajetórias:
- Sortear N trades com probabilidade p de win e R-múltiplo definido.
- Aplicar tamanho do método.
- Computar curva de capital final.
- Reportar: mediana, percentil 5 (cenário ruim), percentil 95 (cenário bom), probabilidade de drawdown > X%, probabilidade de ruína (capital < limite).

### Etapa 6: Cenários de estresse
Aplicar:
- **5 perdas seguidas**: o que acontece com o capital sob cada método?
- **Hit rate cai 10pp em relação ao esperado** (estratégia degradou): qual o impacto?
- **Volatilidade dobra** (regime de stress): o método ainda é viável?

### Etapa 7: Comparar métodos lado a lado
Tabela final mostrando para cada método:
- Tamanho típico em BRL.
- Crescimento esperado anual.
- Drawdown esperado.
- Probabilidade de ruína em 100 trades.
- Adequação ao perfil (conservador / moderado / agressivo).

### Etapa 8: Recomendar perfil, não valor
A skill apresenta os cenários e devolve uma sugestão de **perfil** ("trader conservador deveria operar com fixed fractional 1% ou Quarter-Kelly"). Nunca diz "use R$ X por trade".

## Formato de saída

```markdown
# Simulação de Position Sizing

## Inputs
- Capital: R$ ...
- Risco máximo por trade: ...%
- Hit rate esperado: ...%
- Win/loss ratio (R-múltiplo): ...
- Stop padrão: ...%
- Vol diária (ATR): ...

## Comparação de métodos

| Método | Tamanho típico (R$) | CAGR esperado | Max DD esperado | Prob. ruína (100 trades) |
|---|---|---|---|---|
| Fixed fractional 1% | ... | ... | ... | ... |
| Fixed fractional 2% | ... | ... | ... | ... |
| Half-Kelly | ... | ... | ... | ... |
| Quarter-Kelly | ... | ... | ... | ... |
| Vol-targeting 0,5%/dia | ... | ... | ... | ... |

## Monte Carlo (10.000 trades simulados, N trajetórias)

### Fixed fractional 1%
- Mediana de capital final: R$ ...
- Percentil 5: R$ ...
- Percentil 95: R$ ...
- Trajetórias com drawdown > 30%: X%
- Trajetórias com ruína (< capital inicial × 0,5): Y%

[mesma estrutura para os outros métodos]

## Cenários de estresse
- 5 perdas seguidas → capital cai para: [valor por método]
- Hit rate cai 10pp → CAGR vira: [por método]
- Vol dobra → tamanho ajustado: [por método]

## Sugestão de perfil
[Conservador / Moderado / Agressivo, com método sugerido para esse perfil]

## Premissas
- Custos não inclusos / inclusos: ...
- Hit rate assumido: derivado do backtest / journal de [N trades]
- Janela de simulação: ...
- Independência entre trades: assumida (atenção: violação real reduz Kelly).

## Notas críticas
- Edge percebido != edge real. Se hit rate vem de janela curta (< 100 trades), Kelly pode estar superestimando.
- Trades correlacionados (mesma tese, mesmo dia, mesmo setor) violam independência. Reduzir tamanho.
```

## Checklist de qualidade
- [ ] Pelo menos 3 métodos comparados (fixed fractional, Kelly, vol-targeting).
- [ ] Kelly apresentado como Half ou Quarter, nunca puro.
- [ ] Monte Carlo com pelo menos 1000 trajetórias.
- [ ] Cenários de estresse incluídos.
- [ ] Sugestão é de perfil, não de valor exato.
- [ ] Premissas explícitas (independência, custos, janela).
- [ ] Avisos críticos sobre edge percebido vs real.

## Notas para o assistente
- **Kelly puro praticamente nunca é apropriado para retail.** Default Half ou Quarter.
- **Trader retail tende a operar acima do Kelly** porque superestima edge. Sinalize sempre.
- **Drawdown emocional vs matemático**: trader que aguenta -50% no Excel pode entrar em pânico no -20% real. Sugerir tamanho que o trader **aguenta operar**, não só o que maximiza retorno.
- **Capital total alocado a trading** ≠ patrimônio total. Se o trader confunde, esclareça.
- **Múltiplos trades simultâneos**: independência é violada. Reduzir tamanho efetivo proporcionalmente.
- **Conecta com**: `backtesting-engineer` (input de hit rate), `trade-journal-postmortem` (input real vs esperado), `portfolio-risk-manager` (tamanho que respeita concentração), `risk-regime-portfolio` (sizing top-down).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
