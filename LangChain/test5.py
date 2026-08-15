from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from typing_extensions import Annotated
import os


@tool
def add(
        a: Annotated[int, ..., "第一个整数"],
        b: Annotated[int, ..., "第二个整数"],
) -> int:
    """两数相加"""
    return a + b


@tool
def multiply(
        a: Annotated[int, ..., "第一个整数"],
        b: Annotated[int, ..., "第二个整数"],
) -> int:
    """两数相乘"""
    return a * b


# model = init_chat_model(model="deepseek-chat")

api_key = os.environ["DASHSCOPE_API_KEY"]
model = ChatOpenAI(
    model="qwen-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key,
)

# # 列出所有含 DASH 的环境变量
# print("=== 含 DASH 的环境变量 ===")
# for k, v in os.environ.items():
#     if 'DASH' in k.upper():
#         print(f"  {k}: {v}")

# print("===============================================================")
# api_key = os.environ["DEEPSEEK_API_KEY"]
# model = ChatOpenAI(
#     model="deepseek-chat",
#     base_url="https://api.deepseek.com",
#     api_key=api_key
# )

# 绑定工具
tools = [add, multiply]
model_with_tools = model.bind_tools(tools=tools)

# 设定输入
message = [
    HumanMessage("六加六等于几?还有3乘3等于几?")
]

# 拿到 Ai 的输出
ai_message = model_with_tools.invoke(message)
print(ai_message)

# model_with_tools = model.bind_tools(tools=tools)
# tool_calls=[
# {'name': 'add', 'args': {'a': 6, 'b': 6}, 'id': 'call_00_CtcgfHx4mtXIRwaViYzY8152', 'type': 'tool_call'}
# ]
#
# model_with_tools = model.bind_tools(tools=tools, tool_choice="any")
# tool_calls=[
# {'name': 'add', 'args': {'a': 6, 'b': 6}, 'id': 'call_00_YfZyDeOxT1NFUe3cYAn96336', 'type': 'tool_call'},
# {'name': 'multiply', 'args': {'a': 3, 'b': 3}, 'id': 'call_01_TR2OJwcM0vFK36JrSLVU8287', 'type': 'tool_call'}
# ]

print("===============================================================")

message.append(ai_message)  # 加到一起, 后面给 ai 一起看
print(message)
print("===============================================================")

for tool_call in ai_message.tool_calls:
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    tool_message = selected_tool.invoke(tool_call)
    message.append(tool_message)

print(message)
print("===============================================================")

# 然后一起给 ai 调用
# 调用工具
print(model_with_tools.invoke(message).content)
