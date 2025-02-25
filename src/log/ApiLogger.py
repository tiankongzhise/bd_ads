import logging
from datetime import datetime
from typing import Optional, Dict, Any, Callable
from functools import wraps

# 日志级别枚举
class LogLevel:
    BASIC = "basic"
    DETAIL = "detail"
    DEBUG = "debug"

class APILogger:
    def __init__(self, logger: Optional[logging.Logger] = None, level: str = LogLevel.BASIC):
        self.logger = logger or logging.getLogger(__name__)
        self.level = level
        self._log_strategy = self._get_strategy()

    def _get_strategy(self) -> Callable:
        strategies = {
            LogLevel.BASIC: self._basic_log,
            LogLevel.DETAIL: self._detail_log,
            LogLevel.DEBUG: self._debug_log
        }
        return strategies.get(self.level, self._basic_log)

    def log_request(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(client, endpoint, *args, **kwargs):
            # 记录开始信息
            start_time = datetime.now()
            module_name = client.__class__.__name__
            
            log_data = {
                "module": module_name,
                "endpoint": endpoint,
                "method": func.__name__.upper(),
                "params": kwargs.get('params', {}),
                "json": kwargs.get('json', {}),
                "start_time": start_time
            }

            self._log_strategy("start", log_data)
            
            try:
                result = func(client, endpoint, *args, **kwargs)
                duration = (datetime.now() - start_time).total_seconds()
                
                # 记录成功信息
                self._log_strategy("success", {
                    **log_data,
                    "duration": duration,
                    "response": result
                })
                return result
            except Exception as e:
                # 记录错误信息
                duration = (datetime.now() - start_time).total_seconds()
                self._log_strategy("error", {
                    **log_data,
                    "duration": duration,
                    "error": str(e)
                })
                raise

        return wrapper

    def _basic_log(self, event_type: str, data: Dict):
        msg = {
            "start": f"[{data['module']}] 开始请求 {data['endpoint']}",
            "success": (
                f"[{data['module']}] 请求成功 {data['endpoint']} "
                f"耗时 {data.get('duration',0):.2f}s 状态码: 200"
            ),
            "error": (
                f"[{data['module']}] 请求失败 {data['endpoint']} "
                f"耗时 {data.get('duration',0):.2f}s 错误: {data.get('error')}"
            )
        }[event_type]
        self.logger.info(msg)

    def _detail_log(self, event_type: str, data: Dict):
        if event_type == "start":
            self.logger.info(
                f"[{data['module']}] 请求开始\n"
                f"Endpoint: {data['endpoint']}\n"
                f"Method: {data['method']}\n"
                f"Params: {data['params']}\n"
                f"JSON: {data['json']}"
            )
        elif event_type == "success":
            self.logger.info(
                f"[{data['module']}] 请求成功 (耗时 {data['duration']:.2f}s)\n"
                f"Response: {data['response']}"
            )
        else:
            self.logger.error(
                f"[{data['module']}] 请求失败 (耗时 {data['duration']:.2f}s)\n"
                f"Error: {data['error']}"
            )

    def _debug_log(self, event_type: str, data: Dict):
        # 包含堆栈跟踪等调试信息
        if event_type == "start":
            self.logger.debug(f"Full request data: {data}")
        else:
            self._detail_log(event_type, data)

