---
name: similarweb-analytics
description: >-
  Website traffic intelligence without paid APIs: estimates traffic, ranking, traffic sources,
  geography and engagement for any domain using the public SimilarWeb website, Google Trends,
  manual SERP analysis and the client's own GA4/Search Console data. Use when researching a
  competitor's traffic, sizing a market, or benchmarking a client site against rivals.
  Trigger on quanto trafego tem o site, analisar concorrente, trafego do concorrente,
  ranking do site, fontes de trafego, de onde vem as visitas, benchmark de sites,
  website traffic, competitor traffic analysis, SimilarWeb, domain research, traffic sources.
---

# SimilarWeb Analytics — Inteligência de Tráfego Portável

Análise de tráfego, ranking, fontes de visitas, geografia e engajamento de qualquer site — **sem depender de API paga nem de runtime especial**. Esta skill funciona em qualquer máquina usando apenas navegador/WebFetch e fontes públicas.

## O que esta skill entrega

- **Tráfego**: estimativa de visitas mensais e tendência (subindo/caindo)
- **Ranking**: posição global, por país e por categoria
- **Fontes de tráfego**: busca orgânica, busca paga, direto, social, referrals, e-mail
- **Geografia**: principais países de origem das visitas
- **Engajamento**: taxa de rejeição, páginas por visita, duração média da visita
- **Benchmark competitivo**: comparação lado a lado entre o site do cliente e concorrentes

## Método 1 — Página pública do SimilarWeb (principal)

O SimilarWeb publica gratuitamente um resumo por domínio em:

```
https://www.similarweb.com/website/DOMINIO/
```

Exemplo: `https://www.similarweb.com/website/besourotattoo.com.br/`

**Como usar:** abra a URL com WebFetch ou no browser e extraia da página pública:
- Rank global, rank no país, rank na categoria
- Total de visitas do último mês e variação mensal
- Bounce rate, páginas por visita, duração média
- Top países e divisão de canais (gráficos "Marketing Channels" e "Top Countries")
- Principais palavras-chave orgânicas (amostra limitada na versão grátis)

**Limitações da versão pública (avisar sempre ao cliente):**
- Sites com pouco tráfego (regra prática: abaixo de ~5 mil visitas/mês) aparecem como "não há dados suficientes". Isso é o caso da maioria dos negócios locais brasileiros — um estúdio de tatuagem em Florianópolis quase nunca terá dados no SimilarWeb. Para negócio local, o benchmark relevante é Perfil da Empresa no Google + Instagram, não SimilarWeb.
- Números são **estimativas por modelagem**, não medição direta. Trate como ordem de grandeza, nunca como valor exato.
- Histórico limitado a ~3 meses na versão grátis.
- A página pode exigir interação no browser (scroll, consentimento de cookies) para carregar todos os blocos; se o WebFetch retornar vazio, usar o browser.

## Método 2 — Google Trends (demanda relativa)

Quando o SimilarWeb não tem dados (sites pequenos/locais), o Google Trends mede a **demanda pela marca e pelo tema**:

```
https://trends.google.com.br/trends/explore?q=TERMO&geo=BR
```

**Usos práticos:**
- Comparar interesse de busca entre marcas concorrentes (até 5 termos simultâneos)
- Ver sazonalidade do nicho (ex.: "tatuagem" cresce no verão? antes de eventos?)
- Filtrar por estado/cidade (`geo=BR-SC`) para demanda local
- "Assuntos relacionados" e "pesquisas relacionadas" revelam termos em alta no nicho

Trends mostra **interesse relativo (0–100)**, não volume absoluto. Serve para comparação e tendência, não para dizer "X pessoas buscaram".

## Método 3 — Análise SERP manual (quem captura a demanda)

Buscar no Google os termos comerciais do nicho e mapear quem aparece:

1. Listar 5–10 termos que um cliente digitaria (ex.: "tatuagem fine line florianópolis", "estúdio de tatuagem campeche")
2. Para cada termo, registrar: quem está no pack local do Maps, quem está no top 10 orgânico, quem anuncia
3. Montar tabela concorrente × termo → revela quem domina a captura de demanda mesmo sem dados de tráfego
4. Clicar nos sites do top 3 e observar: para onde direcionam o clique? No Brasil, negócio local bem otimizado direciona para o **WhatsApp** — se o concorrente força formulário ou e-mail, isso é fraqueza explorável no funil do cliente

Usar janela anônima ou avisar que resultados são personalizados por localização/histórico.

## Método 4 — Dados do próprio cliente (GA4 + Search Console)

Quando o cliente dá acesso, os dados dele são a única fonte **medida** (não estimada):

- **GA4**: visitas reais, fontes de tráfego reais, geografia real, engajamento real. Comparar com as estimativas do SimilarWeb dos concorrentes (mesma ordem de grandeza? canal dominante diferente?)
- **Search Console**: consultas que geram impressão/clique, posição média, páginas que rankeiam. Cruzar com a análise SERP manual: termos onde o cliente tem impressão mas não clique = oportunidade de título/descrição
- Métrica de funil que importa para negócio local BR: **cliques no botão de WhatsApp** (configurar como evento-chave no GA4). Tráfego sem conversa iniciada no WhatsApp é vaidade

## Roteiro de benchmark competitivo (passo a passo)

1. Definir 3–5 concorrentes diretos com o cliente
2. Para cada domínio, coletar a página pública do SimilarWeb (Método 1); registrar "sem dados" quando for o caso — isso também é informação (concorrente pequeno)
3. Rodar Google Trends comparando as marcas + termos do nicho (Método 2)
4. Mapear a SERP dos termos comerciais (Método 3)
5. Cruzar com GA4/Search Console do cliente (Método 4)
6. Entregar tabela única: domínio × visitas estimadas × canal dominante × posição SERP × presença local × destino do clique (WhatsApp? formulário?)
7. Recomendar 3 ações priorizadas por impacto no funil (que no Brasil termina no WhatsApp)

## O que SÓ é possível com a API paga do SimilarWeb

Ser honesto com o cliente sobre o teto da versão gratuita. Exigem assinatura paga (Web Intelligence / API):

- Histórico longo (12–36 meses) e granularidade diária/semanal
- Lista completa de palavras-chave orgânicas e pagas por concorrente
- Divisão desktop × mobile detalhada
- Sites de baixo tráfego com estimativa (a versão paga cobre mais domínios pequenos, ainda assim com margem de erro alta)
- Dados de apps, audiência demográfica, jornada entre sites, export em massa via API

Se o projeto exigir isso, a recomendação é orçar a assinatura — nunca fingir precisão que a fonte gratuita não tem.

## Regra de frescor

Layout da página pública do SimilarWeb, limites da versão grátis e URLs do Google Trends mudam com frequência. **Sempre verificar no momento da execução** o que a página realmente exibe antes de prometer um dado ao cliente. Todo número de tráfego de terceiros deve ser rotulado como **estimativa**; heurísticas desta skill (ex.: corte de ~5 mil visitas/mês) são heurísticas, não regra oficial da plataforma.

## Fontes oficiais

- SimilarWeb: https://www.similarweb.com
- Google Trends: https://trends.google.com.br
- Google Search Central: https://developers.google.com/search/docs?hl=pt-br
- GA4 (Central de Ajuda): https://support.google.com/analytics
- Search Console (Central de Ajuda): https://support.google.com/webmasters
- Perfil da Empresa no Google: https://support.google.com/business
