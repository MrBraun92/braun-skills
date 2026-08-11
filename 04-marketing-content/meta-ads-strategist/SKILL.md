---
name: meta-ads-strategist
description: Meta Ads (Facebook/Instagram) strategist for Brazilian local businesses with small budgets (R$ 20-100/day). Covers lean account structure, click-to-WhatsApp campaigns, Pixel + Conversions API minimum viable setup, creative testing cycles, broad audiences with geo radius, learning phase discipline, realistic BR benchmarks, and diagnosis of expensive ads, rejected ads, and restricted accounts. Use when planning, launching, auditing, or fixing paid traffic on Meta for a local business. Trigger on "meta ads", "facebook ads", "instagram ads", "anúncio no instagram", "tráfego pago", "impulsionar post", "campanha de WhatsApp", "click to WhatsApp", "CPM alto", "anúncio caro", "anúncio reprovado", "conta de anúncios restrita", "gestor de tráfego", "quanto investir em anúncio", "criativo para anúncio", "público do anúncio", "fase de aprendizado".
---

# Estrategista de Meta Ads para Negócio Local

## O que é este documento

Este é o manual de tráfego pago no Meta (Instagram + Facebook) para negócios locais brasileiros com orçamento pequeno — de R$ 20 a R$ 100 por dia. Ele foi escrito para ser lido por duas audiências: o dono do negócio que quer entender o que está sendo feito com o dinheiro dele, e quem opera as campanhas no Gerenciador de Anúncios.

A tese central: **com orçamento pequeno, quase todos os erros são erros de estrutura, não de "otimização"**. Quem espalha R$ 50/dia em 6 campanhas com 4 conjuntos cada não tem 24 experimentos — tem 24 fragmentos famintos de dados que nunca saem da fase de aprendizado. A disciplina deste manual é o oposto: pouquíssimas campanhas, verba concentrada, variação nos criativos (não na estrutura), e o funil terminando onde o brasileiro compra: **no WhatsApp**.

Exemplo prático usado ao longo do documento: um estúdio de tatuagem high-ticket em Florianópolis (projetos autorais a partir de R$ 1.500, fechamento por orçamento no WhatsApp). A lógica vale igualmente para clínica, restaurante, academia, arquiteto ou qualquer negócio que atende gente num raio geográfico.

## Princípios operacionais

- **Pense em leilão e sinal, não em "impulsionar".** O Meta é um leilão: você compra atenção competindo com todo anunciante que quer o mesmo público. Quem vence não é quem paga mais, e sim quem entrega o melhor conjunto de lance + qualidade do anúncio + probabilidade de ação. Criativo ruim = você paga mais caro pelo mesmo espaço.
- **O algoritmo otimiza para o evento que você pede.** Se você pede cliques, ele acha gente que clica (inclusive quem clica em tudo e não compra nada). Se você pede conversas iniciadas, ele acha gente que chama no WhatsApp. Escolher o objetivo errado é o erro mais caro e mais comum.
- **Com verba pequena, o criativo é o targeting.** O sistema de entrega moderno decide quem vê o anúncio principalmente a partir de quem reage ao criativo. Trocar de público raramente salva um criativo fraco; trocar o criativo frequentemente salva o público.
- **Diagnóstico por unidade, com hierarquia.** Anúncio caro tem 4 suspeitos em ordem: criativo → oferta → destino (WhatsApp/página) → público. Investigue nessa ordem, com métrica para cada um (ver seção de diagnóstico).
- **ROAS real só existe se a ponta do funil for medida.** Custo por conversa é métrica intermediária. O que fecha a conta é: de cada 10 conversas, quantas viram venda, e de quanto. Sem esse número anotado (mesmo que numa planilha manual), ninguém sabe se a campanha dá lucro.

## Regra de frescor (obrigatória antes de afirmar comportamento de plataforma)

O Gerenciador de Anúncios, os nomes de objetivos, as regras da fase de aprendizado e os recursos Advantage+ mudam com frequência — a Meta reorganiza a interface e renomeia produtos mais ou menos a cada trimestre.

**Antes de afirmar qualquer comportamento específico da plataforma (nomes de objetivos, limites da fase de aprendizado, disponibilidade de recurso, políticas de anúncio), verifique a documentação oficial da Meta no momento da execução** — Central de Ajuda para Empresas e a página de Meta Ads listadas em "Fontes oficiais". O que este documento traz de mecânica de leilão e de método de teste é estável; nomes de botão e números exatos de eventos/dias, não.

Tudo que neste documento for faixa numérica de mercado (CPM, CTR, custo por conversa) é **heurística de operação, não número oficial da Meta** — a Meta não publica benchmarks por país/nicho. Use as faixas como ponto de partida e substitua pelos números reais da conta assim que existirem 2-3 semanas de dados.

## 1. Estrutura de conta enxuta (R$ 20-100/dia)

### A matemática que ninguém faz

A fase de aprendizado (ver seção 6) precisa de um volume mínimo de eventos de otimização por conjunto de anúncios por semana — a referência histórica da Meta é da ordem de ~50 eventos/semana (verifique o número vigente na documentação). Se o seu custo por conversa iniciada é R$ 15, um conjunto precisa de ~R$ 750/semana (~R$ 107/dia) **só para sair do aprendizado**. Com R$ 50/dia no total, você sustenta **um** conjunto decentemente — não seis.

Conclusão estrutural:

| Orçamento diário | Estrutura recomendada |
|---|---|
| R$ 20-40/dia | 1 campanha, 1 conjunto amplo, 3-5 anúncios dentro dele |
| R$ 40-70/dia | 1 campanha principal (conversas) + opcionalmente 1 de retargeting com verba mínima (R$ 10/dia) quando houver dados |
| R$ 70-100/dia | 2 campanhas no máximo: aquisição (conversas/leads) + retargeting. Nunca 3+ campanhas frias competindo entre si |

Regra dura: **cada campanha nova que você cria rouba dados das existentes**. Campanhas da mesma conta com públicos sobrepostos competem no mesmo leilão. Com verba pequena, consolidar sempre vence fragmentar.

### CBO (orçamento no nível da campanha)

O orçamento de campanha Advantage (o antigo "CBO") deixa o Meta distribuir a verba entre conjuntos automaticamente, em vez de você fixar valor por conjunto.

- **Com 1 conjunto só (o caso típico deste manual): tanto faz** — não há o que distribuir. Use o padrão da interface.
- **Com 2+ conjuntos** (ex.: aquisição fria + retargeting **na mesma campanha — evite;** ou dois raios geográficos distintos): CBO tende a favorecer o conjunto que já performa, o que é bom para eficiência e ruim para teste justo. Se a intenção é **testar** dois públicos em pé de igualdade, use orçamento por conjunto (ABO) com valores iguais por 7 dias; se a intenção é **performar**, use CBO.

Heurística: orçamento pequeno + estrutura enxuta = a decisão CBO/ABO importa pouco. Ela só vira relevante quando há múltiplos conjuntos — que é exatamente o que este manual manda evitar.

### Advantage+ vs configuração manual

O Meta empurra automação "Advantage+" em vários níveis (campanha inteira, público, posicionamentos, criativo). Regra prática para negócio local:

- **Posicionamentos Advantage+ (automáticos): aceite.** Deixar o sistema escolher entre Feed, Reels e Stories quase sempre barateia a entrega. Exceção: se o criativo só funciona em 9:16, confira como ele aparece nos posicionamentos quadrados.
- **Público Advantage+ / expansão de público: aceite parcialmente.** Para negócio local, a única restrição inegociável é **geografia** (o Meta respeita o raio). Idade/interesses podem ficar amplos ou com expansão ativa.
- **Campanha Advantage+ completa (ex.: vendas Advantage+): normalmente não é o caso.** Esses formatos brilham em e-commerce com catálogo e milhares de eventos de compra. Negócio local que fecha no WhatsApp tem poucos eventos e funil fora do site — configure campanha manual com objetivo de mensagens/leads.
- **Criativo Advantage+ (variações automáticas de brilho, texto, música): teste com cautela.** Pode ajudar, mas em marca high-ticket (como o estúdio de tatuagem) as "melhorias" automáticas podem quebrar a estética. Revise cada aprimoramento ativado.

Resumo: **automação de entrega, sim; automação de estratégia, não.** Quem decide objetivo, oferta e funil é você; quem decide a quem entregar cada impressão é a máquina.

## 2. Objetivos certos para negócio local

### Click-to-WhatsApp: o formato-chave no Brasil

No Brasil, o funil de negócio local termina no WhatsApp — orçamento, agendamento e fechamento acontecem na conversa. A campanha com objetivo de **mensagens** (engajamento → apps de mensagem, direcionando para WhatsApp; nomes de menu mudam, verifique a interface vigente) faz o anúncio abrir diretamente uma conversa no WhatsApp do negócio, e o Meta otimiza a entrega para **pessoas propensas a iniciar conversa**.

Por que isso vence "cliques no site" para local:

- Elimina uma etapa inteira do funil (site → achar botão → WhatsApp). Cada etapa removida é atrito removido.
- O evento de otimização ("conversa iniciada") é muito mais próximo da venda do que "clique".
- O lead chega identificado (número de telefone real), não como visitante anônimo.

Requisitos mínimos: WhatsApp Business conectado à página do Facebook, **mensagem de saudação configurada** (o que a pessoa vê ao abrir a conversa — inclua uma pergunta que facilite o primeiro toque, ex.: "Oi! Quer orçamento de um projeto? Me conta a ideia e a região do corpo") e alguém que **responda em minutos, não horas**. Anúncio bom + resposta lenta = dinheiro queimado (ver diagnóstico).

Exemplo do estúdio: anúncio em vídeo do processo de uma tatuagem autoral → clique abre WhatsApp → saudação pergunta ideia + região do corpo → artista responde com portfólio direcionado e chama para orçamento. Todo o funil em uma tela.

### Campanhas de leads (formulário)

Objetivo de **cadastro/leads** (formulários instantâneos dentro do próprio Meta) serve quando: (a) o negócio precisa qualificar antes de conversar (ex.: financiamento, orçamento alto com triagem), ou (b) o volume de conversas do WhatsApp está sufocando o atendimento. Formulário nativo converte barato porque pré-preenche os dados, mas o lead é mais frio que quem abriu conversa por vontade própria — **a velocidade de contato pós-formulário decide tudo** (heurística de mercado consolidada: ligar/chamar em até 5-10 minutos multiplica a taxa de contato; após horas, o lead esfria drasticamente).

Para o estúdio de tatuagem: formulário com "estilo desejado + região do corpo + faixa de investimento" filtra curiosos antes do artista gastar tempo — útil quando a agenda está cheia e o problema é qualidade, não volume.

### Reconhecimento: quando (raramente) usar

Campanhas de reconhecimento/alcance otimizam para impressões baratas, não para ação. Para orçamento de R$ 20-100/dia, quase sempre é desperdício — você precisa de conversas, não de "lembrança de marca". Exceções legítimas:

- Inauguração/data específica com raio muito pequeno (ex.: martelar 2 km ao redor do ponto na semana de abertura).
- Negócio de ciclo longo construindo audiência quente barata para retargeting posterior (vídeo views custam centavos e criam público de "assistiu 50% do vídeo").

Se usar, que seja **minoria da verba (10-20%) e com propósito declarado** (alimentar retargeting), nunca a campanha principal.

### Por que não "impulsionar post"

O botão azul "Impulsionar" é a versão de brinquedo do Gerenciador de Anúncios:

1. **Objetivo errado por padrão**: impulsionamento otimiza para engajamento (curtidas, comentários) — o Meta encontra gente que curte, não gente que compra. Curtida não paga aluguel.
2. **Sem estrutura de teste**: um post impulsionado é 1 criativo, sem variações, sem comparação, sem aprendizado reaproveitável.
3. **Segmentação e otimização limitadas**: sem controle fino de evento de otimização, sem formulário nativo, com menos controle de posicionamento e destino.

O impulsionamento não é "errado" — é **incompleto**. Serve no máximo para dar gás em um post orgânico que já provou apelo (prova social barata). Estratégia de aquisição se monta no Gerenciador de Anúncios, sempre.

## 3. Pixel + API de Conversões: o mínimo viável

### Por que medir mesmo vendendo pelo WhatsApp

Mesmo com funil terminando no WhatsApp, medição importa por dois motivos: (1) retargeting — sem Pixel não existe público de "visitou o site"; (2) sinal — cada evento enviado ensina o algoritmo sobre quem é seu cliente.

### Setup mínimo viável (nesta ordem)

1. **Pixel da Meta instalado no site** (via Gerenciador de Eventos; se o site é WordPress/Wix/similar, use a integração oficial da plataforma). Se o negócio não tem site, o funil click-to-WhatsApp funciona sem Pixel — as conversas iniciadas são medidas pelo próprio Meta.
2. **Eventos que importam para local** (não instale vinte, instale estes):
   - `PageView` — automático; base para retargeting de visitantes.
   - `ViewContent` — página de serviço/portfólio vista (ex.: página "orçamento" do estúdio).
   - `Contact` ou `Lead` — clique no botão de WhatsApp do site / envio de formulário. **Este é o evento-rei do negócio local.**
   - `Schedule` (se houver agendamento online).
   - Ignore por ora: `AddToCart`, `Purchase` e afins — são de e-commerce; só entram se houver venda online de verdade.
3. **API de Conversões (CAPI)**: envia os mesmos eventos do servidor, em paralelo ao Pixel do navegador. Com bloqueadores de anúncio e restrições do iOS, o Pixel sozinho perde uma fatia relevante dos eventos; a CAPI recupera parte disso e melhora a correspondência. Mínimo viável: usar a **integração de parceiro** da própria plataforma do site (WordPress, Shopify, frameworks com gateway oficial) — configuração guiada, sem programar. Implementação manual de CAPI só se justifica com desenvolvedor disponível; não trave o lançamento por causa dela. Ordem de prioridade honesta: campanha rodando > Pixel > CAPI.
4. **Deduplicação**: se Pixel e CAPI enviam o mesmo evento, configure o ID de evento para não contar duas vezes (as integrações de parceiro fazem isso sozinhas — só confira no Gerenciador de Eventos se aparece "processado/desduplicado").

Verifique tudo com a aba de teste de eventos do Gerenciador de Eventos antes de escalar verba.

## 4. Criativo é o novo targeting

### A regra das 3-5 variações

Toda campanha entra no ar com **3 a 5 anúncios diferentes dentro do mesmo conjunto** — nunca 1. Motivo mecânico: o sistema de entrega testa os anúncios entre si e concentra verba no que gera evento mais barato. Com 1 anúncio, você não tem campanha, tem aposta.

As variações devem diferir em **ângulo**, não só em cor de fundo:

- **Ângulo 1 — Prova/processo**: vídeo do trabalho acontecendo (a tatuagem sendo feita, o antes/depois, o resultado cicatrizado).
- **Ângulo 2 — Dor/desejo do cliente**: "Cansado de orçamento de tatuagem que não entende sua ideia?" — fala do problema, não do produto.
- **Ângulo 3 — Prova social**: depoimento real de cliente, print de avaliação, reação ao ver o resultado.
- **Ângulo 4 — Oferta/CTA direto**: "Agenda de setembro aberta — 5 vagas para projetos autorais. Chama no WhatsApp."
- **Ângulo 5 — Bastidor/autoridade**: o artista explicando como cria um projeto, o estúdio por dentro.

### Anatomia do criativo que funciona em 2026

- **Formato vertical 9:16** como padrão (Reels e Stories são onde está a atenção barata). Versão 1:1 ou 4:5 para Feed quando fizer sentido.
- **Hook nos 2 primeiros segundos**: a decisão de deslizar acontece antes do 3º segundo. O primeiro frame precisa de movimento, rosto, resultado impactante ou frase de tensão em texto na tela. "Logo da empresa surgindo devagar" é assassinato de verba.
- **Estilo UGC (conteúdo com cara de usuário)**: vídeo gravado no celular, pessoa falando para a câmera, ritmo de conteúdo orgânico. Anúncio que parece anúncio é ignorado; anúncio que parece post de pessoa real ganha atenção emprestada do feed. Para high-ticket, UGC não significa desleixo — significa autenticidade com boa luz e bom áudio.
- **Legenda/texto na tela sempre**: maioria assiste sem som.
- **Um CTA único e concreto**: "Chama no WhatsApp e me conta sua ideia" supera "Saiba mais".

### Ciclo semanal de teste criativo

O trabalho recorrente do gestor não é mexer em público — é rodar esta esteira:

1. **Segunda**: olhar os últimos 7 dias por anúncio (não por campanha). Métricas: custo por conversa iniciada, CTR, taxa de retenção do vídeo (thumb-stop).
2. **Matar o perdedor**: anúncio com custo por conversa claramente acima da média da conta (heurística: >1,5-2x o melhor anúncio, com gasto suficiente para julgar — pelo menos ~3-5x o custo-alvo por conversa gasto nele) é pausado. Sem dó e sem "vai que melhora".
3. **Ler o vencedor**: o que o melhor anúncio tem? Ângulo? Hook? Formato? A hipótese vira insumo.
4. **Repor**: subir 1-2 criativos novos por semana, variações do vencedor (mesmo ângulo, hook diferente; ou mesmo hook, prova diferente). Nunca deixar a campanha "secar" até restar 1 anúncio.
5. **Escalar o vencedor devagar**: aumento de orçamento de no máximo ~20% a cada 2-3 dias (heurística para não resetar o aprendizado — ver seção 6). Dobrar a verba de um dia para o outro frequentemente encarece tudo.

Criativo cansa (frequência sobe, CTR cai, custo sobe — "fadiga de criativo"). Em contas pequenas com raio local, isso acontece rápido: o mesmo público vê o anúncio muitas vezes. Frequência semanal passando de ~3-4 com custo subindo = hora de trocar o criativo, não o público.

## 5. Públicos: amplo, raio e o pecado da micro-segmentação

### Comece amplo com raio geográfico

Para negócio local, a segmentação que importa é o **mapa**:

- Raio ao redor do ponto (ex.: 10-15 km do estúdio em Florianópolis; ajuste ao quanto o cliente viaja pelo serviço — por uma tatuagem de R$ 3.000 as pessoas cruzam a cidade; por um açaí, não).
- Idade em faixa larga e realista (ex.: 20-45), gênero só se o serviço for de fato específico de gênero.
- **Sem pilha de interesses.** Deixe aberto ou com no máximo 1 interesse amplo. O sistema de entrega encontra quem reage ao criativo com mais precisão do que qualquer combinação de interesses que você montaria.

### O anti-padrão: micro-segmentar

Empilhar "interessados em tatuagem" + "interessados em arte" + "excluir X" + faixa de 25-34 + posicionamento só em Stories cria um público minúsculo que: (a) encarece o leilão (menos gente = menos opção de impressão barata), (b) esgota em dias (frequência explode), (c) fragmenta os dados e prende a campanha na fase de aprendizado. Micro-segmentação é a ilusão de controle vendida como técnica. Em conta pequena, é o segundo erro mais comum depois do objetivo errado.

### Lookalike e retargeting: quando houver dados

- **Retargeting** (público de reengajamento): quem visitou o site (Pixel), interagiu com o Instagram/Facebook nos últimos X dias, assistiu Y% dos vídeos, ou mandou mensagem e não fechou. Vale a pena quando o público-fonte tem algumas centenas/milhares de pessoas — antes disso, a campanha de retargeting não tem a quem entregar. Verba: 10-20% do total. Criativo de retargeting é diferente do frio: mais oferta, mais urgência, mais prova ("Você viu nosso portfólio — a agenda do mês fecha sexta").
- **Lookalike (público semelhante)**: o Meta clona o perfil estatístico de uma fonte (lista de clientes, quem converteu). Só faz sentido com fonte de qualidade e volume razoável (heurística: centenas de registros; com 40 clientes, não). Para local com raio pequeno, lookalike importa menos — o raio já limita o universo, e o amplo-com-raio costuma bastar. Priorize: amplo → retargeting → lookalike, nessa ordem de maturidade da conta.

## 6. Fase de aprendizado: a regra do "não mexe"

### O que é

Quando um conjunto de anúncios é lançado (ou sofre edição significativa), o sistema de entrega entra em **fase de aprendizado**: período em que ele explora ativamente quem responde ao anúncio, com desempenho instável e custo geralmente mais alto. A saída da fase depende de acumular volume suficiente de eventos de otimização (a referência histórica é ~50 eventos por semana por conjunto — **verifique o número e as regras vigentes na Central de Ajuda antes de citar como fato**).

### Por que não mexer durante

Cada edição significativa **reseta** o aprendizado — o sistema descarta parte do que aprendeu e recomeça a explorar. Mexer na campanha a cada 2 dias é pagar o pedágio da instabilidade para sempre. Historicamente resetam o aprendizado (confirme na documentação vigente): mudança de evento de otimização, mudança grande de orçamento (daí a heurística dos ~20%), mudança de lance/meta de custo, edição de segmentação, troca/adição relevante de criativo no conjunto.

Não resetam (em geral): renomear coisas, mudar a programação futura, pausar/reativar rapidamente um anúncio individual.

### Disciplina prática

- Após lançar: **7 dias sem tocar** (exceto pausar anúncio individual claramente desastroso). Julgue com uma semana cheia de dados, nunca com 48h.
- "Aprendizado limitado" (o aviso da interface): significa que o conjunto não acumula eventos suficientes na velocidade necessária. As saídas reais são consolidar (menos conjuntos, mais verba em um), otimizar para evento mais frequente (conversa em vez de compra) ou aumentar orçamento — não criar mais uma campanha.
- Escalar = mexer. Por isso o escalonamento é gradual (~20% a cada 2-3 dias) e as trocas de criativo entram como **anúncios novos adicionados**, preferencialmente em dia fixo da semana, não como edições diárias dispersas.

## 7. Métricas e metas realistas (BR)

### Faixas de referência — heurísticas de operação, não benchmarks oficiais

A Meta não publica benchmark por país. As faixas abaixo vêm da prática de mercado em contas locais BR e servem só como régua inicial; os números da própria conta após 2-3 semanas substituem tudo isto:

| Métrica | Faixa heurística inicial (BR, local) | Leitura |
|---|---|---|
| CPM (custo por mil impressões) | ~R$ 10-40 (varia por cidade, nicho, época; dispara em novembro/dezembro) | CPM alto isolado não é problema — é o custo por conversa que manda |
| CTR (taxa de cliques no link) | ~0,8-2%+ | Abaixo de ~0,7% consistente = criativo/oferta fracos |
| Custo por conversa iniciada (WhatsApp) | ~R$ 3-20 (serviço comum) / ~R$ 15-50 (high-ticket como tatuagem autoral) | A métrica operacional central do funil local BR |
| Custo por lead (formulário) | ~R$ 5-30 | Lead de formulário é mais frio; compare custo por lead **qualificado**, não bruto |

### A conta que fecha o ROAS real

Custo por conversa é meio do funil. O que decide se a campanha vive ou morre:

```
Taxa de fechamento = vendas / conversas iniciadas
CAC real           = custo por conversa ÷ taxa de fechamento
ROAS real          = ticket médio ÷ CAC real
```

Exemplo do estúdio: R$ 25 por conversa, 10 conversas/semana, 2 fechamentos (taxa de 20%), ticket médio R$ 2.000. CAC real = R$ 125. ROAS real = 16x. **Essa campanha é uma máquina de imprimir dinheiro mesmo com "custo por conversa alto"** — enquanto um e-commerce de camiseta acharia R$ 25/conversa impagável. Ticket define tudo; nunca julgue custo por conversa sem o ticket ao lado.

Obrigação operacional: manter registro (planilha simples serve) de conversas → orçamentos enviados → fechamentos → valor. Sem isso, a "otimização" é cega e a conversa com o cliente da consultoria não tem número para mostrar. Esse registro também revela o vazamento mais comum: **taxa de fechamento baixa não é problema de anúncio — é problema de atendimento, tempo de resposta ou oferta** (ver diagnóstico).

## 8. Diagnóstico

### Anúncio caro (custo por conversa acima da meta)

Investigue na ordem, cada suspeito com sua métrica:

1. **Criativo** (suspeito nº 1 em ~70% dos casos — heurística): CTR baixo (<0,7-0,8%) e/ou retenção de vídeo fraca (poucos passam de 3s)? As pessoas nem estão parando no anúncio. Correção: novos hooks, novo ângulo, formato UGC. Não mexa em mais nada antes de descartar este.
2. **Oferta/mensagem**: CTR saudável mas pouca conversa iniciada? As pessoas clicam e desistem diante do que encontram. A promessa do anúncio é vaga ("qualidade e tradição") ou não há razão para agir agora? Correção: CTA concreto, oferta com prazo/escassez verdadeira, alinhamento anúncio → saudação do WhatsApp.
3. **Destino (WhatsApp/página)**: conversas iniciadas mas nada vira orçamento/venda? Meça o **tempo de primeira resposta**. Resposta em horas mata lead pago; saudação sem pergunta trava o papo; página lenta (>3s) derruba quem clicou. Este é o vazamento invisível: a campanha parece cara, mas quem está caro é o atendimento.
4. **Público/leilão**: só depois de descartar os três acima. Frequência >3-4 com custos subindo = fadiga (trocar criativo, avaliar ampliar raio). CPM muito acima do histórico da conta = sazonalidade de leilão (Black Friday, dezembro, eleições) ou público estrangulado por micro-segmentação.

### Anúncio reprovado

- Leia o motivo no Gerenciador e a Política de Anúncios vigente (as regras mudam; verifique a página oficial no momento — ver Fontes oficiais). Causas frequentes em local BR: alegações de resultado pessoal ("elimine a flacidez", "antes/depois" em saúde/estética), texto que afirma atributos pessoais do usuário ("você que está acima do peso..."), marcas registradas, categorias sensíveis.
- Tatuagem: cuidado com nudez/pele em excesso no enquadramento — reprovação comum e evitável no corte da imagem.
- Corrija e reenvie, ou peça **revisão manual** se a reprovação parecer erro do sistema automático (acontece com frequência e a revisão humana frequentemente reverte).
- **Nunca** tente "burlar" reprovação repetida com truques (texto na imagem para enganar, contas alternativas): reprovações acumuladas são sinal negativo na conta e caminho direto para restrição.

### Conta restrita

- Prevenção vale mais que cura: verificação da empresa no Gerenciador de Negócios, método de pagamento estável, domínio verificado, admins com contas pessoais antigas e reais, **crescimento de gasto gradual** (conta nova saindo de R$ 0 para R$ 500/dia em uma semana é padrão de fraude aos olhos do sistema).
- Se restringir: usar o canal oficial de contestação na Central de Ajuda (Qualidade da Conta), com calma e uma única contestação bem-feita. Contestar repetidamente com pressa costuma piorar.
- Enquanto isso, não criar contas paralelas com os mesmos ativos (mesmo cartão, mesmo domínio, mesmos admins) — o sistema vincula e derruba tudo junto, incluindo o Gerenciador de Negócios inteiro.
- Estruturalmente: página do Facebook e WhatsApp Business do **cliente**, Gerenciador de Negócios do **cliente**, e o consultor como parceiro/funcionário com acesso. Nunca rodar a verba do cliente em conta própria do consultor — restrição na conta do consultor não pode significar apagão de todos os clientes.

## Checklist de lançamento (resumo operacional)

1. WhatsApp Business conectado à página + saudação com pergunta configurada + responsável por responder em minutos definido.
2. Pixel instalado e evento `Contact`/`Lead` testado (se houver site). CAPI via integração de parceiro se disponível.
3. 1 campanha, objetivo de mensagens (WhatsApp), 1 conjunto: raio geográfico + faixa etária larga, sem pilha de interesses.
4. 3-5 criativos verticais com hook nos 2 primeiros segundos, ângulos diferentes, legenda embutida, CTA único.
5. Orçamento concentrado (R$ 20-100/dia num conjunto só). 7 dias sem mexer.
6. Planilha de conversas → fechamentos → valor desde o dia 1.
7. Toda segunda: ciclo de teste criativo (matar perdedor, ler vencedor, repor 1-2, escalar ~20%).

## Anti-padrões (o que NÃO fazer)

- Impulsionar post como estratégia de aquisição.
- 6 campanhas de R$ 10/dia "para testar" — nenhuma sai do aprendizado.
- Micro-segmentar por pilha de interesses em cidade média.
- Mexer na campanha a cada 48h e resetar o aprendizado em loop.
- Julgar campanha por curtidas, alcance ou CPM isolado.
- Otimizar para cliques quando o objetivo é conversa/venda.
- Rodar anúncio excelente com WhatsApp que responde em 6 horas.
- Escalar dobrando orçamento de um dia para o outro.
- Citar benchmark de mercado como se fosse número oficial da Meta.
- Rodar a verba do cliente na conta de anúncios do consultor.

## Fontes oficiais

Verifique sempre no momento da execução — interface, políticas e regras de aprendizado mudam com frequência:

- Meta Ads (anúncios no Facebook/Instagram): https://www.facebook.com/business/ads
- Meta Business Suite: https://www.facebook.com/business/tools/meta-business-suite
- WhatsApp Business: https://business.whatsapp.com
- Instagram para empresas: https://business.instagram.com
