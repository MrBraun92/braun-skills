---
name: skill-router
description: 'Read this skill IMMEDIATELY in two situations: (1) whenever the user asks Claude to use its installed skills in any language — "use suas skills", "use your skills", "usando suas skills instaladas", "use o máximo de skills", "trabalhe com suas capacidades completas", "faça novamente usando as skills", "apply all your skills", "use todas as skills disponíveis"; (2) whenever the user describes a problem or situation in natural/non-technical language and it''s unclear which specialist skill should handle it. This skill translates what the user actually means — regardless of technical vocabulary — into the correct specialist skill(s). Essential for non-technical users who describe problems in plain language rather than dev/product jargon.'
---

# Skill Router — Roteador Genérico e Dinâmico

## Propósito

Este skill faz duas coisas:

1. **Captura meta-pedidos** — quando o usuário pede para "usar as skills" sem especificar qual
2. **Traduz linguagem natural → skill técnica** — quando o usuário descreve um problema com suas próprias palavras e Claude precisa identificar qual especialista aplicar

O router é **dinâmico**: em vez de depender de uma tabela estática, ele lê as skills disponíveis no momento da execução e usa raciocínio para encontrar as melhores. Isso significa que **funciona automaticamente com qualquer skill nova** — instaladas pelo usuário, por plugins da Anthropic, ou por terceiros — sem precisar ser atualizado.

---

## Passo 1 — Descobrir as skills disponíveis (SEMPRE faça isso primeiro)

Antes de qualquer matching, descubra o que está disponível agora.

### 1a. Ler os diretórios de skills

Execute mentalmente (ou via bash, se disponível):

```
ls /sessions/*/mnt/.claude/skills/
ls /sessions/*/mnt/.remote-plugins/*/skills/
```

Se não tiver acesso ao filesystem, consulte a lista de skills disponíveis no sistema prompt (seção `<available_skills>`). Essas são as skills reais acessíveis nesta sessão.

### 1b. Para cada skill candidata, leia seu SKILL.md

Leia especialmente o campo `description` do frontmatter — ele descreve exatamente quando a skill deve ser acionada e quando não deve.

**Não pule esta etapa.** As skills têm boundary rules e output formats que definem como responder corretamente.

---

## Passo 2 — Entender o que o usuário realmente quer

Leia o histórico da conversa e a mensagem atual. Pergunte-se:

> **Qual é o problema real sendo descrito? Qual seria o resultado ideal para o usuário?**

### Princípios de tradução

O usuário raramente usa jargão técnico. Sua função é mapear a intenção real para as skills certas.

**Perguntas-chave para identificar a intenção:**

- É sobre **código**? (qualidade, arquitetura, performance, segurança, implementação, testes, deploy)
- É sobre **produto / negócio**? (o que construir, precificar, priorizar, posicionar, competir)
- É sobre **UX / design**? (fluxo, interface, copy, acessibilidade, pesquisa com usuários)
- É sobre **dados / analytics**? (métricas, funil, comportamento, SQL, dashboards)
- É sobre **operações / entrega**? (planejamento, bloqueios, lançamento, processos, cloud, SRE)
- É sobre **clientes / go-to-market**? (feedback, retenção, sucesso, suporte, receita, vendas)
- É sobre **finanças / legal / RH**? (relatórios, contratos, conformidade, pessoas)
- É sobre **conteúdo / marketing**? (textos, campanhas, SEO, posicionamento de marca)
- É um **meta-pedido**? ("use suas skills", "aplique tudo", "revise tudo")

### Como fazer o match

Para cada skill disponível (descoberta no Passo 1), compare a intenção do usuário com:

1. O `description` do SKILL.md — especialmente as frases de trigger e as frases de exclusão ("Not for...")
2. O nome da skill — muitas vezes autoexplicativo
3. O conteúdo do SKILL.md — as seções "Use this skill when" e "Do not use this skill when"

Escolha a(s) skill(s) cujo propósito é mais próximo do que o usuário precisa fazer agora.

**Prefira especificidade.** Se existe uma skill dedicada (ex: `retention-lifecycle-strategist`), prefira-a sobre uma skill genérica (ex: `analytics-reviewer`), mesmo que ambas pareçam relevantes.

**Combine skills quando necessário.** Se o pedido tem múltiplas dimensões, aplique múltiplas skills em sequência ou paralelo.

---

## Passo 3 — Executar as skills identificadas

Para cada skill escolhida:

1. Leia o SKILL.md completo (não apenas o description)
2. Siga o output format, reasoning lens e boundary rules definidos nela
3. Aplique o trabalho completo como se aquela skill tivesse sido invocada diretamente

**Sempre inicie a resposta declarando quais skills foram aplicadas:**

> "🔧 Skills aplicadas: `positioning-strategist`, `customer-signal-synthesizer`"

Isso garante transparência e confirma que o sistema funcionou.

---

## Passo 4 — Routing de follow-up

Muitas skills têm "boundary rules" que identificam quando o trabalho deve continuar em outra skill. Respeite essas regras:

- Se a skill atual diz "route to X for Y" → informe o usuário e pergunte se deve continuar com X
- Se o trabalho produzido naturalmente alimenta outra skill → sugira o próximo passo

---

## Comportamento para meta-pedidos

Quando o usuário diz "use suas skills", "aplique tudo", "use o máximo de skills", "trabalhe com capacidades completas":

1. Leia o contexto da conversa para entender o tema
2. Descubra todas as skills disponíveis (Passo 1)
3. Identifique TODAS as skills relevantes para o contexto — não apenas uma
4. Se o contexto é muito amplo ou ambíguo → use `audit-orchestrator` como orquestrador
5. Se o contexto é claro → aplique as skills relevantes diretamente

---

## Quando o contexto não está claro

Se não der para identificar a tarefa real pelo histórico, pergunte de forma simples:

> "Para usar as skills certas, me conta: o que você quer melhorar ou resolver? Por exemplo — o código tá com problema? A interface tá confusa? O produto precisa de direção? Quer entender os dados? Há um cliente com problema específico?"

Aguarde a resposta antes de prosseguir.

---

## Regras críticas

- **Nunca** mantenha uma lista estática de skills neste arquivo — a lista muda conforme novas skills são instaladas
- **Nunca** diga que uma skill não existe sem antes verificar o filesystem ou o `<available_skills>` do sistema
- **Nunca** responda sem ter lido o corpo das skills relevantes — isso anula o propósito do router
- **Sempre** declare quais skills foram aplicadas no início da resposta
- **Nunca** exija que o usuário use jargão técnico — traduza a linguagem natural para a skill certa
- **Sempre** trate skills da Anthropic, skills de plugins, e skills instaladas pelo usuário como equivalentes — o critério é relevância, não origem
- Se `/mnt/.claude/skills/` não estiver acessível, use a lista em `<available_skills>` do sistema prompt e reporte o estado do ambiente

---

## Perfil do usuário típico

O usuário provavelmente:
- Pensa em ideias, resultados e problemas — não em nomes técnicos de áreas
- Diz "isso tá feio" e quer `interface-designer`, não sabe o nome da skill
- Diz "não tá funcionando" e pode precisar de `performance-reviewer`, `code-auditor`, ou `production-reviewer`
- Diz "use suas skills" como atalho para "trabalhe com todo o seu potencial"
- Pode escrever em português, inglês, ou misturar os dois
- Pode ter instalado skills personalizadas que este arquivo nunca menciona — e elas devem funcionar igualmente bem

Sua função é ser o **tradutor universal** entre o que o usuário quer dizer e quem no sistema sabe resolver — independente de quais skills estão instaladas agora ou no futuro.
