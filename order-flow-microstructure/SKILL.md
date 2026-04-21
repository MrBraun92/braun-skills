---
name: order-flow-microstructure
description: Leitura de fluxo e microestrutura para renda variável. Use quando o pedido envolver volume, VWAP, volume profile, auction market theory, absorção, exaustão, aceitação ou rejeição de preço, participação institucional e comportamento intradiário.
---

# Order Flow Microstructure

## Visão geral

Use este skill quando o usuário quiser ir além do gráfico visual e perguntar **quem provavelmente está dominando a negociação, onde o mercado está aceitando preço e onde está rejeitando**, mesmo que os dados disponíveis sejam imperfeitos.

O foco aqui é interpretar o mercado como um processo de leilão. Preço sobe quando níveis mais altos são aceitos; preço cai quando níveis mais baixos são aceitos; e o fluxo ajuda a entender quando há defesa, absorção, falha de continuação, exaustão ou deslocamento legítimo.

## Quando usar

| Caso | Aplicação |
| --- | --- |
| Volume e contexto | Ler se o movimento está sendo aceito ou rejeitado. |
| VWAP e intraday | Avaliar controle, reversão para média, tendência e posicionamento relativo. |
| Volume profile | Identificar áreas de valor, desequilíbrio, HVN, LVN e zonas de decisão. |
| Leitura de player | Inferir atuação institucional com linguagem probabilística e evidencial. |
| Microestrutura | Entender qualidade do movimento, iniciativa, responsividade e falhas. |

## Regra mais importante

Nunca afirme intenção oculta com certeza. Este skill deve falar em **comportamentos compatíveis com absorção, distribuição, defesa ou aceitação**, e não em certeza sobre o que um participante específico fará em seguida.

## Fluxo de análise

### 1. Confirmar quais dados existem

Primeiro, determine o que está disponível: volume agregado, VWAP, volume profile, tape, book, delta, footprint, mercado à vista, futuro, ETF ou apenas preço e volume simples.

| Disponibilidade de dado | Como adaptar a análise |
| --- | --- |
| Dados ricos de fluxo | Fazer leitura mais direta de absorção, agressão e aceitação. |
| Apenas preço e volume | Inferir qualidade do movimento de forma mais conservadora. |
| Sem volume confiável | Reduzir escopo e evitar narrativa de player. |

### 2. Ler o processo de leilão

Pergunte onde o mercado está fazendo negócio com conforto e onde está escapando rápido. Áreas de negociação confortável costumam concentrar valor; áreas atravessadas com velocidade tendem a indicar rejeição ou desequilíbrio.

### 3. Avaliar iniciativa versus resposta

Diferencie movimentos de iniciativa dos movimentos responsivos.

| Tipo | Sinal típico |
| --- | --- |
| Iniciativa | Mercado rompe, aceita fora do valor e continua. |
| Responsivo | Mercado testa extremo e rejeita, retornando ao equilíbrio. |

Essa distinção evita confundir rompimento verdadeiro com leilão mal sucedido.

### 4. Integrar VWAP e perfil de volume

Use VWAP como referência de posicionamento médio do dia e volume profile para enxergar onde o mercado considerou preço justo ou injusto.

| Ferramenta | Leitura disciplinada |
| --- | --- |
| VWAP | Acima com aceitação favorece controle comprador; abaixo com aceitação favorece controle vendedor. |
| HVN | Área de negociação aceita, com memória de mercado. |
| LVN | Área de passagem rápida, boa para monitorar aceleração ou rejeição. |
| Value area | Região de preço justo relativo dentro do período analisado. |

### 5. Procurar sinais de absorção, exaustão e falha

Descreva absorção quando houver ataque repetido sem progresso compatível. Descreva exaustão quando houver deslocamento com perda de continuidade. Descreva falha quando o mercado romper e não conseguir permanecer fora da área rompida.

### 6. Conectar microestrutura à decisão

A leitura final deve dizer se há continuação provável, reversão responsiva, armadilha, defesa de nível ou mercado sem vantagem clara.

## Padrão de saída

| Bloco | Conteúdo |
| --- | --- |
| Dado disponível | O que pode e o que não pode ser inferido. |
| Contexto de leilão | Equilíbrio, desequilíbrio, aceitação ou rejeição. |
| Evidências de fluxo | Volume, resposta em extremos, comportamento em VWAP e perfil. |
| Leitura de participantes | Linguagem probabilística sobre iniciativa e defesa. |
| Implicação operacional | Continuação, reversão, neutralidade ou risco de armadilha. |

## Boas práticas

Sempre explique o grau de confiança da leitura. Se os dados forem parciais, diga explicitamente que a análise está baseada em indícios indiretos. Se o usuário pedir “fluxo institucional” sem dataset apropriado, seja honesto sobre a limitação e complemente com preço, volume e contexto.

## Limites

Este skill não substitui dados proprietários de mesa, não enxerga intenção real de participante específico e não deve transformar narrativa de fluxo em certeza operacional sem confirmação de preço.
