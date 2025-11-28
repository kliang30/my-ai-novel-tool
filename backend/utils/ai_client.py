import httpx
import os

async def call_deepseek(messages: list):
    key = os.getenv("DEEPSEEK_API_KEY")
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.deepseek.com/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={"model": "deepseek-chat", "messages": messages, "temperature": 0.7})
        return resp.json()["choices"][0]["message"]["content"]
