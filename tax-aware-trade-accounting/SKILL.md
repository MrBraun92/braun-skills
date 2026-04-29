---
name: tax-aware-trade-accounting
description: Organiza custo médio, ganhos e perdas por trade no padrão Receita Federal BR. Calcula IR sobre Day Trade (20%) e Swing Trade (15%), aplica isenção mensal de R$ 20k em swing, gera resumo para DARF mensal e IRPF anual. NÃO substitui contador. Aciona quando o usuário pergunta sobre IR, DARF, isenção, declaração, IRPF de trading.
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo". Esta skill é organizacional — não substitui contador habilitado, especialmente para situações complexas.

# Tax-Aware Trade Accounting

Esta skill organiza a parte fiscal do trader retail brasileiro. A Receita Federal exige cálculo mensal de IR sobre operações em bolsa, com regras distintas entre Day Trade (DT) e Swing Trade (ST), isenção de R$ 20.000 em swing apenas para mercado à vista de ações, alíquotas diferentes, controle de prejuízo acumulado para compensação. Trader retail tipicamente erra esses cálculos — paga DARF a maior, perde compensação de prejuízo, ou esquece de declarar e leva multa. Esta skill **organiza**, calcula DARF mensal e prepara dados para declaração anual (IRPF). Não substitui contador para casos complexos (alavancagem alta, opções estruturadas, carteira mista BR + exterior, fundos exclusivos).

## Quando usar esta skill
- Final de mês, calcular DARF até último dia útil do mês seguinte.
- Janeiro / fevereiro, antes de declarar IRPF do ano anterior.
- Após mudança de regime (começou a operar opções, FIIs, exterior).
- Para auditar cálculo da própria corretora (corretora envia nota de DARF, mas é orientação — responsabilidade é do contribuinte).
- Antes de fazer trade grande para entender impacto fiscal.

## Metodologia

### Etapa 1: Coletar dados
Pedir ao usuário:
- Notas de corretagem do mês (PDF, CSV ou export da corretora).
- Saldo de prejuízo acumulado (ST e DT separados — não se compensam entre si).
- Custo médio atual de cada posição (necessário para calcular ganho).
- Operações classificadas: ST ou DT.
- Mercado: ações, FIIs, opções, ETFs, BDRs, futuros (índice, dólar).

### Etapa 2: Classificar cada operação
- **Day Trade (DT)**: compra e venda do mesmo ativo no mesmo dia, mesma conta. Alíquota 20% sobre lucro líquido mensal. **Sem isenção de R$ 20k**.
- **Swing Trade (ST)**: posição mantida por mais de um dia. Alíquota 15% sobre lucro líquido mensal. **Com isenção** se vendas brutas em ações no mês ≤ R$ 20.000 (apenas ações; FII e ETF não têm isenção).

Atenção:
- **FII**: ganho na venda 20% (igual DT, não importa o tempo). Rendimento mensal isento de IR para PF (com condições).
- **ETF de ações**: 15% ganho de capital. **Sem isenção** dos R$ 20k.
- **BDR**: ganho 15%. **Sem isenção** dos R$ 20k. Ganho > R$ 35k/mês de aplicações no exterior tributa.
- **Opções**: 15% (swing) ou 20% (day). Exercício é evento tributável.
- **Futuros (mini-índice, mini-dólar)**: 15% (operação comum), 20% (day trade).
- **Cripto**: ganho > R$ 35k/mês paga 15% (até R$ 5 mi). Apuração própria.

### Etapa 3: Calcular custo médio
Para cada ativo:
- Custo médio = (qtd anterior × custo médio anterior + qtd comprada × preço comprado + custos de corretagem proporcionais) / (qtd anterior + qtd comprada).
- Atualizar a cada compra. Venda **não** altera custo médio (apenas reduz quantidade).

Custos da corretagem entram no custo médio (na compra) ou reduzem ganho (na venda). IR de fonte (0,005% ST, 1% DT) reduz IR a pagar.

### Etapa 4: Apurar ganho mensal
Para cada categoria (ST e DT separadamente):
- Soma de ganhos brutos do mês.
- Subtração das perdas do mês.
- Subtração dos custos (corretagem, emolumentos, IR de fonte).
- Resultado = ganho líquido mensal.

Se resultado negativo, é prejuízo — vai para saldo acumulado para compensar nos próximos meses (mesmo regime: DT compensa DT; ST compensa ST).

### Etapa 5: Aplicar isenção de R$ 20k
Apenas em ST de ações (não FII, não ETF, não BDR):
- Soma das **vendas brutas** do mês em ações ST.
- Se ≤ R$ 20.000: ganho do mês isento de IR.
- Se > R$ 20.000: tributa o ganho inteiro (não só o excedente). Pegadinha clássica.

### Etapa 6: Compensar prejuízo acumulado
Se há saldo de prejuízo:
- Reduzir ganho líquido tributável do mês até zerar o ganho ou o prejuízo.
- Saldo restante de prejuízo continua acumulado para meses seguintes.
- ST compensa ST. DT compensa DT. Não se misturam.

### Etapa 7: Calcular DARF
- IR devido = ganho tributável × alíquota (15% ST, 20% DT).
- Subtrair IR de fonte retido (0,005% ST, 1% DT) já recolhido pela corretora.
- DARF = IR devido - IR fonte (mínimo R$ 10; abaixo disso vira saldo para meses seguintes).
- **Vencimento**: último dia útil do mês seguinte ao da operação.
- Código DARF: 6015 (PF, ganho líquido em renda variável).

### Etapa 8: Preparar IRPF anual
Dados que vão na declaração:
- **Bens e Direitos**: cada ativo no fim do ano (a custo médio, não a preço de mercado).
- **Rendimentos isentos**: dividendos, JCP (com IRRF retido), rendimentos de FII, lucros e dividendos de SA.
- **Rendimentos sujeitos a tributação exclusiva**: JCP (já tributado na fonte 15%).
- **Renda variável**: ganhos mensais por categoria (mês a mês).
- **Operações em bolsa**: detalhe por mercado, lucro/prejuízo mensal.
- **Comuns**: livro-caixa não é necessário para PF, mas memória de cálculo deve ser guardada por 5 anos.

### Etapa 9: Sinalizar situações complexas
Recomendar contador para:
- Alavancagem (margem, BTC tomado).
- Operações com derivativos estruturados (collar, ratio, condor).
- Carteira mista BR + exterior (declaração de bens no exterior, ITR exterior).
- Posições > R$ 5 mi.
- Sucessão / herança / doação envolvendo ativos financeiros.
- Atividade habitual em volume que possa caracterizar PJ de fato.

## Formato de saída

**Mensal (DARF)**:
```markdown
# Apuração mensal — [mês/ano]

## Resumo
- Operações ST: N (total R$ ...)
- Operações DT: N (total R$ ...)
- Vendas ST de ações: R$ ... [isenção aplicável: sim / não]

## Swing Trade — Ações à vista
| Ativo | Compra (R$) | Venda (R$) | Ganho/perda | Custos |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

- Ganho líquido ST ações: R$ ...
- Aplicação de isenção (vendas ≤ R$ 20k): sim / não
- Ganho tributável ST ações: R$ ...
- Compensação de prejuízo ST: R$ ...
- Base de cálculo final ST ações: R$ ...
- Alíquota: 15%
- IR devido: R$ ...
- IR de fonte retido: R$ ...
- DARF a pagar (ST ações): R$ ...

## Swing Trade — FII
[mesma estrutura, sem isenção, alíquota 20%]

## Swing Trade — ETF / BDR
[mesma estrutura, sem isenção, alíquota 15%]

## Day Trade
[mesma estrutura, alíquota 20%, sem isenção]

## Total DARF do mês
- Código: 6015
- Valor: R$ ...
- Vencimento: [último dia útil do mês seguinte]

## Saldos acumulados ao fim do mês
- Prejuízo acumulado ST: R$ ...
- Prejuízo acumulado DT: R$ ...
```

**Anual (IRPF)**:
```markdown
# Resumo IRPF — Ano [YYYY]

## Bens e Direitos (em 31/dez)
[lista por ativo, valor a custo médio]

## Rendimentos isentos
- Dividendos recebidos: R$ ...
- JCP líquido recebido: R$ ...
- Rendimentos FII isentos: R$ ...

## Rendimentos sujeitos a tributação exclusiva
- JCP bruto recebido (com IRRF 15%): R$ ...

## Renda variável — Operações comuns (ações, FII, ETF, BDR)
| Mês | Ganho líquido (R$) | DARF pago (R$) |
|---|---|---|
| Jan | ... | ... |
| ... | ... | ... |

## Renda variável — Day trade
[mesma estrutura]

## Memória de cálculo
- Isenção mensal (R$ 20k) aplicada em [meses].
- Prejuízo acumulado ao fim do ano: ST R$ ..., DT R$ ...
```

## Checklist de qualidade
- [ ] DT e ST separados.
- [ ] Isenção R$ 20k só aplicada em ST de ações à vista.
- [ ] Prejuízo acumulado controlado por categoria.
- [ ] IR de fonte abatido do DARF.
- [ ] FII com regra própria (rendimento isento, ganho 20%).
- [ ] BDR e ETF sem isenção.
- [ ] Custo médio atualizado corretamente.
- [ ] Sinalização de situações complexas que pedem contador.

## Notas para o assistente
- **Esta skill é organizacional, não jurídica.** Trader com dúvida específica vai a contador habilitado.
- **Receita muda regras**: norma de cripto (IN 1.888) e tributação no exterior (Lei 14.754/23, "come-cotas" para offshore) mudaram recentemente. Verificar última versão.
- **Trader habitual em volume alto**: Receita pode reclassificar como atividade empresarial. Questão jurídica.
- **DARF atrasado**: multa 0,33% ao dia + Selic. Cobre até a data de pagamento.
- **Operação não declarada vs imposto não pago**: ambos geram problema, mas a primeira é mais grave (omissão).
- **Conecta com**: `trade-journal-postmortem` (dado de cada trade), `portfolio-risk-manager` (custo médio atual), `position-sizing-simulator` (sizing pós-IR).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo". Esta skill é organizacional — não substitui contador habilitado para situações complexas.
