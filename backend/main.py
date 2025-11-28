```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 这行必须有！名字必须叫 app
app = FastAPI(title="AI网文工厂", description="后端已活")

# 允许所有前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"msg": "后端已经彻底活了！可以开始写小说了！"}

@app.get("/test")
async def test():
    return {"status": "ok"}
