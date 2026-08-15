from langchain_core.tools import StructuredTool

# # 方式一:
# def add(a: int, b: int) -> int:
#     """两数相加"""
#     return a + b
# add_tool = StructuredTool.from_function(func=add)

# ===============================================================

# 方式二:
def add(a: int, b: int) -> int:
    return a + b
add_tool = StructuredTool.from_function(
    func=add,
    name="ADD",                                 # 可以更改工具名, 本来默认是函数名的
    description="两数相加",                      # 工具描述
)

# ===============================================================

print(add_tool.invoke({"a": 2, "b": 5}))
print("=============================================================")
print(add_tool.name)
print("=============================================================")
print(add_tool.description)
print("=============================================================")
print(add_tool.args)