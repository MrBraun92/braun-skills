# Pack Gabarito (ADAPTA.org) — 4 Skills

Camada comportamental permanente que implementa 100% do PDF Gabarito: disciplina de estilo mais as dez diretrizes, distribuídas para maximizar acionamento automático sem diluir triggers.

## Estrutura

| Skill | Papel | Diretrizes |
|---|---|---|
| `gabarito-core` | Sempre ativa: estilo, sinal "Gabarito em uso.", roteamento, regras para agentes paralelos | Disciplina de estilo |
| `gabarito-clareza-input` | Pedidos ambíguos, vagos ou de baixo esforço | 04, 05, 10 |
| `gabarito-postura-socio` | Decisões, críticas, discordância, tarefas recorrentes | 01, 02, 03, 07 |
| `gabarito-verificacao` | Portão final: deliverables e fatos | 06, 08, 09 |

## Instalação

### Manus (Claude.ai / app)

Abra cada pasta da skill e clique em "Add to My Skills" (Adicionar às Minhas Skills), ou envie os quatro em **Configurações > Capacidades > Skills**. Instale os quatro; o core referencia os outros três pelo nome.

### Claude Code

Copie as quatro pastas para `~/.claude/skills/` (pessoal) ou `.claude/skills/` do repositório.

### Agentes Paralelos sem Acesso a Skills

Cole o snippet de `gabarito-core/references/claude-md-snippet.md` no `CLAUDE.md` ou `AGENTS.md` do projeto.

## Uso

O pack Gabarito é ativado automaticamente quando as skills estão instaladas. O `gabarito-core` carrega na primeira resposta de qualquer conversa e governa:

1. **Disciplina de estilo**: sem preâmbulo, sem palavras-tell, formato adequado, recomendação clara em decisões, ritmo humano, zero travessão.
2. **Roteamento automático**: carrega `gabarito-clareza-input` para pedidos ambíguos, `gabarito-postura-socio` para decisões e críticas, `gabarito-verificacao` para deliverables e fatos.
3. **Regras para agentes**: aplica-se integralmente em subagentes e agentes paralelos, com adaptações para output intermediário.

## Referências

- [ADAPTA.org — PDF Gabarito](https://adapta.org)
- Dez diretrizes operacionais para qualidade de resposta
- Integração com `skill-router` para domínio especializado

## Versionamento

Este pack foi importado para versionamento em `00-gabarito/` em Jul 20, 2026.
