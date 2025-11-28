from fastapi import FastAPI
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
async def create_book(title: str):  # 注意：加了类型注解
    return {"book_id": 1, "title": title}

# 临时注释掉 routers 导入，后面再加
# from routers import books, chapters, settings, ai
# app.include_router(books.router, prefix="/api/books")
# ... 其他 routers
