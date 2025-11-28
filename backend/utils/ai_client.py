import httpx
import os

async def call_deepseek(messages: list, max_tokens=2000):
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise ValueError("DEEPSEEK_API_KEY not set")
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={"model": "deepseek-chat", "messages": messages, "temperature": 0.7, "max_tokens": max_tokens})
        if resp.status_code == 200:
            return resp.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"AI error: {resp.status_code}")
