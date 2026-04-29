---
name: rag-architect
description: Designs end-to-end RAG architecture for the EventPro AI Chat (currently OpenAI-based, in server/routers/ai.ts) — chunking strategy, embedding model selection (cost vs quality), retrieval choice (BM25 vs vector vs hybrid), reranking, evaluation harness, and cost modeling. Concrete use case: an event-aware AI that knows the producer's contracts, spreadsheets, emails, and EventPro budget items. Use when the user says "design the AI chat", "RAG", "retrieval", "embeddings", "chunk strategy", "the AI is hallucinating", or wants to upgrade beyond a thin wrapper around GPT.
---

# RAG Architect (EventPro AI Chat)

Designs the retrieval-augmented generation pipeline for the EventPro AI Chat — the floating chat in `EventAIChat.tsx` that today calls OpenAI through `server/routers/ai.ts`. The realistic use case: a producer asks "qual é o pagamento mais alto em aberto do festival?" and the AI must answer from the actual database state, not invent. Real EventPro AI must know **contracts (S3 PDFs), email threads (forwarded by user), spreadsheets (importação), AND the live database (budget items, payments, sponsors, tickets)**. This skill produces an architecture that survives the "AI is making things up" complaint.

## When to use this skill
- User wants the AI Chat to actually answer from the event's data, not generic gpt-output.
- Hallucination complaints: "The AI said we paid R$ 50k for stage rental but we paid R$ 35k."
- Upgrading from a single system-prompt + raw-data-injection to retrieval.
- User has accumulated PDFs (contracts) in S3 and wants the AI to read them.
- Cost: OpenAI token bill is climbing because every request stuffs the entire event into context.

## Methodology

### Step 1: Scope the corpus
List every information source the AI should know:
- **Live database** — events, budgetItems, payments, sponsors, tickets, artists, staff, comments (Drizzle/MySQL on TiDB).
- **Files in S3** — contracts, riders, briefings (uploaded via `BudgetItemFiles.tsx`).
- **Email threads** — currently NOT ingested; would require a forwarding inbox or IMAP integration.
- **Spreadsheets** — imported via `ImportWizard.tsx` and live as budget items afterward.
- **Decisions log** — `decisions.ts` router already stores structured decisions.
- **Activity log** — `activityLog.ts` router stores who-did-what-when.
- **Comments** — per item / per event from `comments.ts`.

For each source: what's the volume, refresh rate, and is it text or structured?

### Step 2: Pick the retrieval pattern per source
Different sources need different retrieval:

- **Live database** → SQL retrieval, NOT vector retrieval. The AI generates a tRPC call (or a constrained SQL query) and gets the answer from the source of truth. This is the most important insight — vectorizing your database is a common antipattern. EventPro already has the data; just teach the AI to query it.
- **PDFs (contracts)** → chunking + vector retrieval. Contracts are unstructured prose; semantic search works.
- **Spreadsheets imported** → already in the database after import; query like the database.
- **Email threads (when introduced)** → chunking + vector retrieval, with metadata (from, to, date, subject).
- **Decisions / Activity logs** → structured; SQL retrieval with a small filter on event_id and date range.
- **Comments** → small enough to fetch all by event_id; no embedding needed at this scale.

The architecture is therefore **hybrid: tool-using agent + vector RAG**, not pure RAG.

### Step 3: Design the tool layer (for structured data)
Define the tools the AI can call:

```
- get_event_summary(eventId): canonical KPIs from shared/financial.ts
- list_open_payments(eventId, dateRange?): from budget.ts
- get_top_n_items(eventId, by, n): top items by value
- get_payment_status_history(itemId): activity log filter
- list_sponsors(eventId, status?): from sponsors.ts (post-Sprint 6 #2 enum)
- get_group_rollup(groupId): from eventGroups.ts (Sprint 6 contribution)
- search_decisions(eventId, query): structured filter
- search_comments(eventId, query): full-text search inside comments
```

Use OpenAI function calling / tools API. Each tool has a strict schema. Pair with backend authorization — the AI runs as the user; tools must call the same `requireEventAccess` guard the rest of the system uses.

### Step 4: Design chunking for unstructured (PDFs, future emails)
- **Chunk size**: 500-1000 tokens. PDFs of contracts often have section headers; respect them. Use semantic chunking (split on double newline + section boundary) when possible, fixed-size chunking only as fallback.
- **Overlap**: 10-15% (50-150 tokens). Reduces miss-by-boundary errors.
- **Metadata per chunk**: source_id, source_type (contract / email / brief), event_id, vendor (if known), date.
- **Multi-vector**: chunk text + a separate "title/summary" vector for the document. Improves coarse retrieval before fine.

### Step 5: Pick the embedding model
Trade-offs in 2026:
- **OpenAI text-embedding-3-small** (1536 dim) — cheap (~$0.02/1M tokens), fine for English/PT mixed.
- **OpenAI text-embedding-3-large** (3072 dim) — better for nuanced retrieval, ~6x more expensive.
- **Cohere multilingual-v3** — strong PT-BR performance specifically; worth considering since EventPro is BR.
- **Voyage AI voyage-3** — very high quality, multilingual, cost similar to OpenAI 3-small.
- **Self-hosted (BGE, e5)** — only if cost or data residency demands it. Operational overhead significant.

Default recommendation for EventPro: **OpenAI text-embedding-3-small** for v1 (already on OpenAI, cheap, good enough for contracts in PT-BR). Upgrade to Voyage or Cohere multilingual if PT-BR retrieval quality is the bottleneck.

### Step 6: Pick the retrieval method
- **BM25** (keyword) — strong baseline, especially for exact terms (vendor names, item names, dates). Cheap.
- **Dense vector** — strong for semantic queries ("who handles audio?" matches "som" related items even without keyword overlap).
- **Hybrid (BM25 + vector + RRF)** — best for mixed queries. Reciprocal Rank Fusion is the simplest combiner.
- **Reranker** — a cross-encoder (Cohere Rerank, Voyage Rerank) re-orders the top N retrievals using full query+passage scoring. Big quality jump for top-3 precision; worth it for the AI Chat.

Recommended: hybrid retrieval (BM25 + vector RRF) → top 20 candidates → rerank → top 4 to context. TiDB has full-text search support that can serve as BM25 directly; Postgres pgvector is another option but EventPro is on TiDB so use what's there or add an external vector DB (Qdrant, Pinecone) only if TiDB vector support proves insufficient.

### Step 7: Design the prompt and the contract
System prompt structure:

```
ROLE: EventPro Assistant for {event_name}
TOOLS available: <list with schemas>
RULES:
- Always use tools to retrieve data; do not answer financial questions from memory.
- If a tool returns no data, say so — do not invent.
- For numeric answers, cite the source row(s).
- Respond in pt-BR.
- If the user asks something outside the event scope, politely redirect.
USER QUERY: ...
```

Provide a tightly scoped contract. Hallucination drops massively when the model is allowed to say "I don't know" and is required to cite.

### Step 8: Build the eval harness
The single most-skipped, most-important step. Without eval, every change to the RAG is vibes.

- **Golden set**: 30-100 question-answer pairs sampled from real producer questions. Mix: factual ("how much did we pay vendor X?"), aggregate ("total open payments?"), reasoning ("which artists need lodging?"), out-of-scope ("what's the weather Friday?").
- **Metrics**: retrieval recall@k (was the right document in top-k?), answer correctness (LLM-as-judge or human), citation faithfulness (did the cited row actually support the answer?), latency, cost per query.
- **Run on every change** to chunking, embedding, retrieval, or prompts.

### Step 9: Cost model
Per-query estimate:
- Embedding query: ~$0.00001 (negligible).
- Retrieval: BM25 + vector lookup are sub-cent.
- Reranker: ~$0.001 for top 20.
- LLM context: ~3-5k tokens of context + response → ~$0.02-0.10 depending on model (GPT-4o, Claude 3.5 Sonnet).
- Tool-calling round-trips: 2-4x the base cost.

For a producer using the chat 50 times/day: ~$1-5/day. Plan tier on EventPro can absorb this; very heavy users may need rate limits.

### Step 10: Output the architecture
Diagrams + spec + migration plan from current state.

## Output format

```
## RAG Architecture — EventPro AI Chat

### 1. Corpus inventory
| Source | Type | Volume | Refresh | Retrieval method |
|---|---|---|---|---|

### 2. Tool layer (structured data)
- Tool name → backend endpoint → schema → guard

### 3. Chunking spec (unstructured)
- Chunk size, overlap, metadata fields

### 4. Embedding model
Selected: <model>
Rationale: <one paragraph>

### 5. Retrieval pipeline
Stage 1: <BM25 / vector / hybrid>
Stage 2: <rerank model>
Stage 3: top-K to LLM context

### 6. Prompt contract
<system prompt template>

### 7. Eval harness
- Golden set size, sample queries
- Metrics tracked
- Where stored / how run

### 8. Cost model
- Per-query: ~$X
- Per-event/day at typical use: ~$Y

### 9. Migration from current state
Step 1: ...
Step 2: ...
Step 3: ...

### 10. Open risks
- PT-BR retrieval quality: <approach>
- Hallucination on aggregates: <approach>
- Stale data when DB changes mid-conversation: <approach>
```

## Quality checklist
- [ ] Database is queried via tools, not embedded as a vector blob.
- [ ] Authorization guards (`requireEventAccess`) apply to AI tool calls — same as user-driven calls.
- [ ] Embedding model choice is justified for PT-BR content.
- [ ] Hybrid retrieval (BM25 + vector) is at minimum considered, not blindly default-vector.
- [ ] Reranker stage is included for top-K precision.
- [ ] Eval harness has a golden set and at least 3 metrics.
- [ ] Cost model is concrete (not "should be cheap").
- [ ] Migration plan is incremental, not a big bang.
- [ ] System prompt explicitly instructs the model to refuse / say "don't know" rather than invent.

## Notes for the assistant
- The biggest mistake is treating a structured database like a documents corpus. EventPro has clean Drizzle queries; teach the AI to use them via tools, don't embed `budgetItems` rows.
- "Throw it all in the prompt" works at small scale and breaks at production scale. The AI Chat in `EventAIChat.tsx` may currently inject the full event — that's fine for v0, broken for v2.
- LLM-as-judge for eval is acceptable but biased. Validate periodically with human review on a subset.
- Vector databases: pgvector / Qdrant / Pinecone / TiDB vector. TiDB has vector support — using what's already in the stack is operationally cheaper than adding another DB. Evaluate before committing to an external vector DB.
- Chunking PDFs of contracts: layout matters. Use a PDF parser that preserves headers/tables (e.g., `unstructured.io`, `pymupdf4llm`) before naive text extraction.
- Reranker quality: Cohere Rerank 3 / Voyage Rerank 2 are both strong for multilingual; pick by latency and cost.
- The user is a non-programmer running a startup. Architectural choices should be explained with their cost and operational implications, not just chosen.
- Pair with `database-optimizer` if tool-call queries become slow, with `error-detective` for hallucination root-cause, with `verification-before-completion` before declaring an architecture change ready.
- Compliance: contract PDFs in S3 may contain personal data (vendor representatives, signatures). Embedding them sends content to OpenAI / chosen embedding provider. Disclose in privacy policy and consider whether contract PDFs should be embedded at all vs. just summarized.
