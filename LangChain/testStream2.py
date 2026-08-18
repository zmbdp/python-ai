import os
import asyncio
from langchain_openai import ChatOpenAI

api_key = os.environ["DEEPSEEK_API_KEY"]
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key
)

# 异步流式输出
async def async_stream():
    print("===异步调用===")
    async for chunk in model.astream("写一段关于春天的作文，100字"):
        print(chunk.content, end="", flush=True)

asyncio.run(async_stream())