from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os

# 1. 定义 DeepSeek 模型
# 默认从系统环境变量中读取 DEEPSEEK_API_KEY
api_key = os.environ["DEEPSEEK_API_KEY"]
# 然后再定义 model
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

# 3. 定义输出解析器组件
parser = StrOutputParser()

# 定义好链之后就不需要手动调用大模型这些了，直接交给链执行

# 4. 定义链
chain = model | parser
# 5. 调用链并输出结果
print(chain.invoke(messages))