# AI Agent Systems & RAG Pipelines

A portfolio repository for building **AI agents** and **Retrieval-Augmented Generation (RAG)** systems using modern agent frameworks and workflow automation.

## What’s inside
- **Agents:** ReAct + ReWOO style agents with tool use and structured reasoning flows
- **RAG:** ingestion → indexing → retrieval → grounded generation
- **LangGraph:** state-driven, multi-step agent workflows (branching, loops, error handling)
- **Automation:** n8n workflows to connect agents to external services and business processes
- **Evaluation mindset:** tracing/debugging concepts (e.g., LangSmith-style observability)

> This repo is actively developed. Projects are published incrementally as they reach demo-ready quality.

## Tech stack
Python • LangChain • RAG • LangGraph • n8n • (FastAPI/Gradio planned)

## Repo structure
- `src/agents` — agent implementations and tools
- `src/rag` — ingestion/indexing/retrieval modules
- `src/graphs` — LangGraph workflows
- `workflows/n8n` — automation workflows (exports added later)
- `docs` — architecture notes, decisions, roadmap
- `tests` — basic smoke tests and validation

## Roadmap
- [ ] RAG MVP: ingest docs → retrieve top-k → cite sources
- [ ] Agent MVP: tool-use agent (calculator/web/file) + safety guardrails
- [ ] LangGraph: multi-step workflow with retries & fallback responses
- [ ] Demo: local UI (Gradio) or API (FastAPI)
- [ ] Evaluation: prompts + test set + lightweight scoring

## How to run (placeholder)
Setup instructions will be added as the first MVP lands.
