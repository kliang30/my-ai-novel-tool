from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI网文工厂中枢", version="1.0.0")

# 允许前端跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI网文工厂后端已启动！准备割韭菜！"}

@app.post("/api/books")
async def create_book(title: str = Query(...)):  # 用 Query 解析 GET/POST params
    return {"book_id": 1, "title": title}

# 测试 API：加个 GET 版本，方便浏览器直接测
@app.get("/api/books")
async def list_books():
    return {"books": [{"id": 1, "title": "测试小说"}]}

# 去掉 --reload（生产环境不需要，防止冲突）
# 如果 railway.json 有 --reload，删掉它
