from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import os

from openai import BaseModel
from pydantic import Field

api_key = os.environ["DASHSCOPE_API_KEY"]
model = ChatOpenAI(
    model="glm-5.2",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key,
)

tool = TavilySearch(
    max_retries=5  # 搜索最大结果数
)
# 先绑定工具
model_with_tools = model.bind_tools([tool])

message = [
    HumanMessage("上海浦东新区现在的天气怎么样？")
]
ai_message = model_with_tools.invoke(message)
message.append(ai_message)

for tool_call in ai_message.tool_calls:
    selected_tool = {"tavily_search": tool}[tool_call["name"].lower()]
    tool_message = selected_tool.invoke(tool_call)
    message.append(tool_message)


class SearchResult(BaseModel):
    """结构化搜索对象"""
    query: str = Field(description="搜索查询")
    findings: str = Field(description="查询结果摘要")

# 再绑定结构化数据
model_with_structured = model_with_tools.with_structured_output(SearchResult)

print(model_with_structured.invoke(message))
# SearchResult(
#   query='上海浦东新区现在天气',
#   findings='根据 MSN 天气数据，上海浦东新区目前的天气情况如下：',
#   current_conditions={
#       'temperature': '25°C',
#       'condition': '阴',
#       'feels_like': '27°C',
#       'humidity': '91%',
#       'wind': '西风 2级',
#       'wind_speed': '6-11 公里/小时',
#       'air_quality': '优 (41)',
#       'primary_pollutant': 'NO₂ 21 ppb',
#       'visibility': '7.7 公里',
#       'air_pressure': '1007 hPa'
#   },
#   interpretation='当前气温适中，体感温度略高于实际气温。湿度较高，体感可能会比较潮湿。空气质量优秀，适合户外活动。能见度良好。'
# )
