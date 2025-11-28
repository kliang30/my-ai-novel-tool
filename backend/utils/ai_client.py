import httpx
import os

async def call_deepseek(prompt: str):
    key = os.getenv("DEEPSEEK_API_KEY")
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/v1/chat/completions", 
            headers={"Authorization": f"Bearer {key}"},
            json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]})
    return resp.json()["choices"][0]["message"]["content"]
