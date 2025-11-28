import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # 假设 models 已导入

# DB URL 支持环境变量
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./novel_factory.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)  # 创建表

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], ...)

@app.get("/")
async def home():
    return {"msg": "后端活了！DB 初始化完成。"}

# ... 其他路由
@app.post("/api/ai/test")
async def test_ai(prompt: str = Query(...)):
    # 简单 DeepSeek 调用（加 httpx）
    import httpx
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        return {"error": "No API key"}
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/v1/chat/completions", json={
            "model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]
        }, headers={"Authorization": f"Bearer {key}"})
    return {"result": resp.json()}
