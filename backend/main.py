import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 安全获取 DATABASE_URL，fallback 到 SQLite
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL or "railway" in DATABASE_URL and len(DATABASE_URL) < 50:  # 检测无效引用
    DATABASE_URL = "sqlite:///./novel_factory.db"  # 本地 fallback
    print("Warning: Using fallback SQLite (add valid DATABASE_URL in Railway)")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

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
    return {"msg": "后端活了！路径修复成功。", "status": "ok", "db_url": DATABASE_URL[:50] + "..." if DATABASE_URL else "fallback"}

@app.post("/api/books")
async def create_book(title: str = Query(...)):
    return {"book_id": 1, "title": title, "status": "创建成功"}

@app.post("/api/ai/parse-worldview")
async def parse_worldview(text: str = Query(...)):
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        return {"error": "缺少 DeepSeek API Key"}
    import httpx
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": f"从文本提取 JSON {{book_title, volumes, characters, settings}}。文本：{text[:4000]}" }],
                "temperature": 0.3
            })
        if resp.status_code == 200:
            return {"result": resp.json()["choices"][0]["message"]["content"]}
        return {"error": resp.status_code}
