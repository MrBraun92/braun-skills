---
name: cost-metering
description: Monitora custo e tempo de workflows de IA do usuário — aceita logs de uso de Claude, OpenAI e Manus, identifica skills queimando tokens à toa, sugere otimização de prompt, projeta custo mensal. Aciona quando o usuário pergunta "quanto gastei", "qual skill consome mais", "fatura Anthropic / OpenAI", ou pede revisão de custo de IA.
---

# Cost Metering

Esta skill é o controle financeiro do solopreneur AI. O Oliver opera Claude, GPT-4 e Manus em paralelo, com múltiplos agentes rodando em background, skills automáticas e workflows agendados. Sem instrumentação, dá para queimar centenas de dólares em um mês sem perceber — e pior, sem saber qual workflow é o vilão. Esta skill recebe logs de uso (CSV exportado da Anthropic Console, OpenAI usage page, ou logs do Manus), identifica os maiores consumidores e sugere ajustes concretos. Pensada para alguém que **não é DevOps** mas precisa entender ROI de cada skill / workflow.

## Quando usar esta skill
- Final do mês, antes da fatura virar — projetar e ajustar.
- Suspeita de pico ("essa semana parece cara").
- Antes de colocar workflow novo em loop automático — projetar custo no longo prazo.
- Decisão de migrar workflow de Opus para Sonnet ou Haiku.
- Auditoria trimestral de stack de IA.

## Metodologia

### Etapa 1: Coletar dados de uso
Pedir ao usuário um ou mais dos seguintes:
- CSV exportado de console.anthropic.com (Settings → Usage).
- CSV de platform.openai.com (Usage → Export).
- Logs do Manus (formato varia — peça print ou export).
- Histórico manual: lista de tarefas grandes ("rodei 30 vezes a skill X esta semana").
- Para Claude Code local: `~/.claude/usage.jsonl` ou similar (pedir ao usuário se existe).

### Etapa 2: Normalizar para uma tabela única
Padronize cada linha em:
- Data (YYYY-MM-DD).
- Provedor (Anthropic / OpenAI / Manus / outro).
- Modelo (Claude Opus 4.7, Sonnet, Haiku, GPT-4, GPT-4o-mini, etc.).
- Tokens input.
- Tokens output.
- Cache hit (se Anthropic e disponível).
- Custo USD.
- Skill / workflow / tag (se identificável).

Se a coluna "skill" não existir, tente inferir por horário ou volume — ou marque "indeterminado" e sinalize.

### Etapa 3: Calcular indicadores principais
- **Custo total no período** (semana, mês, trimestre).
- **Distribuição por provedor** — qual % vai para Anthropic vs OpenAI vs Manus.
- **Distribuição por modelo** — quanto está em Opus (caro) vs Sonnet vs Haiku.
- **Top 5 skills / workflows mais caros**.
- **Custo médio por execução** de cada skill.
- **Cache hit rate** (Anthropic) — se baixo, prompt caching está mal configurado.
- **Custo por dia** — picos vs baseline.
- **Projeção de custo mensal** (extrapolar média diária).

### Etapa 4: Identificar desperdícios
Procure padrões clássicos de skill mal otimizada:
- **Prompt enorme + saída pequena** — contexto inflado, falta cache.
- **Modelo muito caro para tarefa simples** — usar Opus para classificação binária.
- **Loops sem cap** — workflow agendado rodando 24x ao dia quando 4x bastaria.
- **Skill com cache hit rate < 30%** — provavelmente o prompt sistema muda a cada chamada.
- **Repetição de input** — mesmos 50k tokens enviados em 80 chamadas seguidas (cache obrigatório).
- **Output verboso** — saída média > 4k tokens em tarefa que pede uma frase.
- **Chamadas falhadas** que retornam custo (timeouts, errors retried).

### Etapa 5: Sugerir otimizações concretas
Para cada problema, recomendação acionável:
- "Skill X usa Opus mas faz só extração — migrar para Haiku economiza ~70%."
- "Prompt sistema da skill Y muda a cada call — extrair parte estática para `cache_control` reduz 50% do input."
- "Workflow agendado Z roda a cada 15min — 4x ao dia bastam pelo SLA."
- "Skill W tem output médio 6k tokens por chamada com instrução `seja conciso` — reforçar no system prompt e cap em `max_tokens`."

### Etapa 6: Projetar custo futuro
Com base no consumo + otimizações sugeridas:
- Cenário atual estendido (sem mudança).
- Cenário com otimizações sugeridas aplicadas.
- Sensibilidade: o que acontece se volume dobrar? (lançamento, novo workflow).

### Etapa 7: Sugerir orçamento e alertas
- Orçamento mensal sugerido baseado em padrão de uso.
- Alerta quando 50%, 80%, 100% do orçamento for atingido.
- Pelo menos uma "kill switch": skill ou workflow que pode ser desligado se gasto explodir.

## Formato de saída

```markdown
# Relatório de Custo de IA — [período]

## Resumo executivo
- Custo total: USD ... (R$ ...)
- Projeção mensal: USD ...
- Variação vs período anterior: +X% / -X%
- Top consumidor: [skill / workflow]

## Distribuição
| Provedor | Custo USD | % |
|---|---|---|
| Anthropic | ... | ... |
| OpenAI | ... | ... |
| Manus | ... | ... |

| Modelo | Custo USD | % | Chamadas |
|---|---|---|---|
| Claude Opus 4.7 | ... | ... | ... |
| Claude Sonnet | ... | ... | ... |
| GPT-4o | ... | ... | ... |

## Top 5 skills / workflows mais caros
| Skill | Chamadas | Custo médio | Total |
|---|---|---|---|
| ... | ... | ... | ... |

## Desperdícios identificados
1. [problema] — economia estimada: USD X/mês.
2. ...

## Otimizações recomendadas (priorizadas)
1. **[Ação]** — esforço: baixo | médio | alto. Economia: ...
2. ...

## Cenários
- Sem mudança: USD .../mês.
- Com top 3 otimizações: USD .../mês.
- Volume 2x sem otimizar: USD .../mês.

## Orçamento sugerido
- Mensal: USD ...
- Alertas: 50% | 80% | 100%.
- Kill switch: [workflow].
```

## Checklist de qualidade
- [ ] Dados normalizados em tabela única antes da análise.
- [ ] Cache hit rate calculado quando há dado da Anthropic.
- [ ] Top consumidores identificados com nome (não "indeterminado" sem investigar).
- [ ] Otimizações têm estimativa de economia, não só "use modelo mais barato".
- [ ] Projeção mensal extrapola de forma transparente (mostrar premissa).
- [ ] Pelo menos um kill switch foi sugerido.

## Notas para o assistente
- **Não inventar números**: se faltar dado, marque `?` em vez de estimar do nada. Honestidade > completude.
- **Conversão USD → BRL**: usar cotação do dia ou pedir ao usuário. Não fixar taxa antiga.
- **Alguns provedores cobram em centavos por milhão de tokens** — calcular com precisão decimal, arredondar só na apresentação.
- **Workflow do Manus**: pode ser opaco (custo cobrado no plano fixo). Se for plano fixo, a métrica é tempo de runtime, não tokens. Adapte.
- **Não recomendar trocar tudo para Haiku às cegas**: alguns workflows precisam mesmo de Opus por qualidade. Trade-off é qualidade × custo, não só custo.
- **Privacidade**: logs de uso podem revelar conteúdo de prompts via título / tag. Não vazar no relatório.
- **Conecta com**: `weekly-review` (passar custo semanal de IA), `decision-journal` (decidir migrar de modelo), `continue-work` (custo de cada agente em paralelo).
