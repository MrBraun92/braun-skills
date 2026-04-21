# Stack de Skills para Trading e Renda Variável

## Prompt engenheirado

O pedido original já tinha boa direção, mas estava amplo demais para virar um stack reutilizável de alta qualidade. O prompt abaixo foi refinado para deixar explícitos o escopo, a segmentação dos skills, o objetivo analítico e o padrão de entrega.

```text
Atue como um arquiteto de skills especializado em mercado financeiro, trading discricionário, análise técnica, análise fundamentalista, fluxo, microestrutura e automação no ecossistema TradingView.

Crie um stack de skills modular e complementar para renda variável, de modo que cada skill tenha uma função nítida, baixa sobreposição e alto valor prático. O stack deve permitir analisar direção de mercado, estrutura de preço, leitura de fluxo, atuação provável de grandes players, qualidade fundamentalista de ativos, construção de risco e tradução de teses operacionais em Pine Script.

Requisitos:
1. Criar skills especializados, com nomes claros e escopos não redundantes.
2. Cobrir pelo menos estas frentes: orquestração da tese, análise técnica/price action, fluxo e microestrutura, análise fundamentalista, Pine Script/TradingView e gestão de risco/regime.
3. Em cada skill, deixar muito claro quando usar, quando não usar, qual pergunta aquele skill responde melhor e qual deve ser sua saída padrão.
4. O stack deve ser orientado a identificar sinais que o mercado deixa, distinguir evidência de narrativa e evitar conclusões determinísticas sobre a intenção dos grandes players.
5. O skill de Pine Script deve ser alinhado ao ambiente real do TradingView e às restrições e conceitos oficiais do Pine Script.
6. A entrega final deve conter um resumo executivo do stack e os arquivos dos skills prontos para instalação.

Critérios de qualidade:
- Linguagem profissional, objetiva e acionável.
- Forte separação entre observação, interpretação e inferência.
- Baixa sobreposição entre skills.
- Utilidade real para trade, swing trade, position e análise de carteira.
- Sem promessas irreais de previsão ou lucro garantido.
```

## Resumo executivo do stack

O stack foi desenhado para separar com clareza **coordenação de tese**, **leitura de preço**, **leitura de fluxo**, **fundamento**, **implementação em TradingView** e **gestão de risco**. Essa arquitetura reduz sobreposição e permite que cada skill responda a uma pergunta específica, mas ainda funcione em conjunto quando o usuário pedir uma leitura completa do mercado.

| Skill | Papel principal | Melhor pergunta que responde |
| --- | --- | --- |
| `trading-thesis-orchestrator` | Coordena a tese e integra as outras lentes. | “Qual é a leitura consolidada e o que realmente importa aqui?” |
| `technical-price-action` | Lê estrutura, candles, níveis e timing. | “O preço está mostrando continuação, reversão ou armadilha?” |
| `order-flow-microstructure` | Interpreta volume, aceitação e rejeição de preço. | “Há sinais compatíveis com atuação forte ou defesa de nível?” |
| `equity-fundamental-analyst` | Testa qualidade do negócio e valuation. | “O preço está coerente com os fundamentos?” |
| `pine-script-quant` | Converte lógica operacional em código Pine Script. | “Como transformar essa tese em indicador, estratégia ou alerta?” |
| `risk-regime-portfolio` | Define sizing, regime e risco agregado. | “Quanto arriscar e como adaptar a exposição ao ambiente?” |

## Observações de design

O stack foi construído para trabalhar com linguagem probabilística e disciplina analítica. Em particular, a camada de fluxo evita afirmar intenção oculta de participantes sem evidência suficiente, enquanto a camada de Pine Script foi alinhada ao manual oficial do Pine Script v6, que enfatiza o caráter cloud-based da linguagem e suas limitações de recursos [1].

## References

[1]: https://www.tradingview.com/pine-script-docs/welcome/ "Welcome to Pine Script® v6"
