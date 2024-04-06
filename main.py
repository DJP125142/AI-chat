from fastapi import FastAPI,HTTPException
from services.chat_service import ask_question
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ask/")
async def ask(question: str):
    try:
        # 调用服务逻辑
        answer = ask_question(question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))