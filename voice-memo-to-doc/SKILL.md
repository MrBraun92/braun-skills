---
name: voice-memo-to-doc
description: Recebe áudio ou transcrição de 5 a 15 minutos de fala solta sobre uma ideia e devolve documento estruturado — problema, hipótese, próximos passos, perguntas em aberto. Para o usuário pensar caminhando ou no carro e formalizar depois. Aciona quando o usuário envia voice memo, áudio do WhatsApp, gravação do iPhone, ou cola transcrição de monólogo solto.
---

# Voice Memo to Doc

Esta skill captura a forma como o Oliver pensa melhor — falando em voz alta enquanto caminha, dirige ou está no chuveiro. Voice memos são geralmente 5-15 min de fluxo de consciência: ideia inicial, "espera, melhor pensar assim", contradição, "ah, e também...". Sem ferramenta, esses áudios morrem no celular. Esta skill os transforma em **documento estruturado e acionável** preservando a riqueza do raciocínio em voz alta — sem reescrever em tom corporativo nem perder os "talvez" e "não tenho certeza" que carregam informação.

## Quando usar esta skill
- O usuário envia voice memo (m4a, mp3, ogg) ou transcrição dele.
- Áudio de WhatsApp longo dele para si mesmo ou para um colaborador.
- Brainstorm gravado no carro a caminho de algum lugar.
- "Pensando em voz alta" sobre feature de produto, trade, capítulo de tese, decisão pessoal.
- O usuário diz "ouvi minha gravação e tenho ideia confusa, organiza pra mim".

## Metodologia

### Etapa 1: Ter transcrição limpa
Se vier áudio, primeiro transcreva (ou peça ferramenta externa). Se vier transcrição crua, acione `transcript-fixer` antes para ter texto legível. Sem texto legível, esta skill produz lixo estruturado.

### Etapa 2: Identificar o tipo de monólogo
Pergunte (ou deduza pelo conteúdo):
- **Brainstorm de feature / produto** — usuário está explorando uma ideia nova de software, evento, conteúdo.
- **Tese / argumento intelectual** — usuário está construindo argumento acadêmico.
- **Decisão pessoal / carreira** — usuário está pensando em mudança de rumo.
- **Pré-trade / trade thesis** — usuário está justificando entrada ou saída de posição. (Nesse caso, considerar `bbb-strategist` ou `trading-thesis-orchestrator` em sequência.)
- **Vent / desabafo** — usuário só queria botar pra fora; não estruturar como plano.

Cada tipo gera um output ligeiramente diferente.

### Etapa 3: Mapear estrutura latente
Procure no monólogo a estrutura natural:
- **Problema**: o que está incomodando? Por que falar disso agora?
- **Contexto**: o que mudou para o tema virar urgente / interessante?
- **Hipótese ou tese**: qual é a aposta intelectual?
- **Evidências mencionadas**: dados, exemplos, analogias usadas.
- **Contra-argumentos / dúvidas**: pontos onde o usuário disse "mas" ou "espera".
- **Próximos passos**: ações ou perguntas que o usuário levantou no fim.

### Etapa 4: Preservar voz e incerteza
Diferente de uma ata corporativa, **não normalize tom**:
- Manter "acho que", "talvez", "não tenho certeza" — eles sinalizam confiança real.
- Manter analogias e exemplos pessoais.
- Manter contradições! Se o usuário disse uma coisa no minuto 3 e o oposto no minuto 12, registre as duas. A contradição é dado.
- Não inventar conclusão se o monólogo terminou sem fechamento.

### Etapa 5: Estruturar em documento
Formato fixo (ver "Formato de saída"). Hierarquia ajuda o usuário a voltar e refinar parte específica depois. Cada seção deve ser editável de forma independente.

### Etapa 6: Sugerir próximos passos concretos
Termine com bloco de "próximos passos" que o usuário pode acionar:
- Se virou ideia de produto → próximo passo é spec curta (sugerir skill de PRD).
- Se virou decisão → registrar com `decision-journal`.
- Se virou tese acadêmica → conectar com orientador / leitura específica.
- Se virou pré-trade → desenvolver com `trading-thesis-orchestrator`.

Sempre uma sugestão por vez, não uma checklist gigante.

## Formato de saída

```markdown
# [Título da ideia — extraído da fala, não inventado]

**Data:** [data do voice memo]
**Duração:** [tempo aproximado da gravação]
**Tipo:** brainstorm produto | tese | decisão | trade | desabafo

## Problema / pergunta motivadora
[1 parágrafo — o que disparou esse monólogo]

## Contexto
[o que mudou recentemente — o que tornou esse tema atual]

## Hipótese / tese
[a aposta intelectual em uma frase, com hedge se o usuário hedgeou]

## Evidências e exemplos mencionados
- [exemplo 1]
- [exemplo 2]
- [analogia 3]

## Dúvidas / contradições
- [ponto onde o usuário disse "mas..."]
- [contradição interna entre minuto X e minuto Y]
- [perguntas em aberto]

## Próximos passos sugeridos
- [ação concreta 1]
- [pergunta a responder]
- [pessoa a consultar / leitura a fazer]

## Trecho-chave (quote literal)
> [1 ou 2 frases que sintetizam melhor o argumento — citação direta da fala]

---
<!-- Se quiser, próxima skill: [decision-journal | trading-thesis-orchestrator | spec writer]. -->
```

## Checklist de qualidade
- [ ] Estrutura preservou a voz do usuário (não virou texto corporativo).
- [ ] Incertezas e hedges foram mantidos onde existiam.
- [ ] Contradições registradas, não suavizadas.
- [ ] Quote literal escolhida representa o ponto central.
- [ ] Próximos passos são acionáveis em uma frase cada.
- [ ] Título saiu da fala, não foi inventado.

## Notas para o assistente
- **Voice memo não é PRD nem ata.** Não force estrutura inflada — se foi um monólogo curto sobre uma única ideia, o documento é curto também.
- **Não interpretar emoção como dado de produto**: se a pessoa estava irritada com cliente, isso vira observação no contexto, não vira "feature request".
- **Áudios em PT-BR são quase sempre informais**: respeite o registro; não traduzir para português corporativo.
- **Áudios mistos (PT/EN)**: preserve o code-switching se foi natural.
- **Voice memo pessoal sensível**: se identificar que era desabafo privado (relacionamento, saúde mental, conflito profissional), pergunte se o usuário realmente quer estruturar — às vezes o ato de falar já resolveu e não precisa virar documento.
- **Áudios muito longos (>20 min)**: divida em duas ou três ideias separadas. Um voice memo pode conter três insights distintos que merecem documentos separados.
