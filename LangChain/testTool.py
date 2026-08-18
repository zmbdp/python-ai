from typing_extensions import Annotated

from langchain_core.tools import tool
from pydantic import BaseModel, Field


# 定义工具

# # 方式一:
# @tool
# def add(a: int, b: int) -> int:
#     """
#     两数相加
#     :param a: 第一个整数
#     :param b: 第二个整数
#     :return: 两个整数的和
#     """
#     return a + b

# ===============================================================

# # 方式二:
# class AddInput(BaseModel):
#     """两数相加"""
#
#     a: int = Field(..., description="第一个整数")
#     b: int = Field(..., description="第二个整数")
#
# @tool(args_schema=AddInput)
# def add(a: int, b: int) -> int:
#     return a + b

# ===============================================================

# 方式三:
@tool
def add(
        a: Annotated[int, ..., "第一个整数"],
        b: Annotated[int, ..., "第二个整数"]
) -> int:
    """
    两数相加
    :param a: 第一个整数
    :param b: 第二个整数
    :return: 两个整数的和
    """
    return a + b

# ===============================================================


print(add.invoke({"a": 3, "b": 5}))
print("=============================================================")
print(add.name)
print("=============================================================")
print(add.description)
print("=============================================================")
print(add.args)
