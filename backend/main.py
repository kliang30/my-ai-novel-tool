from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "后端已彻底活！可以开始造小说了！"}

@app.post("/api/books")
async def create_book(title: str = Query(None)):
    if not title:
        title = "默认书名"
    return {"book_id": 999, "title": title, "status": "创建成功"}
