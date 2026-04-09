---
name: skill-router
description: 'Read this skill IMMEDIATELY in two situations: (1) whenever the user asks Claude to use its installed skills in any language — "use suas skills", "use your skills", "usando suas skills instaladas", "use o máximo de skills", "trabalhe com suas capacidades completas", "faça novamente usando as skills", "apply all your skills", "use todas as skills disponíveis"; (2) whenever the user describes a problem or situation in natural/non-technical language and it''s unclear which specialist skill should handle it. This skill translates what the user actually means — regardless of technical vocabulary — into the correct specialist skill(s). Essential for non-technical users who describe problems in plain language rather than dev/product jargon.'
---

# Skill Router

## Purpose

Este skill faz duas coisas:

1. **Captura meta-pedidos** — quando o usuário pede para usar as skills sem especificar qual
2. **Traduz linguagem natural → skill técnica** — quando o usuário descreve um problema com suas próprias palavras (não em jargão técnico) e Claude precisa identificar qual especialista resolver

O usuário pode não saber os nomes das áreas. Pode dizer "isso tá quebrado" em vez de "performance issue". Pode dizer "quero que fique mais bonito" em vez de "interface design critique". Pode dizer "isso não faz sentido" em vez de "workflow analysis". Esse skill reconhece a intenção real por trás da linguagem e rota para o especialista certo.

---

## Passo 1 — Identificar o que o usuário realmente quer

Antes de qualquer coisa, leia o histórico da conversa e a mensagem atual. Pergunte-se: **qual é o problema real sendo descrito?**

### Tabela de tradução: linguagem natural → skill

#### Linguagem sobre código / sistema

| O usuário diz (em qualquer língua) | Skill a usar |
|---|---|
| "revise meu código", "audit this", "esse código tá bom?", "o que tem de errado aqui?", "melhore isso" + código anexado | `code-auditor` |
| "como organizar isso?", "a estrutura tá boa?", "como os módulos conversam?", "isso vai escalar?", "architecture review" | `code-architect` |
| "tá lento", "demora muito", "as queries estão pesadas", "otimize a performance", "por que isso trava?" | `performance-reviewer` |
| "isso é seguro?", "tem vulnerabilidade?", "como proteger?", "a autenticação tá certa?", "alguém pode hackear?" | `security-reviewer` |
| "como modelar os dados?", "que tabelas usar?", "qual a relação entre X e Y?", "revise o schema" | `data-modeler` |
| "implemente isso", "crie o componente", "escreva o código", "faça funcionar", "build this" | `implementation-engineer` |
| "que testes escrever?", "como testar isso?", "quais casos cobrir?", "test strategy" | `test-strategist` |
| "podemos fazer deploy?", "está pronto?", "o que verificar antes?", "launch blockers?", "release check" | `release-verifier` |
| "o que esses logs dizem?", "tem erro em produção?", "algo quebrou após o deploy?" | `production-reviewer` |

#### Linguagem sobre produto / negócio

| O usuário diz | Skill a usar |
|---|---|
| "o que construir?", "priorize isso", "vale a pena essa feature?", "roadmap", "o que é mais importante?" | `product-strategist` |
| "o que essa feature precisa fazer?", "quais os requisitos?", "transforme essa ideia em spec", "defina o escopo" | `requirements-analyst` |
| "como cobrar por isso?", "per seat ou usage?", "nosso modelo de preço tá certo?", "pricing model" | `pricing-strategist` |
| "o plano free dá coisa demais?", "as tiers fazem sentido?", "por que não fazem upgrade?", "feature gating" | `packaging-reviewer` |
| "por que a conversão tá baixa?", "por que não estão pagando?", "ARPU baixo", "monetization problem" | `monetization-analyst` |
| "o que os concorrentes fazem?", "como X compara com Y?", "diferenciação", "competitive analysis" | `competitive-reviewer` |
| "o que tá mudando no mercado?", "essa tendência é real?", "buyers querem o quê?", "market trends" | `market-analyst` |

#### Linguagem sobre UX / design / produto

| O usuário diz | Skill a usar |
|---|---|
| "o fluxo tá confuso", "tem passos demais", "o usuário não sabe o que fazer", "jornada quebrada" | `workflow-designer` |
| "a interface tá feia", "o layout não tá claro", "melhore o visual", "hierarquia visual", "design critique" | `interface-designer` |
| "o que escrever aqui?", "mensagem de erro certa?", "botão com qual texto?", "copy da interface" | `ux-writer` |
| "funciona para deficientes?", "screen reader?", "contraste ok?", "WCAG", "acessibilidade" | `accessibility-auditor` |
| "como um iniciante veria isso?", "faz sentido pro nosso usuário?", "perspectiva do cliente" | `persona-analyst` |
| "o que os dados dizem?", "onde os usuários saem?", "funnel analysis", "métrica baixa", "drop-off" | `analytics-reviewer` |

#### Linguagem sobre entrega / operação

| O usuário diz | Skill a usar |
|---|---|
| "como organizar o projeto?", "em que ordem fazemos?", "fases do projeto", "plano de execução" | `execution-planner` |
| "estamos travados", "time fora de sincronia", "handoff falhou", "blocker de entrega" | `delivery-coordinator` |
| "todo mundo está pronto para o lançamento?", "quem faz o quê no go-live?", "plano de launch" | `launch-coordinator` |
| "o processo tem controles?", "quem aprova o quê?", "e se falhar?", "auditoria de processo" | `process-auditor` |

#### Meta-linguagem (use todas as skills)

| O usuário diz | Skill a usar |
|---|---|
| "use suas skills", "use o máximo de skills", "faça com capacidades completas", "use your skills", "apply all skills", "faça novamente com as skills" | Identificar o contexto e aplicar todas as skills relevantes. Se não houver contexto claro → `audit-orchestrator` |
| "revise tudo", "audit geral", "me dê o quadro completo", "full review", "análise completa" | `audit-orchestrator` |
| "como perguntar isso melhor?", "ajude a estruturar meu pedido", "reformule isso" | `prompt-engineer` |

---

## Passo 2 — Ler as skills identificadas

**Não pule esta etapa.** Para cada skill identificada no Passo 1, abra e leia o SKILL.md completo antes de responder. As skills têm output format, reasoning lens e boundary rules que definem como responder corretamente.

---

## Passo 3 — Confirmar as skills usadas e responder

Sempre inicie a resposta dizendo quais skills foram aplicadas:

> "🔧 Skills aplicadas: `code-auditor`, `code-architect`"

Isso garante transparência para o usuário e confirma que o sistema funcionou.

---

## Quando o contexto não está claro

Se não der para identificar a tarefa real pelo histórico, pergunte de forma simples e não-técnica:

> "Para usar as skills certas, me conta: o que você quer melhorar ou resolver? Por exemplo — o código tá com problema? A interface tá confusa? O produto precisa de direção? Quer entender os dados?"

Aguarde a resposta antes de prosseguir.

---

## Regras críticas

- **Nunca** diga que as skills não estão disponíveis sem antes verificar com `ls /mnt/skills/user/`
- **Nunca** responda sem ter lido o corpo das skills relevantes — isso anula o propósito
- **Sempre** declare quais skills foram aplicadas no início da resposta
- Se `/mnt/skills/user/` não estiver acessível, reporte explicitamente: "O diretório de skills não está montado nesta sessão — apenas as skills públicas estão disponíveis. Isso é um problema de ambiente, não das skills em si."
- **Nunca** exija que o usuário use jargão técnico — seu trabalho é traduzir a linguagem natural dele para a skill certa

---

## Perfil do usuário típico deste skill

O usuário provavelmente:
- Pensa em ideias, resultados e problemas — não em nomes técnicos de áreas
- Diz "isso tá feio" e quer `interface-designer`, não sabe o nome da skill
- Diz "não tá funcionando" e pode precisar de `performance-reviewer`, `code-auditor`, ou `production-reviewer`
- Diz "use suas skills" como atalho para "trabalhe com todo o seu potencial"
- Pode escrever em português, inglês, ou misturar os dois

Sua função é ser o tradutor entre o que o usuário quer dizer e quem no sistema sabe resolver.

