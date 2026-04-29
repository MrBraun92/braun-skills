---
name: transcript-fixer
description: Corrige transcrições automáticas geradas por Teams, Tactiq, Otter, Copilot e similares — insere pontuação, separa por speaker, remove muletas verbais ("é", "tipo", "então", "uh"), preserva conteúdo e tom. Aciona quando o usuário cola um texto bruto de transcrição automática que está difícil de ler.
---

# Transcript Fixer

Esta skill recebe uma transcrição automática crua — geralmente um bloco contínuo sem pontuação, com falhas de speaker diarization e cheia de muletas verbais — e devolve um texto legível, com pontuação correta, separado por speaker quando possível, e com muletas removidas sem alterar o sentido. Foco em entrevistas qualitativas (caso real: tese de mestrado da UiS), reuniões internas e conversas gravadas. Esta skill **não é tradução** e **não é resumo** — é higienização.

## Quando usar esta skill
- O usuário cola transcrição do Teams, Otter, Tactiq, Copilot, Whisper, Fireflies ou similar.
- Entrevista qualitativa de pesquisa que será citada em tese (precisa estar inteligível para quote).
- Reunião que será transformada em ata depois (use `meeting-to-actions` no passo seguinte).
- Áudio longo (60+ minutos) onde a leitura crua é inviável.

## Metodologia

### Etapa 1: Diagnóstico inicial
Pergunte (ou identifique) ao receber o texto:
- Origem da transcrição (Otter, Teams, Whisper, etc.) — cada uma tem padrão diferente de timestamp e speaker tag.
- Quantos speakers? Conhece os nomes deles? (ex: "Entrevistador" e "Participante 1" para tese).
- Idioma (PT-BR ou EN — não traduzir, apenas higienizar no idioma original).
- Vai virar quote literal em paper acadêmico? (se sim, ser ainda mais conservador).

### Etapa 2: Restaurar pontuação
Inserir vírgulas, pontos, pontos de interrogação e exclamação seguindo prosódia natural. Regras:
- Pausa longa + queda entonacional → ponto final.
- Frase curta seguida de continuação → vírgula.
- Início de frase com "como", "por que", "será" e tom interrogativo → ponto de interrogação.
- Quebra de frase longa em duas: prefira ponto a ponto-e-vírgula. Manter prosa, não formal.

### Etapa 3: Separar por speaker
Se a transcrição vem com tags de speaker (`Speaker 1:`, `Oliver:`, `[Maria]:`), preserve.
Se vem como bloco contínuo, infira mudanças de speaker por:
- Mudança brusca de tom ou vocabulário.
- Frases interrogativas seguidas de respostas.
- Marcadores como "sim", "concordo", "mhm" no início de turno.
Quando incerto, marque com `[?]` em vez de inventar.

### Etapa 4: Remover muletas verbais
Remova com critério, **preservando o ritmo da fala**:
- "é", "então", "tipo", "tipo assim", "sabe", "né", "uh", "ah" — remover quando vazias.
- Repetições imediatas ("eu eu acho que", "a a gente") — manter uma ocorrência.
- Falsos starts ("eu queria... não, melhor...") — preservar se mostram raciocínio em voz alta (importante em entrevistas qualitativas), remover se são puro ruído.
- **Não remova** marcadores discursivos que carregam informação ("aliás", "mas", "porque", "olha").

### Etapa 5: Preservar marcações de pesquisa
Em entrevistas qualitativas para tese:
- Marcadores não-verbais relevantes ficam entre colchetes: `[risos]`, `[pausa longa]`, `[hesitação]`.
- Trechos inaudíveis: `[inaudível]` ou `[inaudível 14:32]` se houver timestamp.
- Sobreposição de fala: `[fala sobreposta]`.
- Pausas significativas que carregam significado: preserve.

### Etapa 6: Validar fidelidade
Antes de entregar, garanta que:
- Nenhuma frase foi reescrita — só pontuação, capitalização e remoção cirúrgica de muletas.
- O sentido está preservado palavra por palavra (exceto muletas).
- Speakers estão consistentes (não troca quem fala o quê).

## Formato de saída

Texto limpo no idioma original, com este padrão:

```
[timestamp opcional] Speaker: Frase com pontuação correta. Outra frase.

Outro Speaker: Resposta limpa.
```

Ou, para entrevistas formais:

```
**Entrevistador:** Pergunta limpa?

**Participante 1:** Resposta com [risos] marcações relevantes preservadas.
```

No final, comentário entre `<!-- ... -->` listando:
- Trechos com baixa confiança de pontuação.
- Mudanças de speaker inferidas (não confirmadas).
- Trechos onde muletas foram preservadas porque carregavam significado.

## Checklist de qualidade
- [ ] Nenhuma palavra de conteúdo foi alterada.
- [ ] Pontuação restaurada de forma consistente.
- [ ] Speakers identificados ou marcados como `[?]` quando incerto.
- [ ] Marcações de pesquisa (`[risos]`, `[pausa]`, `[inaudível]`) preservadas.
- [ ] Muletas removidas só quando vazias semanticamente.
- [ ] Comentário de transparência no final lista incertezas.

## Notas para o assistente
- **Em entrevistas para tese acadêmica, ser mais conservador** — preferir manter muleta se houver dúvida. Para citação literal, pesquisador precisa do que foi dito.
- **Não traduzir.** Se o áudio era em PT-BR e a transcrição saiu em EN errada, sinalize ao usuário.
- **Não inventar nomes de speaker.** Se não foi dito, deixar como `Speaker 1`.
- **Transcrição muito longa (>1h)**: dividir em blocos por mudança de tópico ou a cada ~15 min de áudio.
- **Conteúdo sensível**: se identificar dados pessoais, médicos ou financeiros sigilosos, sinalize ao usuário antes de prosseguir.
