from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import os

# 1. 定义 DeepSeek 模型
# 默认从系统环境变量中读取 DEEPSEEK_API_KEY
api_key = os.environ["DEEPSEEK_API_KEY"]

model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key
)

# 2. 定义消息
# 用户消息 HumanMessage
# 系统提示消息 SystemMessage
# AI 消息 AIMessage
messages = [
    SystemMessage(content="你是一个翻译助手，请根据用户输入给出相应的中译英或者英译中！"),
    HumanMessage(content="my name is xiaoming")
]

# 3. 调用大模型
result = model.invoke(messages)

# 4. 输出结果
print(result)