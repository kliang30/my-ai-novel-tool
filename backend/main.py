from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import books, chapters, settings, ai  # 后期添加routers文件夹

app = FastAPI(title="AI网文工厂中枢", version="1.0.0")

# 允许前端跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 临时简化：后期添加完整router
@app.get("/")
async def root():
    return {"message": "AI网文工厂后端已启动！"}

# 示例API
@app.post("/api/books")
async def create_book(title: str):
    return {"book_id": 1, "title": title}
