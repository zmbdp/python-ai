from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import os

api_key = os.environ["DASHSCOPE_API_KEY"]
model = ChatOpenAI(
    model="qwen-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key,
)

tool = TavilySearch(
    max_retries=5  # 搜索最大结果数
)

model_with_tools = model.bind_tools([tool])

message = [
    HumanMessage("上海浦东新区现在的天气怎么样？")
]

ai_message = model_with_tools.invoke(message)
print(ai_message)
print("===============================================================")

message.append(ai_message)
model.invoke(message)

for tool_call in ai_message.tool_calls:
    selected_tool = {"tavily_search": tool}[tool_call["name"].lower()]
    tool_message = selected_tool.invoke(tool_call)
    message.append(tool_message)

print(message)
print("===============================================================")

print(model_with_tools.invoke(message).content)
