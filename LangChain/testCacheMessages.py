import os
from typing import Iterator, List

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, trim_messages
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

api_key = os.environ["DEEPSEEK_API_KEY"]
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key
)

store = {}

# 根据会话 id 查询会话里的消息列表
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        # InMemoryChatMessageHistory() 帮助我们将 AIMessage、HumanMessage 等消息自动添加进来
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# trim
# 使用 trim_messages 减少发送给模型的消息数量
trimmer = trim_messages(
    max_tokens=3,              # 修剪消息的最大令牌数，根据你想要的谈话长度来调整 token_counter 为 model 时，表示截取的单位是 token，token_counter 为 len 时，表示截取的单位是条数
    strategy="last",            # 修剪策略："last"（默认）：从后往前保留。"first"：从前往后保留。
    # token_counter=model,        # 传入一个函数或一个语言模型（因为语言模型有消息令牌计数方法）model 表示截取的单位是 token 数，max_tokens=65这东西
    token_counter = len,        # len 表示截取单位是消息的条数
    include_system=True,        # 如果想始终保留初始系统消息，可以指定 include_system=True
    allow_partial=False,        # 是否允许拆分消息的内容
    start_on="human",           # 如果需要确保我们的第一条消息（不包括系统消息）始终是特定类型，可以指定 start_on
)

# 包装了 model，让model具备存储历史消息的能力
# with_history_message_model = RunnableWithMessageHistory(model, get_session_history)

# 包装了 model，让model具备存储历史消息的能力
chain = trimmer | model
with_history_message_model = RunnableWithMessageHistory(chain, get_session_history)

# model: Runnable 实例
# invoke: config: 配置 Runnable 实例
config = {"configurable": {"session_id": "1"}}

# ======================================写死输入=========================================

# with_history_message_model.invoke(
#     input=[HumanMessage(content="我是小明，你好！")],
#     config=config,
# ).pretty_print()
#
# with_history_message_model.invoke(
#     input=[HumanMessage(content="你知道我是谁吗？")],
#     config=config,
# ).pretty_print()

# ======================================持续输入=========================================
print("开始对话，输入 'exit' 或 'quit' 退出")
while True:
    user_input = input("你: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        print("对话结束")
        break

    with_history_message_model.invoke(
        input=[HumanMessage(content=user_input)],
        config=config,
    ).pretty_print()

