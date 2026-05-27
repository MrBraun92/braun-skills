---
name: economic-calendar-prep
description: Monta agenda da semana com eventos macro relevantes (Copom, FOMC, payroll, CPI, IBC-Br). Para cada evento: expectativa de consenso, sensibilidade do mercado, ação operacional sugerida (reduzir tamanho? esperar? operar normal?). Aciona quando o usuário pede "agenda da semana", "calendário macro", "o que vai sair essa semana", em domingos / segundas de manhã.
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Economic Calendar Prep

Esta skill prepara o trader para a semana operacional sob a ótica do calendário macro. Não basta saber que tem FOMC quarta — precisa saber qual o consenso, qual o range de surpresa que o mercado tipicamente reage, e o que isso implica para sizing e timing dos trades. Trader retail tipicamente é pego de surpresa por payroll de sexta ou Copom de quarta. Esta skill produz **briefing de uma página** que o trader lê domingo à noite ou segunda de manhã, e fica preparado.

## Quando usar esta skill
- Domingo à noite ou segunda de manhã, antes da semana operacional.
- Antes de decidir sizing semanal de trades.
- Antes de viajar ou se ausentar — saber o que pode mexer com o portfólio.
- Em conjunto com `weekly-review` (sexta) para fechar a semana e abrir a seguinte.

## Metodologia

### Etapa 1: Coletar agenda da semana
Fontes típicas:
- Boletim Focus (BC Brasil) — segunda de manhã.
- Calendário do Investing.com / Bloomberg / TradingEconomics filtrado por relevância e país (BR + US).
- Site do BC Brasil (Copom, atas, IPCA).
- Site do BLS (US: payroll, CPI), BEA (GDP), ISM.
- Site do IBGE (BR: IPCA, PIB, atividade).

Filtrar para eventos com **alta sensibilidade de mercado** (3 estrelas no calendário típico). Eventos baixos (PMI menor, dado de país periférico) ficam de fora ou em apêndice.

### Etapa 2: Para cada evento — capturar 5 dados
1. **Data e hora** (BRT).
2. **Evento**: nome exato.
3. **Período de referência** (ex: "CPI EUA março").
4. **Consenso** de mercado.
5. **Leitura anterior**.

### Etapa 3: Mapear sensibilidade do mercado
Para cada evento, classificar sensibilidade típica:
- **Crítica** (FOMC, Copom, payroll, CPI EUA): mexe IBOV, juros, câmbio e ações em segundos.
- **Alta** (IPCA BR, ISM, retail sales US, atas): mexe juros e câmbio fortemente.
- **Média** (atividade industrial, balança comercial, confiança): mexe setores específicos.
- **Baixa** (dados secundários): provoca movimento em ativos específicos.

### Etapa 4: Identificar surpresas plausíveis
Para cada evento crítico:
- Qual a janela de surpresa típica? (ex: payroll: consenso 200k, surpresa relevante > +50k ou < -50k).
- O que mercado precificaria em cada cenário?

Não prever direção — mapear cenários "se vier acima, X tende a acontecer; se abaixo, Y".

### Etapa 5: Sugerir postura operacional
Para cada evento crítico, sugerir:
- **Antes**: reduzir tamanho? Não abrir nova posição? Operar normal?
- **Durante**: ficar de fora dos primeiros minutos pós-release.
- **Depois**: aguardar 30-60 min para o spike inicial passar antes de operar?

Padrões clássicos:
- **FOMC** quarta-feira 15h00 BRT: nada de novo trade após 14h00. Posições existentes com hedge ou reduzidas.
- **Copom** quarta noite: viés do comunicado é o que move, não a decisão (geralmente já precificada).
- **Payroll** sexta 09h30 BRT: alta volatilidade nos primeiros 15 min. Spread amplia.
- **CPI EUA** quarta 09h30 BRT (mês intermediário): mexe DI, dólar e ações de tecnologia.

### Etapa 6: Cruzar com posições existentes
Se o usuário compartilhou portfólio:
- Quais posições têm sensibilidade direta a cada evento?
- Ex: posição em pré-fixado é sensível a IPCA. Posição em consumo doméstico é sensível a Selic. Posição em mineradora é sensível a China PMI.

Sinalizar concentração de risco em torno de evento específico.

### Etapa 7: Sumarizar em uma página
Output deve caber em uma tela. Trader não vai ler 10 páginas domingo à noite.

## Formato de saída

```markdown
# Agenda Macro — Semana de [DD/MM] a [DD/MM]

## Eventos críticos
| Dia | Hora | Evento | Anterior | Consenso | Sensibilidade |
|---|---|---|---|---|---|
| Qua | 15:00 | FOMC | 5,50% | 5,25% | 🔴 Crítica |
| Qua | 18:30 | Copom | 10,75% | 10,50% | 🔴 Crítica |
| Sex | 09:30 | Payroll EUA | +220k | +185k | 🔴 Crítica |

## Eventos de alta sensibilidade
| Dia | Hora | Evento | Anterior | Consenso |
|---|---|---|---|---|
| Ter | 09:00 | IPCA março BR | +0,16% | +0,30% |
| Qui | 09:30 | CPI core EUA | +0,3% MoM | +0,3% MoM |

## Cenários para eventos críticos

### FOMC (qua 15h00)
- Cenário base (consenso): corte 0,25pp → mercado provavelmente neutro (já precificado).
- Surpresa hawkish (manter taxa): DXY+, US10Y+, S&P-, IBOV-.
- Surpresa dovish (corte 0,50pp): DXY-, US10Y-, S&P+, IBOV+, ouro+.

### Payroll (sex 09h30)
- Consenso 185k. Janela de surpresa: < 130k ou > 240k.
- Surpresa forte (>240k): hawkish para Fed, US10Y+, S&P-.
- Surpresa fraca (<130k): dovish, S&P+, ouro+.
- Revisão dos meses anteriores tem peso comparável ao número de cabeçalho.

## Postura sugerida (educacional)
- **Quarta**: evitar abrir novos trades após 14h00 BRT (FOMC + Copom no mesmo dia). Posições existentes: avaliar redução.
- **Sexta de manhã**: 09:00 a 10:00 — fora. Spread amplia, slippage alto.
- **Resto da semana**: operação normal, com atenção a IPCA terça e CPI core quinta.

## Cruzamento com portfólio (se aplicável)
- Posição [ATIVO] sensível a Selic — atenção quarta noite.
- Posição [ATIVO] sensível a payroll — atenção sexta de manhã.

## Premissas
- Horários em BRT (UTC-3).
- Consensos do dia [DD/MM] — podem variar até a semana começar.
- Lista filtrada: apenas eventos com sensibilidade média ou superior para BR.
```

## Checklist de qualidade
- [ ] Eventos críticos listados primeiro, alta sensibilidade depois.
- [ ] Cada evento crítico tem cenários (consenso + surpresa em duas direções).
- [ ] Postura operacional sugerida sem usar "compre / venda".
- [ ] Cruzamento com portfólio quando dado disponível.
- [ ] Horários em BRT consistentes.
- [ ] Premissas explícitas no fim.

## Notas para o assistente
- **Não tentar adivinhar direção do release.** Foco em "se A, então X; se B, então Y".
- **Não inventar consenso** se não está na fonte. Marcar `?`.
- **Eventos que cruzam fim de semana** (decisão Fed na quarta + payroll na sexta da mesma semana): risco acumulado. Sinalizar.
- **Releases que são revisão de período anterior** (revisão de payroll, revisão de PIB): podem mover mais que o release de cabeçalho. Não ignorar.
- **Atas** (FOMC e Copom) saem ~3 semanas após a decisão. Tipicamente menos volatilidade, mas pode mover se sinalizar viés diferente.
- **Conecta com**: `macro-economic-analyst` (regime de fundo onde os eventos caem), `weekly-review` (sexta fecha, segunda abre), `portfolio-risk-manager` (cruzamento com posições), `b3-ibov-analyst-br` (impacto setorial).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
