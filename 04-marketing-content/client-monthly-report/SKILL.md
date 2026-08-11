---
name: client-monthly-report
description: Monthly results report for Brazilian local business clients, written in plain PT-BR for non-technical owners — fixed structure (5-line jargon-free executive summary, month's funnel with real numbers, per-channel KPIs with variation, what was done, what we learned, next month's plan, investment recommendation), honest about what did not work, designed to renew trust and justify the retainer every month. Consumes the data model defined in the marketing-measurement skill. Use when closing a client's month, writing or reviewing a monthly report, or preparing a results conversation. Trigger on "relatório mensal do cliente", "fechar o mês do cliente", "relatório de resultados", "prestar contas pro cliente", "mostrar resultado do mês", "renovar o contrato", "monthly client report", "monthly results report", "client reporting".
---

# Relatório Mensal de Resultados

## O que é este documento

Este é o manual do **relatório mensal** que a consultoria entrega a cada cliente no fechamento do mês. Ele é escrito para dois leitores: o consultor (ou agente de IA) que redige o relatório, e o **dono do negócio** que o recebe — um leitor inteligente, ocupado e leigo em marketing, que quer saber três coisas: *o que eu ganhei com isso, o que vocês fizeram, e vale a pena continuar pagando?*

O relatório mensal é o momento em que o retainer é **renovado na cabeça do cliente** — todo mês, antes de qualquer boleto. Um contrato de R$ 3.000/mês não é cancelado no dia do cancelamento; é cancelado nos 3 meses anteriores, em que o cliente recebeu relatórios que não entendeu, ou não recebeu nenhum. O relatório existe para que a pergunta "isso está valendo a pena?" seja respondida antes de ser feita.

**Princípio central: confiança se renova com clareza + honestidade, não com números bonitos.** Um relatório que só mostra vitórias é lido como propaganda. Um relatório que mostra o que funcionou, o que não funcionou e o que será feito a respeito é lido como trabalho de gente séria — e gente séria não se troca por concorrente mais barato.

---

## De onde vêm os números

O relatório **consome** os dados definidos na skill `marketing-measurement` — ele não inventa fontes nem cria métricas novas no dia do fechamento. Fontes canônicas:

| Dado | Fonte |
|---|---|
| Visitas ao site e origem | GA4 |
| Impressões e cliques na busca Google | Search Console |
| Alcance, perfil, cliques no link | Insights nativos do Instagram |
| Visualizações, rotas, ligações, cliques | Desempenho do Perfil da Empresa no Google |
| Cliques no WhatsApp por canal | Links wa.me rastreados + evento de conversão no GA4 |
| Conversas, orçamentos e fechamentos | Registro comercial do WhatsApp (etiquetas / planilha do cliente) |

Regras de integridade — inegociáveis:

- **Nunca inventar, estimar sem rótulo, ou "arredondar para cima".** Se um dado não existe, o relatório diz "ainda não medimos isso; passa a ser medido a partir de [mês]". Instrumentação incompleta é achado de trabalho, não vergonha a esconder.
- **Todo número comparado.** Número solto não informa. Sempre: vs. mês anterior, e (quando houver histórico) vs. média dos últimos 3 meses. Variação sempre com sinal e contexto.
- **Separar o que a consultoria controla do que não controla.** Alcance caiu no mês em que o Instagram mudou distribuição ou o cliente viajou 2 semanas? Diga. Sem virar desculpa crônica: se o fator externo se repete 3 meses, ele é estrutural e o plano precisa absorvê-lo.

---

## A estrutura fixa (7 seções, sempre nesta ordem)

A estrutura não muda de mês a mês. Repetição é recurso: o cliente aprende a ler o relatório, compara meses com facilidade e sente previsibilidade — que é o que se compra num retainer.

### 1. Resumo executivo (5 linhas, zero jargão)

As 5 linhas que o dono lê no celular entre dois atendimentos. Cada linha, uma informação:

1. O resultado do mês em linguagem de negócio (conversas/orçamentos/clientes, não "impressões").
2. A melhor notícia do mês, com número.
3. A pior notícia do mês, com número — dita com a mesma franqueza.
4. O que foi feito (resumo em 1 linha).
5. A prioridade do mês que vem.

**Teste de jargão:** se qualquer palavra dessas 5 linhas precisaria de explicação (CTR, alcance orgânico, sessão, conversão), troque a palavra. "Cliques no botão do WhatsApp" no lugar de "conversões"; "pessoas que viram o perfil" no lugar de "alcance".

### 2. O funil do mês (com números)

Um desenho simples, o mesmo todo mês, mostrando o caminho do estranho até o cliente:

```
Pessoas alcançadas (Instagram + Google + site)      41.200  (▲ +18%)
        │
Visitas ao perfil / site                             2.910  (▲ +12%)
        │
Conversas iniciadas no WhatsApp                         74  (▲ +23%)
        │
Orçamentos enviados                                     31  (▲ +7%)
        │
Fechamentos                                              9  (▼ −10%)
        │
Receita atribuída (informada pelo cliente)       R$ 38.500
```

Duas frases de leitura obrigatórias abaixo do funil: **onde o funil melhorou** e **onde ele vaza mais** (no exemplo: mais conversas do que nunca, mas a taxa orçamento→fechamento caiu — a conversa do mês é sobre follow-up, não sobre posts). O funil transforma "marketing" em um encanamento que o dono enxerga.

### 3. KPIs por canal (com variação)

Uma tabela por extenso, 3-6 linhas por canal ativo, sempre com variação e uma observação em linguagem humana:

| Canal | Indicador | Este mês | Mês anterior | Variação | Leitura |
|---|---|---|---|---|---|
| Instagram | Contas alcançadas | 38.400 | 31.100 | ▲ +23% | 2 Reels puxaram o mês |
| Instagram | Cliques no link (WhatsApp) | 214 | 166 | ▲ +29% | Nova bio + CTA nos Reels |
| Google (Perfil) | Visualizações do perfil | 4.180 | 3.950 | ▲ +6% | — |
| Google (Perfil) | Cliques para ligar/WhatsApp | 58 | 41 | ▲ +41% | Fotos novas + posts semanais |
| Site | Visitas | 890 | 940 | ▼ −5% | Queda sazonal; busca estável |
| WhatsApp | Conversas novas | 74 | 60 | ▲ +23% | 46 do Instagram, 19 do Google, 9 diretas |

Regra: **máximo 3-6 indicadores por canal** — os que se conectam ao funil. Relatório com 40 métricas é onde a confiança vai morrer de tédio. Métricas de vaidade (seguidores, curtidas) podem aparecer, no fim, como contexto — nunca como resultado.

### 4. O que foi feito

A prestação de contas do trabalho — lista objetiva, verificável, sem inflar:

- 16 de 18 peças do calendário publicadas (2 adiadas por falta de material do cliente — combinado plano B abaixo)
- 4 posts no Perfil da Empresa no Google + 11 avaliações respondidas
- Página "Tatuagem realista em Florianópolis" publicada no site
- Follow-up padronizado implantado no WhatsApp (etiquetas + 2 mensagens)

Este bloco responde à pergunta silenciosa "pelo que estou pagando?" antes que ela vire pergunta em voz alta. Se o mês teve menos entrega que o combinado, diga e diga por quê — o cliente sempre percebe; o que ele não perdoa é fingir que não houve.

### 5. O que aprendemos (inclusive o que não funcionou)

A seção que diferencia consultoria de fornecedor de posts. 2-4 aprendizados no formato **teste → resultado → decisão**:

- *Carrosséis de "estilos de tatuagem" tiveram 3x mais salvamentos que a média → viram série mensal.*
- *Os 2 Reels com trend de áudio não geraram nenhuma conversa, apesar do alcance → cortados; alcance sem conversa não paga sessão.*
- *Metade dos orçamentos sem resposta era enviada depois das 19h → orçamento agora sai até as 18h, follow-up no dia seguinte.*

Fracasso relatado com decisão anexada **aumenta** a confiança; fracasso omitido e descoberto pelo cliente a destrói. Nunca relatar erro sem a decisão correspondente — erro sem decisão é só má notícia.

### 6. Plano do próximo mês

3-5 prioridades, cada uma ligada a algo das seções 2, 3 ou 5 (nada de plano genérico caído do céu):

1. **Atacar o vazamento orçamento→fechamento** (seção 2): implantar cadência de follow-up de 3 toques — meta: taxa de fechamento de volta a 35%+.
2. **Dobrar a série de carrosséis vencedora** (seção 5): 2/mês no calendário de novembro.
3. **Abrir a agenda de dezembro na 1ª semana** com campanha de venda (10% do mix).

Cada prioridade com meta verificável no próximo relatório — é isso que fecha o ciclo mensal *planejar → executar → medir → aprender*.

### 7. Recomendação de investimento

Fecho consultivo, em 3-6 linhas: o que fazer com o dinheiro e o esforço no próximo mês.

- **Manter / realocar / adicionar** — ex.: *"Recomendo manter o escopo atual e realocar 2h/mês de produção de Stories para responder orçamentos mais rápido — é onde o funil mais vaza."*
- Se houver mídia paga ou upgrade de escopo a propor, propor **com base no gargalo identificado**, com valor e resultado esperado honesto (ex.: *"R$ 600/mês em anúncios no Google para as buscas que já convertem — expectativa realista: +15-25 conversas/mês; testável por 60 dias"*).
- Se o mês foi ruim, esta seção é obrigatoriamente sóbria: nunca propor aumento de escopo num mês ruim sem antes mostrar a correção de rota.

---

## Tom e linguagem (regras de redação)

- **PT-BR, 100% para leigo.** Tabela de tradução mínima: impressões → "vezes que apareceu"; alcance → "pessoas que viram"; CTR → "de cada 100 que viram, X clicaram"; conversão → "virou conversa no WhatsApp"; sessões → "visitas ao site".
- **Linguagem de dono, não de agência.** O sujeito das frases é o negócio do cliente, não a consultoria. "O estúdio recebeu 74 conversas" em vez de "entregamos 74 leads".
- **Honestidade calibrada, não autoflagelo.** Uma pior-notícia clara com plano anexado por relatório. Não transformar o relatório em pedido de desculpas — nem em desfile.
- **Curto.** 2-4 páginas. O detalhe fica em anexo (dashboard, planilha) para quem quiser mergulhar.
- **Mesmo formato todo mês.** Mudou a estrutura, o cliente perdeu a régua de comparação.
- **Entrega com conversa.** O relatório vai por escrito e é apresentado em 15-20 min (chamada ou áudio) — o documento renova a confiança; a conversa renova a relação.

---

## Workflow de produção (fechamento do mês)

1. **Coletar** os dados das fontes canônicas (dias 1-3 do mês seguinte) conforme `marketing-measurement`; pedir ao cliente os números que só ele tem (fechamentos, receita).
2. **Montar o funil** e localizar o maior vazamento do mês.
3. **Escrever as seções 2-5** (números antes da narrativa — a narrativa sai dos números, nunca o contrário).
4. **Escrever o plano (6) e a recomendação (7)** amarrados aos achados.
5. **Escrever o resumo executivo (1) por último** — é impossível resumir bem antes de saber o que o mês disse.
6. **Passar o teste de jargão** no documento inteiro.
7. **Entregar + apresentar em 15-20 min**, terminando na prioridade nº 1 do próximo mês.
8. **Alimentar o próximo ciclo:** os aprendizados da seção 5 entram como insumo do calendário do mês seguinte (skill `content-calendar-engine`).

---

## Anti-padrões (o que NUNCA fazer)

- **Relatório-print.** Capturas de tela do Instagram Insights coladas num PDF não são relatório — são lição de casa não feita.
- **Só boas notícias.** Cliente não é bobo: quando tudo é vitória e a agenda dele continua igual, quem perde credibilidade é o relatório.
- **Métricas de vaidade como manchete.** "Crescemos 800 seguidores" na primeira linha, com zero conversas a mais, é o começo do cancelamento.
- **Número sem comparação, comparação sem leitura.** "▼ −12%" sem uma frase dizendo por que e o que será feito é pior que não reportar.
- **Jargão.** Cada termo técnico não traduzido é uma pequena expulsão do leitor do próprio relatório.
- **Culpar o algoritmo.** Fator de plataforma pode ser citado como contexto verificado (ver regra de frescor), nunca como desculpa recorrente.
- **Plano do próximo mês desconectado dos dados do mês.** É o sintoma nº 1 de relatório de fachada.
- **Atrasar.** Relatório do mês entregue dia 20 comunica desorganização mais alto do que qualquer número comunica competência. Prazo: até o 5º dia útil.

## Regra de frescor (obrigatória)

Métricas nativas mudam de nome, definição e disponibilidade a cada trimestre (Instagram Insights, Desempenho do Perfil da Empresa no Google, relatórios do GA4). **Antes de citar qualquer métrica ou comportamento de plataforma no relatório, verifique a documentação oficial no momento da execução** (links abaixo) — especialmente ao explicar uma queda por "mudança do algoritmo": afirmação sobre plataforma sem fonte oficial deve ser rotulada como **hipótese/heurística** no próprio relatório, nunca como fato.

## Fontes oficiais

- GA4 — https://support.google.com/analytics
- Search Console — https://support.google.com/webmasters
- Perfil da Empresa no Google — https://support.google.com/business
- Instagram para empresas — https://business.instagram.com
- Meta Business Suite — https://www.facebook.com/business/tools/meta-business-suite
- WhatsApp Business — https://business.whatsapp.com
- Meta Ads — https://www.facebook.com/business/ads
- Ajuda YouTube — https://support.google.com/youtube
- TikTok Creator Academy — https://www.tiktok.com/creator-academy
