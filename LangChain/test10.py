import os
from typing import Iterator, List

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

api_key = os.environ["DEEPSEEK_API_KEY"]
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key
)

parser = StrOutputParser()

# 自定义生成器
def split_into_list(input: Iterator[str]) -> Iterator[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        # 遇到。需要刷新
        while "。" in buffer:
            # 找到。的位置
            stop_index = buffer.index("。")
            # yield 用于创造生成器
            yield [buffer[:stop_index].strip()]
            buffer = buffer[stop_index + 1 :]
    # 处理buffer最后几个字
    yield [buffer.strip()]

chain = model | parser | split_into_list

# 返回一个迭代器，产生的消息块
for chunk in chain.stream("写一段关于爱情的歌词，需要5句话，每句话用中文句号隔开。"):
    # chunk: AIMessageChunk
    # print(chunk.content, end="|", flush=True)
    # 使用 parser，结果就是 str
    print(chunk, end="|", flush=True)
# ['你眼里的星光是洒向我的第一场雨季']|
# ['心跳总在触碰你名字的瞬间突然安静']|
# ['我们像两棵逆向生长的树，却在泥土下缠紧了根须']|
# ['原来最深的拥抱不过是，把叹息和沉默都算作同行']|
# ['若爱是易碎的容器，我愿做那个永远接住你的支点']|
# ['']|

# tmp_chunks = chunks[0] + chunks[1] + chunks[2] + chunks[3]

# print(tmp_chunks)
