import os
from typing import Optional, TypedDict, Annotated

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

api_key = os.environ["DASHSCOPE_API_KEY"]
model = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key,
)


# TypedDict 对象
class Joke(TypedDict):
    """给用户讲的一个笑话"""

    setup: Annotated[str, ..., "这个笑话的开头"]
    punchline: Annotated[str, ..., "这个笑话的妙语"]
    rating: Annotated[Optional[int], None, "从1-10分，给这个笑话评分"]


# model_with_structured = model.with_structured_output(Joke)
# print(model_with_structured.invoke("分别讲一个关于唱歌和跳舞的笑话"))
# # {
# #   'setup': '唱歌的人为什么总是很累？',
# #   'punchline': '因为他们每天都在练高音，结果把力气都唱没了。',
# #   'rating': 6
# # }

class Data(BaseModel):
    """获取关于笑话的数据列表"""

    jokes: list[Joke]


# ================================================================================================================

model_with_structured = model.with_structured_output(Data)
print(model_with_structured.invoke("分别讲一个关于唱歌和跳舞的笑话"))
# jokes=[
#   {
#       'setup': '唱歌的笑话',
#       'punchline': "
#           一个五音不全的人去参加合唱团面试。\n
#           面试官说：'请唱一首歌。'\n
#           他唱完后，面试官沉默了很久，说：'你的音准……很有创意。'\n
#           他高兴地问：'那我能加入吗？'\n
#           面试官回答：'不，我们怕你带坏其他音符。',
#       'rating': 1
#       "
#   },
#   {
#       'setup': '跳舞的笑话',
#       'punchline': "
#           一个人去看舞蹈表演，发现有个舞者一直在原地转圈。\n
#           他问旁边的人：'那个舞者为什么一直转？'\n
#           旁边的人说：'因为他跳的是《陀螺之舞》。'\n
#           过了一会儿，转圈的舞者突然摔倒了。\n
#           那人又问：'现在呢？'\n
#           旁边的人叹气：'哦，他进入了第二乐章——'晕头转向'。,
#       'rating': 2
#       "
#   }
# ]