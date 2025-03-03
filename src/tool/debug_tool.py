import functools
import inspect
import traceback
import sys

def debug_decorator(func):
    @functools.wraps(func)  # 关键：保留原函数元信息[1,6](@ref)
    def wrapper(*args, **kwargs):
        # 获取调用者信息
        caller_frame = inspect.currentframe().f_back
        caller_name = caller_frame.f_code.co_name
        
        
        try:
            # 记录输入参数
            print(f"🟢 函数调用追踪: {func.__name__}")
            print(f"   ├─ 调用者: {caller_name}")
            print(f"   ├─ 位置参数: {args}")
            print(f"   ├─ 关键字参数: {kwargs}")
            
            # 执行原函数
            result = func(*args, **kwargs)
            
            # 记录输出结果
            print(f"   └─ 返回值: {result}")
            return result
        except Exception as e:
            # 异常处理
            _, _, tb = sys.exc_info()
            last_traceback = traceback.extract_tb(tb)[-1]
            
            print(f"🔴 异常捕获: {func.__name__}")
            print(f"   ├─ 异常类型: {type(e).__name__}")
            print(f"   ├─ 错误信息: {str(e)}")
            print(f"   ├─ 出错文件: {last_traceback.filename}")
            print(f"   ├─ 出错行号: {last_traceback.lineno}")
            print(f"   └─ 调用者栈: {caller_name}")
            
            # 保留原始异常堆栈[6](@ref)
            raise e.with_traceback(tb)
            
    return wrapper
