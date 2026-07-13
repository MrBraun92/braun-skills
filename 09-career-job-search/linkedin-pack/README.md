# LinkedIn Skills Pack

Pack integrado de Agent Skills para posicionamento profissional, otimização de perfil, SSI, conteúdo, networking e operações assistidas por MCP no LinkedIn.

## Skills

1. `linkedin-strategist-orchestrator` — define foco, coordena diagnóstico e direciona o agente para o workflow correto.
2. `linkedin-profile-optimizer` — otimiza posicionamento, foto, capa, headline, Sobre, experiências, competências, SEO, discoverability e configurações do perfil.
3. `linkedin-ssi-network-strategist` — diagnostica os quatro pilares do SSI e transforma pontuação em plano de marca, rede, interação e relacionamento.
4. `linkedin-content-strategist` — planeja, escreve, humaniza, audita, reaproveita e mede conteúdo profissional.
5. `linkedin-mcp-operator` — usa ferramentas MCP para pesquisar pessoas, empresas, vagas, posts, conversas e oportunidades, com confirmação humana para ações externas.

## Princípios do pack

- Clareza sobre cargo-alvo, área e senioridade.
- Palavras-chave baseadas em vagas e linguagem real de mercado.
- Resultados e impacto acima de listas de tarefas.
- Conteúdo fiel à voz e à experiência do usuário.
- SSI tratado como indicador de comportamento, não como objetivo final isolado.
- Nenhuma experiência, métrica ou competência pode ser inventada.
- Ações externas e automações devem respeitar limites da plataforma e exigir aprovação humana quando houver envio, publicação ou conexão.
- Heurísticas de algoritmo devem ser identificadas como hipóteses ou rubricas internas, nunca como pesos oficiais não divulgados.

## Fluxo recomendado

```text
linkedin-strategist-orchestrator
├── linkedin-profile-optimizer
├── linkedin-ssi-network-strategist
├── linkedin-content-strategist
└── linkedin-mcp-operator
```

O orquestrador pode chamar mais de uma skill quando o pedido envolver perfil, conteúdo, networking e busca de oportunidades ao mesmo tempo.
