import os
from typing import Optional, Union

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

api_key = os.environ["DASHSCOPE_API_KEY"]
model = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key,
)


# Pydantic 对象
class Joke(BaseModel):
    """给用户讲的一个笑话"""

    setup: str = Field(description="这个笑话的开头")
    punchline: str = Field(description="这个笑话的妙语")
    rating: Optional[int] = Field(default=None, description="从1-10分，给这个笑话评分")


class Response(BaseModel):
    """用以对话的方式回应。"""

    content: str = Field(description="用于对用户查询的会话响应")


class FinalResponse(BaseModel):
    """最终回复，选择合适的输出结构"""

    final_output: Union[Joke, Response]


model_with_structured = model.with_structured_output(FinalResponse)
print(model_with_structured.invoke("讲一个关于跳舞的笑话，用结构化输出给我"))
print(model_with_structured.invoke("你是谁？？？"))

# final_output=Joke(
#   setup='一只兔子去跳舞培训班报名，老师问它：“你会跳什么舞？”',
#   punchline='兔子认真地说：“我会跳‘兔子舞’，但你们得教我怎么‘左左、右右、前后、前前前’——因为我每次跳完就去拔萝卜，根本停不下来！”',
#   rating=3
# )
# final_output=Response(
#   content='
#       你好！我是DeepSeek，一个由深度求索公司创造的AI助手。我的使命是帮助你解答问题、提供信息和进行各种对话。无论你需要学习、创作、分析还是闲聊，我都会尽我所能为你提供帮助。😊\n
#       \n
#       有什么我可以为你做的吗？
#   '
# )