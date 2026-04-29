---
name: weekly-review
description: Conduz a revisão semanal estilo GTD adaptada ao stack do Oliver — passa por projetos abertos (tese, EventPro, trading, social media), pendências, próximas ações. Sai sexta sabendo exatamente o que vem na segunda. Aciona quando o usuário diz "revisão semanal", "fechamento da semana", "weekly review", "o que vem na semana que vem".
---

# Weekly Review

Esta skill é a revisão semanal do Oliver — solopreneur AI que opera múltiplas frentes em paralelo (tese de mestrado UiS, EventPro SaaS, trading de portfólio, presença online, eventual venture novo). Sem revisão semanal estruturada, frentes ficam órfãs, pendências escapam e a segunda começa em modo reativo. Inspirada no método GTD de David Allen, mas adaptada para alguém que **opera sozinho com múltiplos agentes IA** — então pergunta também sobre custo de IA da semana e estado dos workflows automáticos. Tempo-alvo: 30 a 45 minutos toda sexta à tarde.

## Quando usar esta skill
- Sexta à tarde / sábado pela manhã, fechando a semana.
- Final de mês ou trimestre (versão estendida da revisão).
- Voltando de viagem ou pausa longa (versão "catchup").
- Antes de uma virada importante (lançamento, banca de tese, fim de sprint).

## Metodologia

### Etapa 1: Coletar inputs da semana
Antes de começar, junte:
- Commits da semana em cada repo (`git log --since="1 week ago"`).
- E-mails não respondidos.
- Notas avulsas (Apple Notes, Obsidian, Notion daily notes).
- Mensagens de WhatsApp / Slack que viraram tarefa.
- Calendário da semana (o que aconteceu de fato).
- Calendário da semana seguinte (o que está marcado).
- Carteira / posições de trading (rebalance? algum stop ativado?).

### Etapa 2: Passar por cada frente
Para cada projeto / frente ativa, perguntar:
- **O que avançou esta semana?** (fato concreto, com prova — commit, doc, decisão).
- **O que estava planejado e não avançou?** (e por quê).
- **Próxima ação concreta na segunda?** (verbo + objeto).
- **Algum bloqueio?** (precisa de input externo? decisão pendente?).

Frentes default do Oliver (ajustar com o usuário):
1. **Tese de mestrado UiS** — escrita, leitura de papers, reuniões com orientador, deadlines.
2. **EventPro SaaS** — sprint atual, PRs abertos, bugs em produção, próximas features.
3. **Trading** — performance da semana (sem se gabar nem se punir), trades feitos, lições, agenda macro semana seguinte.
4. **Social media / autoridade** — conteúdo publicado, ideias capturadas, engajamento.
5. **Pessoal / vida** — saúde, sono, exercício, relacionamentos, finanças pessoais.

### Etapa 3: Inventário de pendências (Mind Sweep)
Pergunte: "Tem algo na cabeça que não está em nenhuma lista?". Capture absolutamente tudo, sem filtrar — depois classifica. Inclui:
- Compromissos sociais não confirmados.
- Mensagens não respondidas que estão pesando.
- Pequenas tarefas administrativas (banco, contador, médico, IRPF, DARF).
- Ideias soltas que querem virar projeto.
- Coisas que precisam ser delegadas.

### Etapa 4: Triagem GTD-style
Para cada item capturado:
- **Acionável agora (<2 min)?** Faça já, não anote.
- **Acionável depois?** Vai para próxima ação com data.
- **Não acionável agora?** Vai para "Aguardando" (esperando alguém) ou "Algum dia" (talvez no futuro).
- **Lixo / fora de jogo?** Descarte explicitamente — ato de fechar.

### Etapa 5: Revisar custo e workflows de IA
Solopreneur AI: a cada semana checar:
- Custo Claude / OpenAI / Manus (rough — `cost-metering` se disponível).
- Workflows automáticos que rodaram sem revisão? Estão fazendo o esperado?
- Skills usadas mais e menos esta semana.
- Algum agente travou ou produziu saída ruim que mereça ajuste no prompt?

### Etapa 6: Planejar a próxima semana
- **Top 3 prioridades da semana** — não 7, não 5. Três.
- **Bloqueios de tempo na agenda** — quando vai mexer em cada coisa.
- **O que NÃO vai fazer esta semana** — explicitar para não sentir culpa.
- **Próximo passo claro de cada frente prioritária**.

### Etapa 7: Fechar com lições
- Uma coisa que funcionou bem esta semana — replicar.
- Uma coisa que não funcionou — ajustar.
- Uma decisão que vale registrar formalmente (use `decision-journal`).

## Formato de saída

```markdown
# Revisão Semanal — [data fechamento]

## Frentes
### Tese UiS
- Avançou: ...
- Não avançou: ...
- Próxima ação: ...
- Bloqueio: ...

### EventPro
- Avançou: ...
- Próxima ação: ...
...

### Trading
- Performance da semana: [neutro, sem viés]
- Trades feitos: N (X day, Y swing)
- Lições: ...
- Agenda macro próxima semana: [link com economic-calendar-prep]

### Social / vida pessoal
- ...

## Mind Sweep
[lista crua, sem filtro]

## Triagem
- Próxima ação: ...
- Aguardando: ...
- Algum dia: ...
- Descartado: ...

## Workflows IA
- Custo aproximado: R$ ...
- Skills mais usadas: ...
- Ajuste necessário: ...

## Plano da próxima semana
1. **Prioridade 1**: ...
2. **Prioridade 2**: ...
3. **Prioridade 3**: ...

NÃO vou fazer esta semana: ...

## Lições
- Funcionou: ...
- Não funcionou: ...
- Decisão a registrar: ...
```

## Checklist de qualidade
- [ ] Toda frente ativa foi tocada (mesmo que para dizer "não avancei").
- [ ] Mind sweep esvaziou a cabeça — nada pendente sem registro.
- [ ] Top 3 da próxima semana estão definidos com clareza.
- [ ] "Não vou fazer" foi explicitado para evitar culpa.
- [ ] Pelo menos uma lição operacional foi capturada.
- [ ] Custo de IA da semana foi olhado mesmo que de leve.

## Notas para o assistente
- **Tempo importa**: 30-45 min é o alvo. Se a sessão ultrapassar uma hora, pare e termine a triagem em outro momento.
- **Não julgue performance**: trading semanal, escrita de tese, código — relatar fatos, não interpretar emoção. Para emoção, use `trader-psychology-coach`.
- **Frentes que estão dormentes**: marque "dormente" explicitamente. Não force atividade.
- **Não inventar próxima ação**: se o usuário não sabe, sinalize "definir próxima ação" como ação em si.
- **Conecta com**: `decision-journal` (decisões da semana), `cost-metering` (custo IA), `economic-calendar-prep` (semana de trading), `continue-work` (segunda de manhã).
- **Versão de fim de mês**: adicionar revisão de OKRs / metas mensais e olhar tendência de 4 semanas em cada frente.
