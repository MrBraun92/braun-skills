---
name: doc-to-markdown
description: Converte arquivos PDF, DOCX, PPTX e HTML em Markdown limpo e estruturado, preservando headings, listas, tabelas, blocos de citação e metadados. Aciona quando o usuário precisa transformar um documento (paper acadêmico, contrato, slide, página web) em texto pronto para Notion, Obsidian, Claude ou GitHub.
---

# Doc to Markdown

Esta skill recebe um documento em formato fechado (PDF, DOCX, PPTX, HTML) e devolve Markdown limpo, hierárquico e fiel ao conteúdo original. O foco é preservar estrutura semântica (headings, listas, tabelas, citações em bloco, links, ênfase) sem inventar conteúdo nem perder dados. Serve o Oliver para alimentar a base de conhecimento da tese de mestrado, organizar PDFs de papers da UiS, transformar slides de aula em notas e padronizar conteúdo entre Claude / Manus / GPT.

## Quando usar esta skill
- O usuário envia um PDF acadêmico (paper, capítulo de livro, tese) e quer extrair o texto em Markdown.
- O usuário precisa migrar conteúdo de DOCX (Word) ou PPTX (PowerPoint) para Notion ou Obsidian.
- O usuário cola HTML bruto ou pede para "limpar" um artigo de blog em Markdown.
- O usuário quer normalizar exports do Google Docs ou Office 365 antes de subir para um repo.

## Metodologia

### Etapa 1: Identificar formato e propósito
Pergunte (ou deduza pelo arquivo) qual é o formato de origem e o destino do Markdown (Notion, Obsidian, GitHub, Claude). O formato de destino afeta sintaxe (Obsidian aceita `[[wikilinks]]`, Notion não; GitHub renderiza tabelas pipe, Notion prefere blocos nativos). Identifique se o documento é acadêmico (paper, tese), executivo (relatório, contrato) ou narrativo (artigo, slide).

### Etapa 2: Extrair texto preservando estrutura
- **PDF**: priorize PDFs com camada de texto. Se for scan (imagem), avise o usuário que precisa de OCR antes. Detecte hierarquia por tamanho de fonte, negrito e espaçamento.
- **DOCX**: leia estilos de parágrafo (Heading 1, Heading 2, etc.) — eles são a fonte de verdade da hierarquia.
- **PPTX**: cada slide vira uma seção `## Slide N — título`. Notas do palestrante viram blockquote.
- **HTML**: mantenha apenas tags semânticas (`h1`–`h6`, `ul/ol`, `table`, `blockquote`, `code`). Descarte `div`, `span`, classes CSS, scripts.

### Etapa 3: Mapear elementos para Markdown
- Headings: `#` (h1) a `######` (h6) — apenas um `#` por documento.
- Listas: `-` para não ordenadas, `1.` para ordenadas. Indentação com 2 espaços.
- Tabelas: sintaxe pipe (`| col | col |`) com linha separadora.
- Citações em bloco: `>` com quebra de linha em branco entre parágrafos.
- Código inline: backticks. Bloco de código: três backticks com linguagem quando identificável.
- Notas de rodapé acadêmicas: `[^n]` no texto + `[^n]: conteúdo` no fim.
- Imagens: `![alt](caminho)` — se a imagem não foi exportada, deixe placeholder `![figura N — descrição]()`.

### Etapa 4: Tratar conteúdo acadêmico (caso da tese)
Quando for paper APA 7:
- Preserve referências bibliográficas em uma seção `## Referências` no fim, uma por linha.
- Citações no texto (Smith, 2024) ficam inline.
- DOI e URLs ficam como link Markdown.
- Tabelas e figuras numeradas (Tabela 1, Figura 3) viram H4 (`#### Tabela 1 — descrição`).
- Equações: LaTeX entre `$...$` (inline) ou `$$...$$` (bloco).

### Etapa 5: Limpar artefatos comuns
Remova ou normalize:
- Cabeçalhos / rodapés repetidos a cada página de PDF.
- Números de página soltos.
- Hífens de quebra de linha (`pala-vra` → `palavra`).
- Ligaduras tipográficas (`ﬁ` → `fi`, `ﬂ` → `fl`).
- Espaços duplos, tabs no início de linha que não são indentação.
- Aspas curvas viram retas se o destino for código; preserve se for prosa.

### Etapa 6: Validar e devolver
Antes de entregar, verifique:
- Hierarquia de headings é monotônica (não pula de H1 para H4).
- Tabelas estão alinhadas e renderizam.
- Links têm URL válida.
- Não sobraram fragmentos de markup do formato original (`<o:p>`, `\par`, etc.).

## Formato de saída

Um arquivo Markdown único, com:
1. Frontmatter YAML opcional com `title`, `author`, `source`, `date`, `tags` (apenas se o usuário pediu para Obsidian).
2. Corpo do documento com hierarquia semântica.
3. Seção final `## Referências` ou `## Notas` quando aplicável.
4. Comentário no fim entre `<!-- ... -->` listando elementos que **não** foram convertidos (imagens não exportadas, equações complexas, layout multicoluna perdido) — transparência total.

## Checklist de qualidade
- [ ] Headings seguem hierarquia semântica sem pular níveis.
- [ ] Tabelas renderizam corretamente em Markdown pipe.
- [ ] Citações em blockquote têm marcação correta com `>`.
- [ ] Referências APA preservadas integralmente (zero edição de conteúdo).
- [ ] Imagens marcadas com placeholder se não foram exportadas.
- [ ] Cabeçalhos e rodapés repetidos foram removidos.
- [ ] Comentário de transparência lista o que não foi convertido.

## Notas para o assistente
- **Nunca resuma o conteúdo.** Esta skill é conversão fiel, não síntese. Se o usuário quer resumo, recomende uma skill diferente.
- **Não invente metadados.** Se o autor ou data não estão no documento, deixe em branco no frontmatter.
- **Documentos em PT-BR e EN**: detecte o idioma e preserve. Não traduza.
- **PDFs escaneados (sem camada de texto)**: pare e avise — recomende rodar OCR antes.
- **Documentos longos (>50 páginas)**: divida em arquivos por capítulo se o usuário não especificou o contrário.
- **Confidencial**: se o documento parece confidencial (contrato, NDA, dado pessoal), avise antes de processar e sugira anonimização.
