import os
from typing import Optional

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
    """给用户讲一个笑话"""

    setup: str = Field(description="这个笑话的开头")
    punchline: str = Field(description="这个笑话的妙语")
    rating: Optional[int] = Field(default=None, description="从1-10分，给这个笑话评分")


class Data(BaseModel):
    """获取关于笑话的数据列表"""

    jokes: list[Joke]


# ================================================================================================================

model_with_structured = model.with_structured_output(Data)
print(model_with_structured.invoke("分别讲一个关于唱歌和跳舞的笑话"))

# jokes=[
#   Joke(setup='一个人唱歌总是跑调，唱完之后，朋友对他说：', punchline='朋友说：“你唱歌真好听，就是有点费调。”', rating=7),
#   Joke(setup='一个人跳舞时总踩到舞伴的脚，舞伴终于忍不住说：', punchline='舞伴说：“你跳得真好，就是步子有点大。”', rating=7)
# ]

# ================================================================================================================

# model_with_structured = model.with_structured_output(Joke)
# print(model_with_structured.invoke("讲一个关于唱歌的笑话"))

# setup='有个五音不全的人去参加合唱团面试，'
# punchline='面试官听完后沉默良久，终于开口：‘您这唱法吧……我们这儿是合唱团，不是‘拆’合唱团。’'
# rating=5

# ================================================================================================================

# print(model.invoke("讲一个关于唱歌的笑话").content)

# 给你讲两个关于唱歌的笑话，一个是短平快的，一个是画面感极强的：
#
# ### 笑话一：费钱的爱好
#
# 一个男生去相亲，女方问他：“你平时有什么爱好吗？”
# 男生想展现一下自己，就说：“我特别喜欢唱歌，朋友们都叫我‘原唱杀手’。”
# 女方眼睛一亮：“哇，那你唱得一定很好听吧？不过唱歌怎么会‘费钱’呢？是因为你唱得太好听，朋友们都抢着给你打赏吗？”
# 男生叹了口气，幽幽地说：“不是……是因为每次我去KTV唱歌，唱到一半，服务员都会进来塞给我两百块钱，求我放下麦克风，去外面吃点果盘。”
#
# ***
#
# ### 笑话二：KTV里的“灵魂歌手”
#
# 老王是个名副其实的“麦霸”，但五音不全，杀伤力极大。
# 周末，他和几个朋友去KTV聚会。酒过三巡，老王拿起麦克风，点了一首《死了都要爱》。他闭着眼睛，青筋暴起，唱得撕心裂肺。那高音破得，简直像指甲刮黑板一样刺耳。
# 朋友们在沙发上痛苦地捂着耳朵，但碍于面子不敢切他的歌。
#
# 唱到最高潮的时候，包厢门突然被“砰”地一声推开了，冲进来三个保安。
# 保安队长一把夺过老王的麦克风，气喘吁吁地说：“大哥，快别唱了！”
# 老王很不高兴：“怎么了？我唱得不好听吗？你们KTV还管客人唱歌？”
#
# 保安队长快哭了：“大哥，你唱得好不好听我们不管。但是隔壁包厢的客人刚才打前台电话，说你们包厢有人在 **‘严刑逼供’**，再不把麦克风给他，他就要报警了！”
# 老王：“……”
# 朋友们：“……”
#
# 保安队长接着说：“而且，楼下大厅的客人问我们，是不是店里的**消防警报器坏了**，怎么一直发出这种尖锐的惨叫声？”
