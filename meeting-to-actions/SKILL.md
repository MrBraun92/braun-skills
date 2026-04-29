---
name: meeting-to-actions
description: Recebe transcrição ou áudio de reunião e devolve estrutura acionável — decisões tomadas, próximos passos com responsável e prazo, dúvidas em aberto, contexto. Output pronto para colar em Slack, e-mail ou Notion. Aciona quando o usuário pede "ata", "resumo da call", "action items", "tarefas da reunião".
---

# Meeting to Actions

Esta skill transforma transcrição bruta de reunião em um documento operacional — não é ata formal exaustiva, é o briefing que faz a próxima ação acontecer. Foco em decisões, donos e prazos. Substitui aquele momento pós-call em que ninguém anota nada e na semana seguinte ninguém lembra do que foi combinado. Funciona em PT-BR (default) ou EN, dependendo do idioma da reunião.

## Quando usar esta skill
- Pós-call de cliente, parceiro ou equipe interna.
- Reunião com orientador da tese ou banca.
- Reunião 1:1 onde foram combinados próximos passos.
- Reunião de sócio / co-fundador / fornecedor sobre projeto em andamento.
- Brainstorm em grupo que precisa virar plano de ação.

## Metodologia

### Etapa 1: Higienizar a transcrição
Se a transcrição vier crua, primeiro acionar (mentalmente ou explicitamente) `transcript-fixer` para ter um texto legível. Sem texto legível, decisões e ações ficam difusas.

### Etapa 2: Identificar participantes e papéis
Liste quem estava na reunião e qual o papel funcional de cada um (cliente, fornecedor, time, orientador, etc.). Isso afeta a quem atribuir ação. Se não souber, marque `[verificar]`.

### Etapa 3: Extrair decisões tomadas
Decisão = mudança concreta no que será feito. Marcadores típicos:
- "Vamos seguir com X."
- "Decidido que..."
- "Combinado..."
- Tom de fechamento de tópico: "Beleza, então fica assim."

Para cada decisão, capture:
- O que foi decidido (uma frase).
- Quem participou da decisão.
- Pressuposto / contexto crítico para entender a decisão depois.

### Etapa 4: Extrair próximos passos (action items)
Cada action item precisa de **três campos obrigatórios**:
- **Ação**: verbo + objeto, frase curta. ("Enviar proposta revisada")
- **Dono**: nome da pessoa. Nunca "alguém" ou "o time".
- **Prazo**: data concreta ou "até a próxima call em DD/MM".

Marcadores típicos de ação: "fica com você", "vou fazer", "até [data]", "preciso de [coisa] até".

Se faltar dono ou prazo na fala, marque `[Dono?]` ou `[Prazo?]` — não invente. Sinalize no fim do output que esses campos precisam ser confirmados.

### Etapa 5: Extrair dúvidas em aberto
Dúvidas = perguntas que ficaram sem resposta na reunião e precisam ser respondidas para destravar ações. Não confunda com ações ("checar X" é ação, "ainda não sabemos qual o impacto de X" é dúvida).

### Etapa 6: Extrair contexto / observações
Trechos importantes que não viram decisão nem ação mas vale registrar:
- Mudança de tom de cliente.
- Risco mencionado.
- Restrição revelada (orçamento, prazo, jurídico).
- Insight ou ideia para revisitar depois.

### Etapa 7: Formatar e revisar
Saída em Markdown estruturado pronta para colar. Se for para Slack, sugira versão condensada como bloco final.

## Formato de saída

```markdown
# Reunião — [tópico] — [data]

**Participantes:** Nome (papel), Nome (papel), ...
**Duração:** X min
**Idioma:** PT-BR | EN

## Decisões
1. [decisão concreta] — contexto: [1 linha].
2. ...

## Próximos passos
| # | Ação | Dono | Prazo |
|---|------|------|-------|
| 1 | Enviar proposta revisada | Oliver | 02/05 |
| 2 | Confirmar disponibilidade da sala | [Dono?] | 30/04 |

## Dúvidas em aberto
- [pergunta 1] — quem pode responder: [nome]
- [pergunta 2]

## Contexto / observações
- [observação relevante 1]
- [risco ou restrição mencionada]

## Versão Slack (cole direto)
> Resumo da call de hoje: [3 linhas].
> Ações principais: 1) [...] 2) [...]. Dúvidas em aberto: [...].

---
<!-- Itens com [Dono?] ou [Prazo?] precisam de confirmação antes de virar tarefa real. -->
```

## Checklist de qualidade
- [ ] Toda ação tem dono e prazo (ou sinaliza como `[?]`).
- [ ] Decisões são distinguidas de ações (decisão = mudança de rumo, ação = trabalho a fazer).
- [ ] Nomes dos participantes corretos (não inventar).
- [ ] Dúvidas em aberto não viraram ações por engano.
- [ ] Versão Slack tem no máximo 5 linhas e é colável direto.
- [ ] Datas no formato BR (DD/MM) por default; EN-style (MM/DD) só se a reunião foi em inglês.

## Notas para o assistente
- **Quando o usuário disse "X fica responsável" mas não disse prazo**, marque `[Prazo?]` — é mais útil saber que falta prazo do que inventar um.
- **Não invente decisões**: se a reunião foi exploratória sem fechamento, o output é "Sem decisões formais nesta reunião — discussão exploratória" e a seção de ações fica vazia. É honesto.
- **Reuniões longas (>60 min)**: agrupe ações por tópico antes de listar.
- **Reunião com orientador de tese**: dê peso extra a "feedback recebido" como contexto separado das ações.
- **Cliente B2B**: distinga ações do nosso lado vs ações do lado do cliente — formato `Oliver — ação` vs `Cliente — ação`.
- **Confidencial**: se a reunião envolve dados sensíveis (jurídico, RH, salários), avise o usuário antes de gerar versão Slack que poderia vazar.
