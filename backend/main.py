import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # 导入模型
from database import engine  # 如果 database.py 有 engine，用它

# DB 支持 env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./novel_factory.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)  # 创建表

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def home():
    return {"msg": "后端活了！DB 就绪。"}

@app.post("/api/books")
async def create_book(title: str = Query(..., description="小说标题")):
    return {"book_id": 1, "title": title, "status": "创建成功"}

@app.post("/api/ai/test")  # AI 测试路由
async def test_ai(prompt: str = Query(...)):
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        return {"error": "缺少 API Key"}
    import httpx
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]})
    return {"result": resp.json()["choices"][0]["message"]["content"]}
