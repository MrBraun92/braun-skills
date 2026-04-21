---
name: trading-thesis-orchestrator
description: Orquestra análises de mercado em renda variável. Use quando o pedido envolver direção de mercado, tese operacional, leitura de fluxo institucional, combinação entre análise técnica e fundamentalista, ou síntese de cenário para trade, swing trade ou position.
---

# Trading Thesis Orchestrator

## Visão geral

Use este skill quando o usuário não quer apenas uma leitura isolada, mas sim uma **tese operacional completa**. Ele existe para transformar perguntas amplas, como “qual a direção provável do mercado?”, “o que o fluxo está dizendo?”, “os players grandes já se posicionaram?” ou “como alinhar técnico, fundamento e risco?”, em uma análise estruturada, rastreável e acionável.

Este skill funciona como a camada de coordenação do stack. Ele decide qual lente usar primeiro, em qual profundidade, quais evidências faltam, e como consolidar conclusões sem confundir hipótese com fato observado.

## Quando usar

Acione este skill sempre que o pedido envolver uma ou mais das situações abaixo.

| Situação | Como interpretar |
| --- | --- |
| Direção de mercado | O usuário quer saber viés, tendência, regime, assimetria ou cenário-base. |
| Leitura de fluxo | O usuário quer inferir atuação de institucionais, absorção, defesa de nível, distribuição ou acumulação. |
| Tese completa | O pedido exige combinar contexto macro, preço, volume, fundamento e risco. |
| Priorização de evidências | O usuário quer separar ruído de sinal. |
| Plano operacional | O usuário quer transformar análise em gatilhos, invalidação e gestão. |

## Papel dentro do stack

Este skill deve coordenar os demais skills especializados sempre que o escopo pedir profundidade adicional.

| Skill complementar | Quando puxar |
| --- | --- |
| `technical-price-action` | Quando a estrutura de preço, candles, suportes, resistências e indicadores forem centrais. |
| `order-flow-microstructure` | Quando a pergunta envolver players, agressão, absorção, volume profile, VWAP ou comportamento intradiário. |
| `equity-fundamental-analyst` | Quando valuation, balanços, resultados, guidance, margens e qualidade do negócio forem relevantes. |
| `pine-script-quant` | Quando o usuário quiser transformar uma lógica analítica em indicador, estratégia, screener ou alerta no TradingView. |
| `risk-regime-portfolio` | Quando o foco for sizing, risco, correlação, volatilidade, proteção ou construção de portfólio. |

## Fluxo de trabalho

### 1. Identificar o horizonte decisório

Antes de analisar, determine se a pergunta é de **intraday, swing, position ou alocação**. A mesma evidência muda de significado conforme o horizonte. Um rompimento intradiário pode ser ruído para um position trader, enquanto uma compressão semanal pode ser invisível para quem opera fluxo curto.

### 2. Definir a pergunta central

Reescreva mentalmente o pedido em uma pergunta operacional única. Exemplos úteis:

| Pedido bruto do usuário | Pergunta operacional |
| --- | --- |
| “Como está o mercado?” | Qual é o regime atual e qual lado tem vantagem estatística agora? |
| “Tem player comprando?” | Há sinais observáveis de defesa, absorção ou aceitação de preços mais altos? |
| “Vale entrar nesse papel?” | Existe assimetria favorável, com gatilho, invalidação e contexto coerentes? |

### 3. Mapear as evidências na ordem correta

Comece do contexto mais estrutural para o mais tático.

1. Regime e contexto.
2. Estrutura de preço e localização no range.
3. Volume, participação e qualidade do movimento.
4. Fundamento, se o ativo exigir.
5. Risco, invalidação e assimetria.

Nunca comece pelo candle isolado se o problema for estrutural.

### 4. Separar observação, interpretação e inferência

Toda boa tese precisa distinguir três camadas.

| Camada | O que entra |
| --- | --- |
| Observação | Fatos verificáveis: tendência, volume, gap, resultados, volatilidade, posicionamento relativo. |
| Interpretação | Leitura técnica ou fundamental derivada dos fatos. |
| Inferência | Hipótese sobre intenção de players ou provável continuação. |

Se a base observável for fraca, reduza a confiança da inferência.

### 5. Produzir uma tese em cenários

A saída padrão deve conter cenário-base, cenário alternativo e invalidação. Não entregue direção única como se fosse certeza.

Use a estrutura abaixo.

| Bloco | Conteúdo esperado |
| --- | --- |
| Contexto | Regime, horizonte e condição do mercado. |
| Evidências | Principais sinais objetivos que sustentam a leitura. |
| Tese-base | Leitura principal e por que ela faz sentido. |
| Risco de erro | O que pode invalidar a tese ou indicar armadilha. |
| Plano | Gatilho, confirmação, stop conceitual e acompanhamento. |

## Regras de qualidade

Priorize sempre a **coerência entre horizontes**. Se o semanal estiver em tendência forte de alta e o intraday mostrar exaustão, descreva isso como conflito de timing, e não como contradição lógica.

Quando o usuário falar em “grandes players”, não finja acesso a intenção real. Inferir participação institucional é permitido; afirmar intenção escondida sem evidência não é. Use linguagem como “há indícios compatíveis com absorção” ou “o comportamento sugere defesa”, e não “o institucional vai fazer X”.

Quando faltarem dados, explicite a limitação. Se não houver volume confiável, tape reading, profundidade ou dados de opções, não substitua ausência de evidência por convicção narrativa.

## Saída padrão

Ao responder, organize a análise na seguinte sequência.

1. Definição do horizonte.
2. Leitura do regime.
3. Evidências-chave.
4. Tese-base.
5. Cenário alternativo.
6. Níveis ou condições de invalidação.
7. Próxima ação recomendada para investigação ou execução.

## Limites

Este skill melhora a qualidade analítica, mas não deve prometer previsão determinística, rentabilidade futura ou certeza sobre movimentos de mercado. Ele serve para elevar a leitura de contexto, a qualidade da hipótese e a disciplina da decisão.
