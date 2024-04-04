from fastapi import FastAPI, HTTPException
from .services.chat_service import ask_question
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ask/")
async def ask(txtFile: str, question: str):
    # 构造文件的完整路径
    file_path = os.path.join('data', txtFile)
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            document = file.read()

        # 调用服务逻辑
        answer = ask_question(document, question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
