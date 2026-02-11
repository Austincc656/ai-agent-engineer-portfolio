from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

from src.agent import DataAnalystAgent, FallbackLLM
from src.context import build_ctx

app = FastAPI(title="Autonomous Data Analyst Agent API", version="0.1.0")


class ChatRequest(BaseModel):
    user_id: str = Field(default="demo_user")
    question: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    answer: str
    metadata: Dict[str, Any] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    ctx, con = build_ctx()
    try:
        llm = FallbackLLM()              # ✅ required by DataAnalystAgent
        agent = DataAnalystAgent(llm=llm)

        answer = agent.answer(ctx, req.question)

        return {
            "answer": answer,
            "metadata": {"user_id": req.user_id, "session_id": req.session_id},
        }
    finally:
        con.close()
