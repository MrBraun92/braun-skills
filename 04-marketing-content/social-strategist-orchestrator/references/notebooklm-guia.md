# Guia prático: instalando o pack no NotebookLM do cliente

Este guia ensina, passo a passo, como montar um **NotebookLM** para um cliente leigo usando os documentos deste pack de skills como fontes. O resultado é um "assistente de marketing" que o cliente consulta sozinho, no navegador ou no celular, e que responde **apenas** com base no material da consultoria.

**Piloto de referência:** estúdio de tatuagem high-ticket em Florianópolis. Os exemplos abaixo usam esse caso, mas o processo é idêntico para qualquer negócio local.

---

## 1. O que é o NotebookLM (explicação para o cliente)

O NotebookLM (https://notebooklm.google.com) é uma ferramenta gratuita do Google onde você cria um "caderno" e sobe documentos como fontes. Depois, você conversa com uma IA que responde usando **somente** esses documentos — como ter o manual da consultoria aberto do lado, mas que responde perguntas.

**Aviso importante (repita isso ao cliente):** o NotebookLM responde **APENAS com base nas fontes subidas**. Ele não busca na internet, não sabe de notícias e não conhece nada fora dos documentos do caderno. Se a resposta não está nas fontes, ele vai dizer que não encontrou — isso é um recurso, não um defeito: garante que o cliente recebe a metodologia da consultoria, não opinião aleatória da internet.

## 2. Quais documentos subir como fontes

Suba os arquivos `SKILL.md` abaixo, nesta ordem de prioridade. Cada um é um documento autocontido em português. No Mac do consultor, os caminhos são:

**Núcleo (subir sempre):**

1. `/Users/mrbraun_mac/.claude/skills/instagram-growth-specialist/SKILL.md` — Instagram: Reels, bio, Stories, funil até o WhatsApp
2. `/Users/mrbraun_mac/.claude/skills/whatsapp-conversion-specialist/SKILL.md` — WhatsApp: scripts de resposta, follow-up de orçamento, fechamento
3. `/Users/mrbraun_mac/.claude/skills/google-business-local-seo/SKILL.md` — Google Maps / Perfil da Empresa: avaliações, aparecer nas buscas locais
4. `/Users/mrbraun_mac/.claude/skills/content-calendar-engine/SKILL.md` — calendário: o que postar, quando e por quê
5. `/Users/mrbraun_mac/.claude/skills/content-production/SKILL.md` — produção: como escrever legenda, post, página, e-mail

**Opcionais (subir se o canal for relevante para o cliente):**

6. `/Users/mrbraun_mac/.claude/skills/tiktok-specialist/SKILL.md` — se o negócio produz vídeo curto além do Instagram
7. `/Users/mrbraun_mac/.claude/skills/youtube-strategist/SKILL.md` — se o negócio investe em vídeo longo/Shorts (para o estúdio de tatuagem: sim, vídeos de processo funcionam bem)

**Complemento útil:**

8. `/Users/mrbraun_mac/.claude/skills/social-strategist-orchestrator/references/sources.md` — a lista de fontes oficiais das plataformas (dá ao cliente os links certos quando ele quiser conferir algo direto na fonte)

**Como subir:** no NotebookLM, criar caderno novo (ex.: "Marketing — [Nome do Estúdio]") → "Adicionar fonte" → arrastar cada arquivo `.md` (o NotebookLM aceita Markdown; se algum upload falhar, abra o arquivo, copie o texto e use "Texto colado" como fonte).

## 3. O que NÃO subir (e por quê)

**Não suba as skills internas de consultoria:**

- `client-audit-360` — é o roteiro de auditoria do **consultor**: como diagnosticar um cliente novo, o que cobrar, como priorizar. Nas mãos do cliente, vira confusão ("por que meu consultor segue um checklist?") e entrega o método comercial.
- `client-monthly-report` — é o modelo de prestação de contas do **consultor**. O cliente recebe o relatório pronto, não o molde.
- `meta-ads-strategist`, `marketing-measurement`, `similarweb-analytics` — são operacionais/técnicas demais para leigo e envolvem decisões de orçamento que devem passar pelo consultor. Suba apenas se o cliente opera os próprios anúncios (não é o caso do piloto).
- `social-strategist-orchestrator/SKILL.md` (o orquestrador em si) — ele roteia entre skills dentro do Claude Code; no NotebookLM não há roteamento, então só adicionaria ruído.

**Regra geral:** o NotebookLM do cliente contém o que o cliente **executa no dia a dia** (conteúdo, Instagram, WhatsApp, Google). O que é método, precificação ou operação da consultoria fica fora.

## 4. Como o cliente deve perguntar (10 perguntas prontas)

Entregue esta lista ao cliente junto com o caderno. Perguntas específicas geram respostas específicas — quanto mais contexto na pergunta, melhor a resposta.

1. "Me dê 5 ideias de Reels para essa semana usando os tipos de conteúdo que funcionam para estúdio de tatuagem."
2. "Escreva a resposta para esse orçamento no WhatsApp: [colar a mensagem do cliente]. Quero valorizar o trabalho sem parecer caro demais."
3. "Um cliente pediu orçamento há 3 dias e sumiu. Escreva uma mensagem de follow-up que não pareça insistente."
4. "Escreva a legenda para um post com a foto de uma tatuagem finalizada de [estilo], terminando com convite para chamar no WhatsApp."
5. "Como devo pedir avaliação no Google para um cliente que acabou de sair satisfeito da sessão? Escreva a mensagem pronta."
6. "Monte meu calendário de postagens da próxima semana: tenho 3 fotos de trabalhos prontos, 1 vídeo de processo e pouco tempo."
7. "Minha bio do Instagram está assim: [colar bio]. Reescreva seguindo as recomendações do documento de Instagram."
8. "O que eu devo postar no meu Perfil da Empresa no Google este mês?"
9. "Qual a melhor forma de transformar um vídeo de processo de tatuagem em conteúdo para Reels? Me dê o roteiro com gancho nos primeiros segundos."
10. "Recebi essa mensagem: 'quanto custa um fechamento de braço?'. Escreva a resposta ideal seguindo o script de orçamento do documento de WhatsApp."

**Dica de uso:** sempre colar a situação real (a mensagem recebida, a bio atual, as fotos disponíveis). O NotebookLM aplica a metodologia dos documentos ao caso concreto.

## 5. Manutenção do caderno

- Quando a consultoria atualizar uma skill (ex.: mudança confirmada no algoritmo do Instagram), **substitua a fonte antiga** no caderno pela versão nova — o NotebookLM não atualiza sozinho.
- Revise o caderno a cada trimestre junto com a revisão de frescor das skills (algoritmos mudam; os documentos acompanham).
- Se o cliente relatar que o caderno "não soube responder" algo recorrente, isso é sinal para a consultoria: ou falta uma seção na skill correspondente, ou a pergunta é da alçada do consultor (aí a resposta certa é chamar o consultor, não engordar o caderno).

## 6. Checklist de instalação (resumo executável)

- [ ] Criar caderno no NotebookLM com o nome do cliente
- [ ] Subir os 5 SKILL.md do núcleo (+ TikTok/YouTube se relevante, + sources.md)
- [ ] Conferir que NENHUMA skill interna de consultoria foi subida
- [ ] Fazer 3 perguntas-teste da lista acima e validar que as respostas seguem a metodologia
- [ ] Compartilhar o caderno com o e-mail do cliente (permissão de leitura/chat)
- [ ] Enviar ao cliente: a lista de 10 perguntas prontas + o aviso de que o caderno responde só com base nas fontes
- [ ] Agendar revisão trimestral das fontes
