---
name: decision-journal
description: Registra decisões importantes com hipótese, opções consideradas, critério de sucesso e prazo de revisão. Volta em datas marcadas para confrontar a decisão com o resultado real, ajudando o usuário a aprender com erros próprios em vez de esquecê-los. Aciona quando o usuário diz "decidi", "vou seguir com", "estou em dúvida entre", "registra essa decisão", ou pede para revisar uma decisão antiga.
---

# Decision Journal

Esta skill é o diário de decisões do Oliver — solopreneur que toma decisões grandes (produto, finanças, carreira, trades, tese) sozinho e sem feedback estruturado. Inspirado em Annie Duke (*Thinking in Bets*) e em decision logs corporativos. Cada entrada captura **o estado mental no momento da decisão** — não para julgar depois, mas para distinguir decisão boa com resultado ruim (azar) de decisão ruim com resultado bom (sorte). Sem isso, o aprendizado é distorcido pelo viés de retrospectiva.

## Quando usar esta skill
- Decisão de produto importante (entrar em sprint X, cortar feature Y, mudar arquitetura).
- Decisão de negócio (contratar, demitir, fechar contrato, recusar cliente, mudar pricing).
- Decisão de trading que vale revisar depois (entrada grande, sizing fora do padrão, mudar tese).
- Decisão pessoal estruturada (carreira, mudança de país, parceria, virada de stack).
- Quando o usuário pede para revisitar uma decisão antiga ("dei conta da revisão de 90 dias?").

## Metodologia

### Etapa 1: Capturar o contexto da decisão
Pergunte ou peça que o usuário descreva:
- **Decisão**: uma frase. ("Vou entrar em posição de 5% do portfólio em VALE3.")
- **Data**: hoje (ou explícita).
- **Categoria**: produto / negócio / trading / pessoal / carreira / tese.

### Etapa 2: Capturar a hipótese
Pergunte: "Por que você acredita que essa decisão vai dar certo?"
Capture:
- Hipótese principal (uma frase).
- Pressupostos críticos (3 a 5 bullets — coisas que precisam ser verdade).
- Confiança subjetiva (% ou baixa/média/alta).

### Etapa 3: Capturar opções consideradas e descartadas
Pelo menos duas alternativas que foram consideradas e por que foram descartadas. Decisão "única opção" geralmente é decisão mal pensada. Se o usuário só enxergou uma opção, force a pergunta: "E se você não fizer nada?" "E se fizer o oposto?".

### Etapa 4: Definir critério de sucesso e fracasso
**Antes de saber o resultado**, definir:
- Sucesso: que indicador objetivo, em que prazo? ("Em 90 dias, ROI positivo de pelo menos 8%.")
- Fracasso: o que faz desistir? ("Drawdown de 15% ou mudança de tese fundamental.")

Sem critério pré-definido, o usuário racionaliza qualquer resultado depois — vies de retrospectiva clássico.

### Etapa 5: Definir prazo de revisão
Quando voltar para olhar essa decisão? Default:
- Trading: 30 ou 90 dias (depende do horizonte do trade).
- Produto: 60 a 90 dias.
- Carreira / pessoal: 6 a 12 meses.

Marque o prazo. Idealmente o usuário coloca em calendário na hora.

### Etapa 6: Registrar
Salvar a entrada em formato estruturado (ver "Formato de saída"). Sugerir local persistente: arquivo `docs/decisions/YYYY-MM-DD-titulo-curto.md` em repo Git, Notion, ou pasta Obsidian.

### Etapa 7: Revisitar (uso secundário)
Quando o usuário diz "vamos revisar a decisão X de janeiro":
- Recupere a entrada original.
- Pergunte resultado real (sem julgar).
- Confronte com critério pré-definido.
- Classifique:
  - Decisão boa + resultado bom → confirmar processo.
  - Decisão boa + resultado ruim → azar; manter processo, ajustar variável que falhou.
  - Decisão ruim + resultado bom → sorte; ajustar processo apesar do ganho.
  - Decisão ruim + resultado ruim → identificar viés que levou ao erro (ver `trader-psychology-coach` se for trade).
- Documente o aprendizado em campo "Revisão" da entrada original.

## Formato de saída

```markdown
# Decisão: [título curto]

- **Data**: 2026-04-29
- **Categoria**: produto | negócio | trading | pessoal | carreira | tese
- **Decisão**: [uma frase clara — verbo + objeto]
- **Confiança subjetiva**: 70% | baixa/média/alta

## Hipótese
[1 parágrafo]

## Pressupostos críticos
- [pressuposto 1 — precisa ser verdade]
- [pressuposto 2]
- [pressuposto 3]

## Opções consideradas
1. [opção escolhida] — por quê: ...
2. [alternativa A] — descartada porque: ...
3. [alternativa B / não fazer nada] — descartada porque: ...

## Critério de sucesso (antes do resultado)
[indicador objetivo + prazo]

## Critério de fracasso
[o que faz desistir]

## Prazo de revisão
[data concreta — colocar em calendário]

---

## Revisão (preencher na data de revisão)
- **Data da revisão**:
- **Resultado real**:
- **Critério atingido?**: sim | não | parcial
- **Classificação**: decisão boa+resultado bom | boa+ruim | ruim+bom | ruim+ruim
- **Aprendizado**:
- **Mudança de processo a aplicar nas próximas decisões similares**:
```

## Checklist de qualidade
- [ ] Decisão tem uma frase clara, não vaga ("vou pensar sobre" não é decisão).
- [ ] Hipótese é falsificável (algo pode provar que ela está errada).
- [ ] Pelo menos duas alternativas foram consideradas.
- [ ] Critério de sucesso é objetivo, não emocional.
- [ ] Prazo de revisão tem data concreta.
- [ ] Confiança subjetiva foi capturada (mesmo que aproximada).

## Notas para o assistente
- **Não julgue a decisão na hora do registro.** Esta skill captura o estado mental, não opina.
- **Na revisão**, foco no processo, não no resultado. "Você poderia ter sabido?" é uma pergunta melhor que "deu certo?".
- **Para decisões de trading**, conecte com `trade-journal-postmortem` e `trader-psychology-coach`.
- **Decisões reversíveis vs. irreversíveis**: para irreversíveis (Bezos chamou "Type 1"), force o rigor — mais opções consideradas, mais pressupostos explicitados, prazo de revisão mais longo.
- **Não force decisão precoce**: se o usuário ainda está coletando dados, sugira voltar quando a hipótese estiver mais clara, em vez de registrar uma decisão fraca.
- **Revisitar decisões antigas é a parte mais valiosa**: incentive o usuário a olhar o calendário e fazer a revisão na data marcada, mesmo que demore 5 minutos.
