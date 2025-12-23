# Roadmap

## MVP 1 — RAG baseline
- Load documents (txt/pdf later)
- Chunk + embed
- Store in vector index
- Retrieve top-k passages
- Generate grounded response

## MVP 2 — Tool-using agent
- Define tool interface
- Add at least 2 tools (e.g., calculator + doc search)
- Add prompt + system policy

## MVP 3 — LangGraph workflow
- Multi-step state machine
- Error handling + retries
- Fallback response when retrieval fails

## MVP 4 — Demo
- Gradio UI or FastAPI endpoint
- Logging + basic monitoring
