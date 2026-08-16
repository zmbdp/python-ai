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

# JSON Schema
json_schema = {
    "title": "joke",
    "description": "给用户讲一个笑话。",
    "type": "object",
    "properties": {
    "setup": {
    "type": "string",
    "description": "这个笑话的开头",
    },
    "punchline": {
    "type": "string",
    "description": "这个笑话的妙语",
    },
    "rating": {
    "type": "integer",
    "description": "从1到10分，给这个笑话评分",
    "default": None,
    },
    },
    "required": ["setup", "punchline"],
}

model_with_structured = model.with_structured_output(json_schema)
print(model_with_structured.invoke("讲一个关于唱歌的笑话"))

# 【注意】虽然声明是 JSON，但返回的还是字符串
# {
#   'setup': '一个人去音乐厅唱歌，结果唱得太差，观众都跑了。他问指挥：‘为什么他们都走了？’指挥说：‘可能是他们觉得你的调子‘跑’得比他们都快！’',
#   'punchline': '他叹气：‘看来我唱歌不是跑调，是跑步级别了！’',
#   'rating': 8
# }