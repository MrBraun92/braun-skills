---
name: linkedin-mcp-operator
description: >-
  Opera ferramentas MCP autorizadas para ler e pesquisar dados do LinkedIn, auditar o
  próprio perfil e configurações, buscar pessoas, empresas, funcionários, vagas, posts,
  feed e conversas, e preparar ações com confirmação humana. Trigger on LinkedIn MCP,
  buscar pessoas LinkedIn, pesquisar recrutadores, funcionários de empresa, vagas LinkedIn,
  ler perfil, settings LinkedIn, boolean search, inbox, enviar mensagem ou conexão.
---

# LinkedIn MCP Operator

## Objetivo

Fornecer a camada operacional do LinkedIn Skills Pack. Esta skill executa leitura, busca, coleta e preparação de ações usando apenas ferramentas autorizadas e disponíveis. Estratégia e redação devem ser encaminhadas às skills especializadas.

## Regras de segurança e conformidade

- Usar apenas conta e sessão autorizadas pelo usuário.
- Não burlar autenticação, limites, CAPTCHA ou controles da plataforma.
- Não executar scraping massivo.
- Não enviar convites, mensagens, comentários ou posts sem confirmação explícita.
- Não automatizar outreach em escala.
- Não coletar dados sensíveis desnecessários.
- Minimizar e estruturar os dados coletados.
- Informar quando uma função não estiver disponível ou estiver instável.
- Não prometer suporte a configurações que a ferramenta não consegue ler.

## Catálogo de capacidades

Quando suportado pelo MCP conectado:

### Perfil próprio

- obter perfil autenticado;
- selecionar seções: experiências, educação, certificações, skills, projetos, idiomas, contato e posts;
- comparar o perfil real com o diagnóstico de `linkedin-profile-optimizer`;
- identificar campos ausentes;
- verificar coerência de cargo, área, senioridade, localização e setor.

### Perfis de terceiros

- ler perfis públicos acessíveis;
- pesquisar pessoas por palavras-chave;
- filtrar por localização, grau de conexão, empresa atual e outros filtros suportados;
- coletar apenas informações necessárias para networking ou benchmark.

### Empresas

- obter perfil da empresa;
- pesquisar empresas;
- ler posts e vagas;
- localizar funcionários;
- identificar gestores, recrutadores e possíveis hiring managers.

### Vagas

- pesquisar vagas por cargo, palavras-chave e localização;
- abrir detalhes;
- extrair requisitos e keywords;
- encaminhar vagas ao sistema de job search e ao profile optimizer.

### Feed e conteúdo

- ler feed;
- obter posts próprios e de empresas;
- reunir contexto para conteúdo e comentários;
- preparar respostas;
- encaminhar ao `linkedin-content-strategist`.

### Inbox e relacionamentos

- listar conversas;
- ler conversa específica;
- pesquisar mensagens;
- preparar respostas;
- enviar apenas após confirmação.

### Conexões

- identificar perfis recomendados;
- preparar convite com nota;
- aceitar ou enviar conexão somente após confirmação;
- registrar motivo e resultado.

### SSI

- recuperar o SSI real apenas se a integração suportar explicitamente;
- caso contrário, pedir screenshot ou os quatro valores;
- encaminhar ao `linkedin-ssi-network-strategist`;
- nunca inferir score oficial.

## Busca booleana

Construir consultas com base em cargo-alvo, equivalentes PT/EN, senioridade, área, empresa e localização.

Exemplos conceituais:

- `(“AI Product Manager” OR “AI Product Lead” OR “Product Manager AI”) AND (Brazil OR Remote)`
- `(Recruiter OR “Talent Acquisition”) AND (AI OR Artificial Intelligence) AND CompanyName`
- `(“Strategy & Operations” OR “Business Operations”) AND AI`

Usar somente sintaxe suportada pela ferramenta/interface atual. Não prometer filtros inexistentes.

## Auditoria de configurações

Se a ferramenta conseguir ler settings, capturar como checklist booleano:

- perfil público;
- foto e visibilidade;
- localização;
- industry;
- Open to Work;
- cargos desejados;
- localizações desejadas;
- tipos de trabalho;
- remoto/híbrido/presencial;
- visibilidade do Open to Work;
- follow/connect;
- idiomas;
- contato;
- URL personalizada;
- recursos de criação, newsletter ou serviços disponíveis.

Quando não houver acesso programático, gerar checklist e solicitar screenshots ou confirmação manual. Não inventar o estado.

## Workflows

### A. Benchmark de cargo-alvo

1. Receber cargo, senioridade e mercado.
2. Pesquisar vagas e profissionais.
3. Extrair termos recorrentes.
4. Separar keywords de skills, ferramentas, metodologias e conhecimentos.
5. Entregar dados ao profile optimizer.

### B. Mapa de pessoas certas

1. Receber empresas e cargos-alvo.
2. Pesquisar recrutadores, gestores, pares e alumni.
3. Classificar relevância.
4. Identificar contexto genuíno para conexão.
5. Entregar ao SSI/network strategist.

### C. Inteligência de oportunidade

1. Ler empresa, vagas, funcionários e posts.
2. Detectar sinais de contratação, expansão ou projeto.
3. Identificar contatos adequados.
4. Produzir briefing com evidências.
5. Preparar abordagem, sem enviar automaticamente.

### D. Auditoria do perfil real

1. Ler perfil autenticado.
2. Comparar com checklist normativo.
3. Marcar campos como presente, ausente, incoerente ou não verificável.
4. Encaminhar reescritas ao profile optimizer.

### E. Conteúdo assistido

1. Ler posts e feed relevantes.
2. Coletar contexto e fontes.
3. Encaminhar ao content strategist.
4. Preparar ação.
5. Solicitar confirmação para publicar ou comentar.

## Registro de ações

Para cada operação, registrar:

- objetivo;
- ferramenta usada;
- consulta;
- itens lidos;
- dados retidos;
- recomendação;
- ação preparada;
- confirmação do usuário;
- resultado ou erro.

## Entregáveis

1. Dados estruturados e deduplicados.
2. Evidências e URLs/perfis quando permitido.
3. Checklist de configurações verificadas.
4. Consultas booleanas.
5. Lista priorizada de pessoas, empresas ou vagas.
6. Briefing antes de qualquer ação.
7. Log de confirmação e execução.
