---
name: risk-regime-portfolio
description: Gestão de risco, regime de mercado e construção de exposição em renda variável. Use para sizing, volatilidade, correlação, assimetria, cenários de perda, proteção, alocação entre teses e adaptação tática ao regime de mercado.
---

# Risk Regime Portfolio

## Visão geral

Use este skill quando a decisão principal não for “qual ativo escolher”, mas **quanto arriscar, em que regime operar, como distribuir exposição e como sobreviver quando a leitura estiver errada**.

Ele cobre sizing, controle de perda, risco por tese, risco agregado, correlação, volatilidade, cenários, concentração e adaptação entre mercado tendencial, lateral, direcional volátil ou regime de stress.

## Quando usar

| Caso | Aplicação |
| --- | --- |
| Position sizing | Definir tamanho coerente com stop, volatilidade e convicção. |
| Regime de mercado | Ajustar agressividade ao ambiente predominante. |
| Portfólio | Evitar concentração invisível e correlação excessiva. |
| Proteção | Estruturar hedge conceitual, caixa ou redução de risco. |
| Revisão de tese | Decidir se deve reduzir, zerar, rebalancear ou manter. |

## Princípios centrais

### Sobreviver vem antes de maximizar

Sem controle de risco, uma tese boa pode virar uma execução ruim. O skill deve tratar risco como variável primária, não como apêndice da análise.

### Regime muda o tamanho da aposta

A mesma setup merece pesos diferentes conforme o ambiente.

| Regime | Ajuste típico |
| --- | --- |
| Tendência limpa | Permite carregar um pouco mais, desde que a invalidação seja clara. |
| Lateralidade | Exige alvo mais disciplinado e menor expectativa de expansão. |
| Alta volatilidade | Pede sizing menor e stop calibrado por amplitude. |
| Stress sistêmico | Prioriza defesa, caixa e redução de correlação. |

### Correlação escondida é risco real

Várias posições diferentes podem, na prática, ser a mesma aposta macro. O skill deve procurar fatores comuns: juros, commodities, câmbio, growth, beta alto, small caps ou dependência de liquidez.

## Fluxo de análise

### 1. Definir a unidade de risco

Primeiro, torne explícito como o risco será medido: percentual do capital, valor financeiro, ATR, desvio padrão, stop estrutural ou perda máxima tolerável por tese.

### 2. Ajustar sizing à qualidade da assimetria

Não aumente posição apenas por convicção subjetiva. Aumente quando houver combinação melhor entre gatilho, invalidação, liquidez, volatilidade e clareza de cenário.

### 3. Mapear risco no nível da carteira

| Camada | O que observar |
| --- | --- |
| Posição | Distância até invalidação, liquidez e gap risk. |
| Conjunto de posições | Correlação entre teses e exposição temática repetida. |
| Carteira total | Drawdown potencial, beta agregado e sensibilidade a choques. |

### 4. Planejar o erro antes da entrada

Toda operação deve responder antecipadamente:

1. Onde a tese deixa de fazer sentido?
2. Quanto custa estar errado?
3. O que fazer se o mercado acelerar contra?
4. Quando reduzir mesmo sem stop formal?

### 5. Rever risco dinamicamente

Risco não é definido uma única vez. Se o mercado muda de regime, se a volatilidade expande ou se correlação aumenta, o tamanho ideal também muda.

## Padrão de saída

| Bloco | Conteúdo |
| --- | --- |
| Regime | Qual ambiente de mercado está vigente. |
| Risco por posição | Tamanho, invalidação e perda esperada. |
| Risco agregado | Concentração, correlação e exposição repetida. |
| Ajuste recomendado | Aumentar, reduzir, manter, proteger ou esperar. |
| Plano defensivo | O que fazer se o cenário piorar. |

## Boas práticas

Sempre prefira linguagem como “risco aceitável para este contexto”, “assimetria piorou” ou “a carteira ficou excessivamente concentrada”, em vez de frases genéricas como “está arriscado”.

Quando o usuário estiver muito focado em retorno potencial, reancore a conversa em perda máxima, sequência de perdas e preservação de capital. Renda variável premia permanência mais do que heroísmo.

## Limites

Este skill não deve mascarar incerteza com precisão falsa. Sizing, hedge e correlação são aproximações práticas, não garantias de proteção perfeita.
