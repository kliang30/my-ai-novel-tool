from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

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
    return {"book_id": 1, "title": title, "status": "创建OK"}
