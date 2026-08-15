import os

from langchain_openai import ChatOpenAI
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage

# 定义大模型
api_key = os.environ["DASHSCOPE_API_KEY"]
model = ChatOpenAI(
    model="glm-5.2",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key,
)


class Person(BaseModel):
    """一个人的信息。"""

    # 注意：
    # 1. 每个字段都是 Optional "可选的" — 允许 LLM 在不知道答案时输出 None。
    # 2. 每个字段都有一个 description "描述" — LLM 使用这个描述。
    # 有一个好的描述可以帮助提高提取结果。
    name: Optional[str] = Field(default=None, description="这个人的名字")
    hair_color: Optional[str] = Field(default=None, description="如果知道这个人头发的颜色")
    skin_color: Optional[str] = Field(default=None, description="如果知道这个人的肤色")
    height_in_meters: Optional[str] = Field(default=None, description="身高以米为单位的高度")


structured_model = model.with_structured_output(schema=Person)
messages = [
    SystemMessage(content="你是一个提取信息的专家。从文本中提取信息，如果身高是英尺单位，请换算成米（1英尺=0.3048米），只返回数值。如果不知道属性值，返回null。"),
    HumanMessage(content="史密斯他身高6英尺，金发。")
    # HumanMessage(content="史密斯他身高6英尺，长得黝黑黝黑的，金发。")
]

result = structured_model.invoke(messages)
print(result)
# name='史密斯' hair_color='金发' skin_color=None height_in_meters='1.83'
# name='史密斯' hair_color='金发' skin_color='黝黑' height_in_meters=None          模型不聪明，身高未识别到