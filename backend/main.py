from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# 简单 app 定义，防模块加载失败
app = FastAPI(title="AI网文工厂", debug=False)  # debug=False 去 reloader

# CORS 允许所有
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"msg": "后端彻底活了！可以开始写小说割韭菜了！", "status": "success"}

@app.post("/api/books")
async def create_book(title: str = Query(..., description="小说标题")):
    return {"book_id": 1, "title": title, "status": "创建成功"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
