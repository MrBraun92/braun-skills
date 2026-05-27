---
name: pine-script-quant
description: Engenharia de indicadores, estratégias e automações no TradingView com Pine Script. Use para converter lógica operacional em código, criar estudos e estratégias, revisar scripts, corrigir bugs, estruturar alertas e melhorar backtests com disciplina metodológica.
---

# Pine Script Quant

## Visão geral

Use este skill quando o usuário quiser transformar uma lógica de mercado em **indicador, estratégia, sistema de alertas ou estudo visual no TradingView**. Ele faz a ponte entre tese operacional e implementação disciplinada em Pine Script.

O skill deve respeitar a realidade do ambiente do TradingView: scripts executam em nuvem, têm limites de tempo, memória, tamanho e acesso a dados, e precisam ser escritos de forma clara, eficiente e verificável [1].

## Quando usar

| Caso | Aplicação |
| --- | --- |
| Indicador | Converter lógica de leitura de mercado em visualização objetiva. |
| Estratégia | Traduzir regras de entrada, saída e gestão em backtest reproduzível. |
| Alerta | Gerar condições operacionais utilizáveis no TradingView. |
| Refatoração | Melhorar legibilidade, robustez e eficiência do script. |
| Debug | Corrigir repaint, lookahead, lógica inconsistente ou erro de execução. |

## Regras de implementação

### 1. Especificar a lógica antes do código

Antes de escrever Pine Script, defina claramente:

| Item | Pergunta |
| --- | --- |
| Sinal | O que exatamente gera entrada ou saída? |
| Filtro | Quais condições invalidam sinais fracos? |
| Horizonte | O script é intraday, swing ou position? |
| Objeto | É indicador visual, estratégia backtestável ou alerta? |
| Risco | Haverá stop, alvo, trailing ou apenas marcação? |

Sem isso, o código tende a ficar bonito e inútil.

### 2. Escrever com disciplina de causalidade

Nunca use informação futura de forma implícita. O skill deve ter especial cuidado com repaint, `request.security()`, confirmação de barra e leituras intrabar. Sempre deixe claro se o script opera em barra fechada, em formação, ou se depende de confirmação adicional.

### 3. Separar cálculo, sinal e visualização

Estruture o script em blocos conceituais.

| Bloco | Função |
| --- | --- |
| Inputs | Parâmetros controláveis e seguros. |
| Cálculo | Séries, filtros e variáveis-base. |
| Sinais | Regras explícitas de entrada, saída ou marcação. |
| Visual | `plot`, `bgcolor`, `label`, `table` e marcações. |
| Alertas | Condições utilizáveis pelo usuário final. |

### 4. Validar a lógica, não apenas compilar

Script que compila pode continuar ruim. Sempre verificar:

1. Se a regra implementada corresponde à tese descrita.
2. Se há risco de repaint.
3. Se o backtest está simplificando demais custos, slippage ou execução.
4. Se a visualização comunica a lógica com clareza.

### 5. Otimizar sem destruir legibilidade

Pine Script foi desenhado para criar indicadores e estratégias de forma acessível e roda na infraestrutura do TradingView, mas impõe limites computacionais e de dados [1]. Portanto, evite complexidade desnecessária, loops custosos e cálculos redundantes quando a mesma lógica puder ser expressa com séries nativas.

## Fluxo de trabalho

### Etapa A. Traduzir a tese em regras testáveis

Converta descrições vagas como “comprar quando o fluxo estiver forte” em condições mensuráveis. Se a lógica não puder ser observada no dado disponível do TradingView, diga isso antes de codar.

### Etapa B. Escolher o tipo de script

| Tipo | Quando escolher |
| --- | --- |
| `indicator()` | Quando a prioridade for visualização e apoio à decisão. |
| `strategy()` | Quando a prioridade for backtest, entradas e saídas simuladas. |
| Híbrido conceitual | Quando o usuário ainda não decidiu entre leitura visual e execução sistemática. |

### Etapa C. Codificar com explicação

Sempre que possível, entregue código acompanhado de explicação curta sobre lógica, parâmetros, limitações e modo correto de uso.

### Etapa D. Testar e revisar

Se houver resultados de backtest, interpretar com cautela. Melhorias em resultado sem robustez metodológica não são avanço real.

## Padrão de saída

| Bloco | Conteúdo |
| --- | --- |
| Objetivo do script | O que o código pretende resolver. |
| Lógica | Regras de cálculo e de sinal. |
| Implementação | Código em Pine Script com comentários úteis. |
| Alertas e uso | Como operar o script no TradingView. |
| Limitações | Repaint, timing, premissas e restrições do ambiente. |

## Limites

Este skill não deve prometer “robô vencedor” nem confundir backtest com edge comprovada. Ele deve ser rigoroso com viés de amostra, simplificações de execução e limitações do ambiente Pine.

## References

[1]: https://www.tradingview.com/pine-script-docs/welcome/ "Welcome to Pine Script® v6"
