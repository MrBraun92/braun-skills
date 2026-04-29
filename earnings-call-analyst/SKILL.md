---
name: earnings-call-analyst
description: Lê transcrição de teleconferência de resultados (BR ou US) e extrai tom do CEO, mudança de guidance, sinais de risco, pontos de orgulho, e perguntas que analistas evitaram responder. Output estruturado em uma página. Aciona quando o usuário cola transcrição de earnings call ou pede "resumo do call de resultado de [empresa]".
---

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".

# Earnings Call Analyst

Esta skill lê transcrição de teleconferência de resultados (earnings call) e extrai sinais que vão **além dos números reportados**. O release de resultado tem números públicos (lucro, receita, margem); o call tem o que importa de verdade — tom do CEO, ajustes de guidance, palavras evitadas, perguntas duras de analistas, respostas evasivas. Trader retail lê o release e ignora o call. Investidor sofisticado lê o call. Esta skill faz a leitura estruturada que cabe em uma página, em PT-BR, com viés de honestidade radical (não vende a empresa, lê crítica). Funciona para empresas BR e US — basta a transcrição.

## Quando usar esta skill
- Após divulgação de resultado de empresa em que o usuário tem ou está considerando posição.
- Em rodada de earnings (sazonalmente: meados de fevereiro/maio/agosto/novembro para US; abril/julho/outubro/fevereiro para BR).
- Comparando dois trimestres consecutivos da mesma empresa.
- Comparando duas empresas concorrentes que reportaram juntas.
- Para reforçar ou refutar tese de tese existente sobre a empresa.

## Metodologia

### Etapa 1: Verificar inputs
Inputs necessários:
- Transcrição completa (apresentação inicial + Q&A com analistas).
- Release de resultado (pelo menos: receita, lucro, margem, guidance se houver).
- Trimestre referência e comparáveis (Y/Y e Q/Q).
- Empresa, setor, ticker.
- Posição do usuário (comprado, vendido, sem posição, considerando).

### Etapa 2: Ler apresentação inicial (CFO / CEO)
Procurar:
- **Highlight numéricos**: o que a empresa optou por destacar primeiro? Receita? Margem? Cash flow?
- **Palavras vagas**: "challenging", "difícil", "macro", "transitório", "ruído pontual" — todas escondem problema.
- **Mudança de tom em relação ao trimestre anterior**: ficou mais defensivo? mais confiante?
- **Reorganização de KPIs**: trocaram o KPI central? (Sinal forte de que o KPI antigo virou ruim.)
- **Ajustes não-recorrentes**: quantos? Recorrência crescente? "Não-recorrente" todo trimestre é recorrente.
- **Guidance**: manteve, subiu, baixou, retirou? Faixa apertou ou abriu?

### Etapa 3: Ler Q&A com analistas
Dispositivo crítico de análise:
- **Quais analistas estão presentes**? Top sell-side (BTG, Itaú BBA, JPMorgan, Goldman) levam mais peso.
- **Pergunta que repete em vários analistas**: aquilo é o tema do trimestre.
- **Resposta evasiva**: analista pergunta "qual margem do segmento X?", CEO responde "estamos confortáveis com nossa direção operacional" — bandeira vermelha.
- **Analista volta com follow-up agressivo**: tema sensível.
- **Analista sai sem pergunta**: notável quando acontece (significa "eu já sei a resposta e ela não me agrada").
- **CFO contradiz CEO** sutilmente — leia com atenção.
- **CEO entusiasmado em pergunta sobre geração de caixa, defensivo em pergunta sobre dívida**: priorize o sinal defensivo.

### Etapa 4: Identificar mudança de guidance
Tipos de mudança e severidade:
- **Subida de guidance** (raise): tom positivo. Ainda assim, conferir se está acima de consenso ou apenas em linha.
- **Manutenção de guidance**: neutro, mas atenção à credibilidade — se trimestre veio fraco, manter guidance pode ser otimismo forçado.
- **Aperto de faixa**: confiança crescente.
- **Baixa de guidance** (cut): bandeira vermelha forte.
- **Retirada de guidance** ("não comentamos guidance neste momento"): bandeira muito vermelha.
- **Reformulação de KPI**: quase sempre suaviza realidade.

### Etapa 5: Capturar pontos de orgulho e de risco
Listar:
- **3 pontos que a empresa quis destacar** (orgulho).
- **3 sinais de risco** identificados pelo seu próprio julgamento (não pela empresa).

Geralmente os dois conjuntos não se sobrepõem.

### Etapa 6: Tom do CEO
Avaliar tom geral:
- **Confiante e específico**: cita números detalhados, dá exemplos concretos.
- **Confiante e vago**: usa palavras grandes ("transformação", "jornada", "execução"), evita números.
- **Defensivo**: corta perguntas, usa muletas.
- **Cansado / desanimado**: tom plano, sem energia. Pode ser sinal de saída próxima.
- **Novo CEO**: primeiro call dele tem padrão diferente — concentre-se em prioridades anunciadas.

### Etapa 7: Comparar com call anterior
Se tiver acesso:
- O que foi prometido no call anterior foi entregue?
- Mudou alguma narrativa? (Ex: empresa que dizia "foco em margem" virou "foco em volume" — virada estratégica.)
- Métrica que era "principal" virou "secundária"?

### Etapa 8: Sintetizar
Output em uma página, padronizado, com viés crítico (não release oficial, é análise de leitor cético).

## Formato de saída

```markdown
# Earnings Call — [TICKER] — [Trimestre]

## Snapshot
- Receita: R$ ... mi (vs Y/Y: +/- ...%, vs consenso: +/- ...)
- Lucro líquido: R$ ... mi (vs Y/Y: ..., vs consenso: ...)
- Margem operacional: ...% (vs anterior: ...)
- Guidance: [mantido / subiu / baixou / retirado]

## Tom geral do call
**[Confiante específico / Confiante vago / Defensivo / Cansado]** — justificativa em 1-2 linhas.

## Highlights da apresentação (o que a empresa quis destacar)
1. ...
2. ...
3. ...

## Sinais de risco (nossa leitura crítica)
1. [risco — com referência a trecho do call]
2. ...
3. ...

## Q&A — temas dominantes
- **Tema 1**: [N analistas perguntaram sobre]. Resposta: [direta / evasiva]. Sinal: ...
- **Tema 2**: ...

## Perguntas com resposta evasiva
1. [Analista X (Banco Y) perguntou Z. Resposta: parafrasear. Por que evasiva: ...]

## Mudança vs call anterior (se aplicável)
- O que foi prometido: ...
- O que foi entregue: ...
- Narrativa mudou? sim / não. Como: ...

## Guidance
- Anterior: ...
- Atual: ...
- Implicação: ...

## Trecho-chave (quote literal)
> [1 frase do CEO ou CFO que sintetiza o trimestre — citação direta]

## Pontos a monitorar nos próximos 3 meses
- [ ] [ponto 1 — KPI a observar]
- [ ] [ponto 2]
- [ ] [ponto 3]

## Premissas / contexto
- Setor / momento de mercado: ...
- Posição do usuário: comprado / vendido / sem / considerando.
- Ressalva: análise é sobre o tom do call; números do release não foram auditados aqui.
```

## Checklist de qualidade
- [ ] Snapshot numérico antes da análise qualitativa.
- [ ] Tom do CEO classificado em uma das 4 categorias.
- [ ] Pelo menos 3 sinais de risco identificados (independentes da empresa).
- [ ] Q&A analisado, não só apresentação inicial.
- [ ] Pelo menos uma pergunta evasiva flagrada.
- [ ] Mudança de guidance explicitada.
- [ ] Quote literal escolhida para sintetizar tom.
- [ ] Pontos a monitorar listados (acionáveis).

## Notas para o assistente
- **Não vire shill da empresa.** Skill existe para ler crítica. Se tudo está bom, dizer "tudo está bom" — mas não inventar bom.
- **Não vire vendido sistemático.** Se o trimestre foi de fato bom, reconhecer.
- **Tom evasivo no Q&A** é dado mais valioso que número do release. Foco em sinal qualitativo.
- **Empresas BR**: discurso tipicamente mais informal, mais cordial. Padrão de evasão é diferente.
- **Empresas US**: discurso mais ensaiado, IR muito treinado. Sinal aparece em pausa, repetição, mudança de pronoun ("we" vs "I").
- **Setor regulado** (utilities, saúde, financeiro BR): muita coisa fica fora do call por questão regulatória. Atenção a "estamos avaliando alternativas" — frase guarda-chuva.
- **Conecta com**: `b3-ibov-analyst-br` (contexto setorial BR), `equity-fundamental-analyst` (análise fundamentalista mais ampla), `decision-journal` (registrar mudança de tese após call), `trade-journal-postmortem` (validar tese contra release).

> ⚠️ **Disclaimer:** Esta skill produz análise educacional e simulação. NÃO é recomendação de investimento. Decisões de aporte de capital são responsabilidade exclusiva do usuário. Esta skill nunca usa palavras como "compre", "venda", "garantido" ou "certo".
