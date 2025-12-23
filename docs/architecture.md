# Architecture (High-level)

User → Agent Router → (RAG Retriever / Tools) → LLM → Response

Key components:
- Retrieval pipeline for grounded answers (RAG)
- Agent planning + tool execution (ReAct/ReWOO)
- LangGraph for controlled multi-step flows
- Automation layer (n8n) for real workflows
