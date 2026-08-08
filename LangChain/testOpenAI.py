from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# 1. 定义 OpenAI 模型
# 默认从系统环境变量中读取 OPENAI_API_KEY
model = ChatOpenAI(model="gpt-4o-mini")

# 2. 定义消息
# 用户消息 HumanMessage
# 系统提示消息 SystemMessage
# AI 消息 AIMessage
messages = [
    SystemMessage(content="你是一个翻译助手，请根据用户输入给出相应的中译英或者是英译中！"),
    HumanMessage(content="hello")
]

# 3. 调用大模型
result = model.invoke(messages)

# 4. 输出结果
print(result)

# 5. 定义输出解析器组件
parser = StrOutputParser()
print(parser.invoke(result))

# 6. 定义链
chain = model | parser