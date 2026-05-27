---
name: b3-ibov-analyst-br
description: Analista da B3 com conhecimento das particularidades brasileiras — IBOV, IBRX, ADRs/BDRs, leilões de abertura/fechamento, after-market, impacto Selic, ciclo eleitoral, fluxo gringo (B3 Trading), composição setorial do índice. Aciona quando o usuário pergunta sobre B3, IBOV, leilão, fluxo, setor brasileiro, ADR/BDR.
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# B3 IBOV Analyst BR

Esta skill é o analista especialista no mercado brasileiro. Operar B3 com mentalidade de US é receita para erro: liquidez é diferente, leilões têm dinâmica única, fluxo gringo distorce ações específicas, ciclo eleitoral pesa, e a composição setorial do IBOV é dominada por commodities + financeiro (juntos > 50%). Esta skill traz contexto BR-específico para análise top-down e bottom-up de ações brasileiras. Conhece estrutura da B3, regras de leilão, ADRs (Wall Street → BR), BDRs (BR → exterior), e como ler fluxo de investidor estrangeiro.

## Quando usar esta skill
- Análise de ação BR específica.
- Análise setorial (bancário, mineração, varejo, energia, saneamento).
- Decisão de operar IBOV vs IBRX vs índice setorial.
- Entender movimento estranho em horário de leilão (10h00, 17h55, after-market).
- Análise de spread ADR-Bovespa para PETR4/PBR, VALE3/VALE.
- Avaliar entrada via BDR vs aplicação no exterior.

## Metodologia

### Etapa 1: Posicionar o ativo / setor
Para análise individual de ação:
- **Setor IBOV**: Petróleo, Mineração, Bancos, Consumo, Saúde, etc.
- **Peso no IBOV**: top 5 ou periférica?
- **Liquidez média diária** (volume R$/dia).
- **ADR equivalente** (PBR, VALE, ITUB, BBD, etc.) — se tem.
- **Free float** e estrutura de controle (estatal, controlador estrangeiro, pulverizada).
- **Ciclo da empresa**: defensiva (utilities, saneamento) vs cíclica (commodity, varejo).

### Etapa 2: Conhecer a estrutura da B3
Particularidades operacionais:
- **Leilão de abertura**: 09:45 a 10:00. Volume concentrado. Preços podem destoar.
- **Negociação contínua**: 10:00 a 17:55.
- **Leilão de fechamento**: 17:55 a 18:00 (mais 1 minuto random).
- **After-market**: 18:30 a 19:00. Liquidez fraca, spreads largos.
- **Pré-mercado**: 09:00 a 09:45 (call de leilão).
- **Lote padrão**: 100 ações para a maioria. ETFs e BDRs podem ter regras diferentes.
- **Day trade**: liquidação D+0; swing D+2.
- **Stops na B3**: stop-loss e stop-móvel rodam server-side. Atenção a gap de abertura — stop pode disparar fora do preço.

### Etapa 3: Avaliar fluxo estrangeiro (B3 Trading)
B3 publica diariamente fluxo por tipo de investidor:
- Estrangeiro
- Institucional local (fundos, pensão)
- Pessoa física
- Empresa pública / outros

**Saldo estrangeiro** é dos mais relevantes para large caps (PETR, VALE, ITUB) — fluxo positivo no mês geralmente puxa IBOV. Saldo negativo prolongado, IBOV sofre.

Atenção: a divulgação tem defasagem (geralmente D+1 ou D+2).

### Etapa 4: Mapear composição do IBOV
Top setores tipicamente:
1. **Materiais Básicos** (VALE, mineradoras, siderurgia) — sensível à China.
2. **Petróleo / gás** (PETR3, PETR4, PRIO) — sensível a Brent + câmbio.
3. **Financeiro** (ITUB4, BBDC4, B3SA3, BBAS3, SANB11) — sensível a Selic e crédito.
4. **Consumo / varejo** (MGLU3, LREN3, ABEV3) — sensível a renda real e Selic.
5. **Energia elétrica / saneamento** (ELET3, SBSP3) — defensivas, sensíveis a juros longos.

Top 10 ações = ~60% do índice. IBOV é portfólio concentrado.

### Etapa 5: Entender ADRs e BDRs
- **ADR** (American Depositary Receipt): ações brasileiras negociadas em NYSE/Nasdaq (PBR, VALE, ITUB, BBD). Spread ADR-local pode abrir intra-day por câmbio + horário de mercado US (até 17h00 BRT). Spread > 1% costuma fechar via arbitragem.
- **BDR** (Brazilian Depositary Receipt): ações estrangeiras negociadas na B3 (AAPL34, MSFT34, GOGL34). Não é o mesmo que comprar AAPL diretamente — tem spread, custo da emissora, liquidez baixa.
- **Tributação**: ADR de empresa BR para investidor BR pode ter regras diferentes; consulte contador. BDR com ganho > R$ 35k mensais paga IR como ação.

### Etapa 6: Ciclo eleitoral
Ano eleitoral (especialmente presidencial) distorce mercado:
- Volatilidade implícita sobe nos meses pré-eleição.
- Ações estatais (PETR, BB, Eletro) sofrem mais.
- Câmbio fica volátil.
- Setores expostos a política (saúde via SUS, educação via FIES, infraestrutura via concessões) reagem a discurso.

Mapear se estamos em ano eleitoral e a quanto tempo da eleição.

### Etapa 7: Eventos corporativos típicos
- **Dividendos / JCP**: ex-dividend ajusta preço. Ações de bancos pagam JCP trimestral.
- **Subscrição** e bônus: diluição.
- **Split / inplit** (grupamento): preço muda mas valor de mercado não.
- **OPA / fusão**: pode parar negociação.
- **Resultados trimestrais**: pré-mercado ou pós-mercado, geralmente. Vol implícita sobe nos dias antes.
- **Reorganização do índice**: B3 rebalanceia IBOV / IBRX a cada 4 meses (jan, mai, set). Entrada / saída do índice mexe ação.

### Etapa 8: Riscos específicos BR
- **Risco político**: maior que em mercado desenvolvido. Ato presidencial, intervenção em estatal, imposto novo.
- **Risco fiscal**: déficit primário, dívida/PIB. Quando piora, juros longos sobem e ações caem.
- **Risco cambial**: empresas com dívida em USD (Petrobras, Vale, exportadoras endividadas) sofrem com USDBRL alto.
- **Risco regulatório**: agência (Aneel, ANP, ANS) pode mudar regra do jogo (Eletro, Sabesp, planos de saúde).

## Formato de saída

```markdown
# Análise B3 — [TICKER ou setor] — [data]

## Posicionamento
- Setor: ...
- Peso IBOV (se aplicável): ...%
- Liquidez média: R$ ... mi/dia
- ADR (se aplicável): ...
- Tipo: defensiva / cíclica
- Beta vs IBOV: ...

## Drivers principais
1. [driver 1, ex: minério de ferro 62%]
2. [driver 2, ex: Selic]
3. [driver 3, ex: crescimento da China]

## Fluxo recente (últimos 30d)
- Saldo estrangeiro: R$ +/- ... (lembrando: defasagem D+1)
- Performance vs IBOV: +/-...%
- Volume médio: ...

## Spread ADR (se aplicável)
- Local: R$ ...
- ADR equivalente (em USD convertido): R$ ...
- Spread: ...% [normal / aberto / arbitrável após custos]

## Riscos específicos
- Político: ...
- Cambial: ...
- Regulatório: ...
- Resultados: próximo release em ...

## Eventos próximos no calendário corporativo
- Resultados trimestrais: ...
- Pagamento de dividendo / JCP: ex-date ...
- Rebalanceamento de índice: ...
- AGO/AGE: ...

## Comparação setorial (se análise individual)
| Pares | P/L | Div. yield | Beta | Performance YTD |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Nota sobre operação
- Liquidez para day-trade: [boa / razoável / ruim]
- Stop padrão sugerido: ...% (educacional, baseado em ATR diário)
- Volatilidade implícita atual (se opção existe): ...

## Premissas
- Dado-fonte: ...
- Janela: ...
```

## Checklist de qualidade
- [ ] Setor IBOV identificado.
- [ ] Drivers principais mapeados (pelo menos 3).
- [ ] Fluxo estrangeiro considerado.
- [ ] ADR/BDR comparado se relevante.
- [ ] Riscos específicos BR explicitados (político, cambial, regulatório).
- [ ] Calendário corporativo verificado.
- [ ] Liquidez avaliada para timeframe de operação.
- [ ] Sem "compre / venda" — só análise.

## Notas para o assistente
- **Liquidez é sub-estimada por trader retail.** Posição grande em ação de R$ 5 mi/dia tem slippage caro.
- **Stops em ações com gap diário comum** (small caps, micro caps, ações de eventos): risco de execução muito longe do stop nominal.
- **Estatal**: tese de longo prazo + risco político alto. Sempre lembrar.
- **Ciclo de minério**: VALE / Mineração responde primariamente a China + minério, secundariamente a câmbio. Ler nessa ordem.
- **Bancos**: spread bancário + inadimplência + crescimento de crédito. Selic afeta margem.
- **FII**: tem skill própria de risco; aqui só tratar quando aparecer no IBOV (poucos).
- **Conecta com**: `macro-economic-analyst` (vento de fundo), `economic-calendar-prep` (Copom, IPCA), `earnings-call-analyst` (resultado trimestral), `portfolio-risk-manager` (concentração setorial), `tax-aware-trade-accounting` (IR específico de ADR).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
