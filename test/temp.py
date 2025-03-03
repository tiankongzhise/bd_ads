from src.tool.debug_tool import debug_decorator
@debug_decorator
def divide(a, b):
    """除法函数"""
    return a / b

def calculator():
    print(divide(10, 2))  # 正常调用
    divide(a=5, b=0)          # 触发异常

calculator()
