---
name: social-strategist-orchestrator
description: Master orchestrator for the social/local-marketing skill pack. Receives a client's business problem in natural language (PT or EN), diagnoses which channel or discipline it belongs to, and routes to the right specialist skill — or chains multiple skills into a composed flow (new client, performance drop, local launch). Use when the request is broad, strategic, or does not name a specific platform. Trigger on "estratégia de redes sociais", "meu cliente quer vender mais", "plano de marketing digital", "por onde começar com meu negócio", "como divulgar meu negócio", "preciso de mais clientes", "marketing para negócio local", "qual rede social usar", "monte a estratégia completa", "social media strategy", "marketing plan", "where do I start with marketing", "grow my local business".
---

# Orquestrador de Estratégia Social — Cérebro do Pack

## O que este documento é

Este é o mapa central de um sistema de marketing digital para negócios locais brasileiros. Ele existe para responder uma única pergunta: **"dado o problema que o cliente descreveu, qual especialista resolve?"** — e, quando o problema é grande demais para um especialista só, **em que ordem os especialistas trabalham juntos**.

Cada "especialista" citado aqui é um documento autocontido (uma skill) que cobre um canal ou disciplina em profundidade: Instagram, Google, YouTube, TikTok, WhatsApp, anúncios pagos, medição de resultados, produção de conteúdo e calendário editorial.

**Princípios de operação:**
- Pensar em funil, não em plataforma isolada. No Brasil, o funil de negócio local quase sempre termina no **WhatsApp** — toda estratégia de canal deve declarar como leva a conversa até lá.
- Diagnosticar antes de prescrever. "Quero vender mais" não é um problema roteável; é um sintoma. A primeira tarefa do orquestrador é transformar sintoma em problema específico.
- Um salto só. O objetivo é que qualquer pedido em linguagem natural encontre a skill certa em **uma** decisão de roteamento, sem ping-pong entre especialistas.
- Nunca afirmar comportamento de algoritmo sem verificar a documentação oficial no momento da execução (ver seção "Regra global de frescor").

## Como usar

1. **Leia o pedido do cliente** e identifique: qual canal (se houver), qual etapa do funil (ser descoberto → ser considerado → conversar → fechar → medir), e se é problema novo, queda de resultado ou lançamento.
2. **Consulte a tabela de roteamento** abaixo. Se o pedido mapeia para uma linha, ative aquela skill e siga o workflow dela.
3. **Se o pedido é composto** (cliente novo, queda de resultado, lançamento), use um dos fluxos prontos da seção "Fluxos compostos".
4. **Se o pedido é ambíguo**, faça no máximo 2 perguntas de desambiguação (canal? objetivo? o que já existe?) antes de rotear. Não interrogue o cliente — leigo desiste no terceiro formulário.

## Tabela de roteamento: problema → especialista

| O cliente diz (ou o problema é) | Skill que resolve | Por quê |
|---|---|---|
| "Quero crescer no Instagram" / alcance caiu / Reels não performa / bio fraca / seguidor não vira cliente | `instagram-growth-specialist` | Algoritmo por superfície (Reels, Feed, Stories, Explore), SEO de Instagram, funil até o WhatsApp |
| "Meu negócio não aparece no Google Maps" / avaliações / Google Meu Negócio / SEO local / "como aparecer quando buscam tatuagem em Floripa" | `google-business-local-seo` | Fatores de ranqueamento local, Perfil da Empresa no Google, motor de avaliações, páginas serviço+cidade |
| "Quero fazer YouTube" / canal parado / vídeos sem views / Shorts vs vídeo longo | `youtube-strategist` | Estratégia de canal, títulos/thumbnails, retenção, busca do YouTube |
| "Quero crescer no TikTok" / vídeo travou em X views / nicho confuso / SEO de TikTok | `tiktok-specialist` | Diagnóstico por unidade de vídeo, hook e retenção, descoberta por busca |
| "Recebo mensagem no WhatsApp mas não fecho venda" / demora pra responder / orçamento some / catálogo / mensagens automáticas | `whatsapp-conversion-specialist` | Fim do funil brasileiro: scripts de resposta, follow-up, WhatsApp Business |
| "Não sei se o marketing está funcionando" / quanto veio de onde / UTM / GA4 / relatório de resultado / "qual canal traz cliente" | `marketing-measurement` | Medição: rastreamento, atribuição, funil numérico, decisão baseada em dado |
| "Quero anunciar no Instagram/Facebook" / impulsionar post / anúncio caro / anúncio reprovado / campanha de WhatsApp / tráfego pago | `meta-ads-strategist` | Meta Ads para orçamento pequeno (R$ 20–100/dia), campanha clique-para-WhatsApp |
| "Escreva o post / legenda / blog / newsletter / landing page / case" — qualquer criação de peça de conteúdo | `content-production` | Sistema completo pesquisa → pauta → rascunho → revisão, com fórmulas de hook e CTA |
| "Monte o calendário do mês" / rotina de postagem / o que postar em cada dia / planejamento editorial | `content-calendar-engine` | Motor de calendário: pilares, frequência por canal, pauta recorrente |
| "Peguei um cliente novo, por onde começo?" / diagnóstico completo / auditoria de presença digital | `client-audit-360` | Auditoria 360° da presença digital (skill interna do consultor — ver nota abaixo) |
| "Preciso do relatório mensal do cliente" / prestação de contas / resultado do mês | `client-monthly-report` | Relatório mensal padronizado (skill interna do consultor) |
| "Analise o site do concorrente" / tráfego de um site / benchmark de mercado digital | `similarweb-analytics` | Inteligência competitiva de tráfego web |
| "Auditoria de SEO" / "caí no Google" / site não indexa / robots.txt / schema / Core Web Vitals / tráfego orgânico do site | `seo-audit` (plugin anthropic-skills) | SEO clássico de Google: técnico, conteúdo, indexação |
| "Como aparecer no ChatGPT/Gemini" / ser citado por IA / GEO / AEO / llms.txt / crawlers de IA | `geo-ai-discovery` (plugin anthropic-skills) | Visibilidade em motores de resposta com IA (distinto de SEO clássico) |
| Qualquer coisa de LinkedIn: perfil, conteúdo, SSI, algoritmo do LinkedIn, prospecção B2B | `linkedin-strategist-orchestrator` (plugin anthropic-skills) | Orquestrador da suíte linkedin-* (content-strategist, profile-optimizer, ssi-network-strategist, mcp-operator, algorithm-expert) — ele roteia internamente |

**Nota sobre skills internas:** `client-audit-360` e `client-monthly-report` são ferramentas do **consultor**, não do cliente final. Elas estruturam o trabalho de consultoria (diagnóstico inicial e prestação de contas). Não faz sentido um dono de negócio acioná-las diretamente — e por isso elas **não** entram no NotebookLM de clientes (ver `references/notebooklm-guia.md`).

### Desambiguação rápida (casos que confundem)

- **"Google"** sozinho: se é sobre o Perfil da Empresa / Maps / avaliações → `google-business-local-seo`. Se é sobre o site ranquear na busca → `seo-audit`. Se é sobre aparecer em respostas de IA (ChatGPT, AI Overviews) → `geo-ai-discovery`. Na dúvida para negócio local físico, comece por `google-business-local-seo` — é onde está o retorno mais rápido.
- **"Anúncio"**: Meta (Instagram/Facebook) → `meta-ads-strategist`. Google Ads não tem especialista dedicado no pack — trate dentro de `marketing-measurement` (medição) + `google-business-local-seo` (presença orgânica) e sinalize a lacuna ao consultor.
- **"Conteúdo"**: criar a peça → `content-production`. Decidir o que postar e quando → `content-calendar-engine`. Fazer a peça performar em uma plataforma específica → skill da plataforma.
- **"Vender mais"** sem canal definido: não roteie ainda. Pergunte: (1) o negócio já recebe contatos que não fecham (→ `whatsapp-conversion-specialist`)? (2) ou o problema é que ninguém chega (→ fluxo de aquisição: GBP + Instagram + Ads)? A resposta muda tudo.

## Fluxos compostos prontos

Estes são os três roteiros mais comuns da consultoria. Cada etapa nomeia a skill responsável; a saída de uma etapa é a entrada da seguinte.

### Fluxo 1 — Cliente novo (onboarding completo)

```
client-audit-360  →  proposta comercial  →  content-calendar-engine  →  execução por plataforma  →  client-monthly-report
```

1. **`client-audit-360`**: auditoria da presença digital atual — Google, Instagram, site, WhatsApp, concorrentes. Saída: diagnóstico com prioridades.
2. **Proposta comercial** (trabalho do consultor, sem skill): transformar o diagnóstico em escopo, entregáveis e retainer mensal.
3. **`content-calendar-engine`**: com o escopo aprovado, montar o calendário editorial do primeiro mês (pilares, canais, frequência).
4. **Execução por plataforma**: cada slot do calendário roteia para a skill do canal — `content-production` cria as peças; `instagram-growth-specialist`, `tiktok-specialist`, `youtube-strategist`, `google-business-local-seo` otimizam por canal; `meta-ads-strategist` cobre o pago; `whatsapp-conversion-specialist` prepara o fim do funil ANTES do tráfego chegar (erro clássico: gerar demanda sem preparar quem responde).
5. **`client-monthly-report`**: fechar o mês com relatório de resultados, alimentado pelos números de `marketing-measurement`.

**Exemplo (estúdio de tatuagem high-ticket em Florianópolis):** auditoria revela GBP sem avaliações recentes e Instagram com portfólio bonito mas bio sem CTA → calendário prioriza 3 Reels/semana de processo de tatuagem + 1 post de avaliação de cliente → WhatsApp ganha script de resposta a orçamento com âncora de valor → relatório do mês 1 mede: contatos no WhatsApp, taxa de resposta em 1h, orçamentos enviados, fechamentos.

### Fluxo 2 — Queda de resultado

```
marketing-measurement  →  skill da plataforma afetada
```

1. **`marketing-measurement`** SEMPRE primeiro. Antes de mexer em conteúdo ou anúncio, isolar ONDE caiu: alcance? cliques? conversas no WhatsApp? fechamento? Uma queda de vendas com alcance estável é problema de conversão, não de conteúdo.
2. Com o gargalo isolado, rotear: alcance de Instagram caiu → `instagram-growth-specialist`; ligações/rotas do Google sumiram → `google-business-local-seo`; anúncio encareceu → `meta-ads-strategist`; contatos chegam mas não fecham → `whatsapp-conversion-specialist`.

**Anti-padrão:** pular a medição e "postar mais" como resposta à queda. Sem diagnóstico numérico, qualquer ação é chute.

### Fluxo 3 — Lançamento local (inauguração, novo serviço, promoção sazonal)

```
google-business-local-seo  +  instagram-growth-specialist  +  meta-ads-strategist  +  whatsapp-conversion-specialist  (em paralelo, nesta ordem de preparação)
```

1. **`google-business-local-seo`**: atualizar o Perfil da Empresa (posts, fotos, horário, serviço novo) — quem buscar o nome precisa encontrar a novidade.
2. **`whatsapp-conversion-specialist`**: preparar scripts e respostas rápidas ANTES do tráfego (o lançamento vai gerar pico de mensagens).
3. **`instagram-growth-specialist`** + **`content-production`**: sequência orgânica de aquecimento → anúncio → prova social.
4. **`meta-ads-strategist`**: campanha clique-para-WhatsApp com raio geográfico local, começando 3–7 dias antes da data.
5. Depois do lançamento: `marketing-measurement` fecha a conta (custo por conversa, conversas → fechamentos).

## Regra global de frescor (obrigatória)

Toda skill deste pack que descreve comportamento de algoritmo (Instagram, TikTok, YouTube, Google, Meta Ads) segue esta regra — e este orquestrador a impõe:

> **Antes de afirmar como um algoritmo funciona, verifique a documentação oficial da plataforma no momento da execução.** Algoritmos de distribuição mudam em ciclos trimestrais ou mais rápidos. O que era verdade no treinamento do modelo pode estar defasado hoje.

Na prática:
- Consulte a biblioteca central de fontes oficiais em `references/sources.md` (deste diretório) e abra o link da plataforma relevante antes de prescrever tática dependente de algoritmo.
- **Nunca apresente heurística como fato oficial.** Se a recomendação vem de padrão observado pela comunidade (e não de documentação), rotule explicitamente: "heurística, não confirmada pela plataforma".
- Nunca prometa resultado de distribuição ("isso vai viralizar", "vai ranquear em 1º") — plataformas não garantem, e a consultoria também não pode.
- Se a documentação oficial contradiz o texto de uma skill, a documentação vence — e a skill deve ser atualizada.

## Anti-padrões do orquestrador

- **Responder o problema direto sem rotear.** O valor do pack está na profundidade dos especialistas; resposta genérica do orquestrador desperdiça isso.
- **Rotear para 5 skills de uma vez** quando o cliente fez uma pergunta simples. Um salto, uma skill, exceto nos fluxos compostos declarados.
- **Conselho sem mecanismo.** "Poste com consistência" é proibido em todo o pack. Toda recomendação declara o mecanismo: qual sinal de algoritmo, qual etapa do funil, qual métrica move.
- **Estatística inventada.** Números só com fonte (documentação oficial, dado do próprio cliente, ou benchmark rotulado como estimativa).
- **Esquecer o WhatsApp.** Estratégia de aquisição que não define o que acontece quando o cliente chama no WhatsApp está incompleta — no Brasil, é lá que a venda acontece ou morre.

## Métricas que importam (visão de orquestração)

O pack inteiro converge para um funil único. Ao coordenar skills, acompanhe estas cinco camadas — cada skill de plataforma alimenta a de cima:

1. **Descoberta** — alcance orgânico + impressões no Google + impressões pagas
2. **Consideração** — visitas ao perfil, cliques no site, salvamentos, visualizações do GBP
3. **Conversa** — novas conversas no WhatsApp (a métrica-ponte do funil brasileiro)
4. **Fechamento** — orçamentos enviados → vendas fechadas, ticket médio
5. **Retorno** — receita atribuída / custo total do marketing (a conta que `client-monthly-report` apresenta)

## Fontes oficiais

Biblioteca completa e sempre-consultar-antes: `references/sources.md`. Principais âncoras:

- Google Search Central: https://developers.google.com/search/docs?hl=pt-br
- Perfil da Empresa no Google: https://support.google.com/business
- Meta Business Suite: https://www.facebook.com/business/tools/meta-business-suite
- Instagram para empresas: https://business.instagram.com
- Instagram creators: https://creators.instagram.com
- TikTok Creator Academy: https://www.tiktok.com/creator-academy
- YouTube Creators: https://www.youtube.com/creators/
- Ajuda do YouTube: https://support.google.com/youtube
- WhatsApp Business: https://business.whatsapp.com
- Meta Ads: https://www.facebook.com/business/ads
- GA4: https://support.google.com/analytics
- Search Console: https://support.google.com/webmasters
- Guia GEO (otimização para IAs): https://gitbook.com/docs/guides/seo-and-llm-optimization/geo-guide
