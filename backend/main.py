import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # 确保 models.py 已导入

# DB 支持 Railway PostgreSQL 或本地 SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./novel_factory.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)  # 自动创建表

app = FastAPI(title="AI网文工厂", debug=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"msg": "后端活了！路径修复成功。", "status": "ok"}

@app.post("/api/books")
async def create_book(title: str = Query(...)):
    # 简单模拟创建书（后期连 DB）
    return {"book_id": 1, "title": title, "status": "创建成功"}

@app.post("/api/ai/parse-worldview")
async def parse_worldview(text: str = Query(...)):
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        return {"error": "缺少 DeepSeek API Key，请在 Railway Variables 添加"}
    import httpx
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": f"你现在是网文架构师。请从以下文本中提取结构化数据：书名、大纲（卷章）、角色（主角/女主/反派）、设定（世界观/力量体系）。严格返回 JSON 格式，不要加解释。\n\n文本：{text[:4000]}" }],  # 截断避免超限
                "temperature": 0.3
            })
        if resp.status_code == 200:
            return {"result": resp.json()["choices"][0]["message"]["content"], "parsed": True}
        else:
            return {"error": "AI 调用失败", "status_code": resp.status_code}
