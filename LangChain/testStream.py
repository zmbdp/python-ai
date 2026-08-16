import os

from langchain_openai import ChatOpenAI

api_key = os.environ["DEEPSEEK_API_KEY"]
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key
)

for chunk in model.stream("写一个关于春天的作文，不少于一百字"):
    print(chunk.content, end="", flush=True)
