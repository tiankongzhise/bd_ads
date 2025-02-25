import requests
from typing import Optional, Dict, Any
from src.log.ApiLogger import APILogger,LogLevel

class APIClientError(Exception):
    """自定义API异常基类"""
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.status_code = status_code
        super().__init__(message)


class BaseAPIClient:
    def __init__(
        self,
        base_url: str,
        access_token: str,
        user_name:str,
        timeout: int = 10,
        session: Optional[requests.Session] = None,
        logger: Optional[APILogger] = None,
        **kwargs
    ):
        self.base_url = base_url.rstrip('/')
        self.access_token = access_token
        self.user_name = user_name
        self.timeout = timeout
        self.session = session or requests.Session()
        self.logger = logger or APILogger(level=LogLevel.BASIC)
        
        # 公共请求头配置
        self.session.headers.update({
            'userName':self.user_name,
            'accessToken':self.access_token,
        })
    @APILogger.log_request
    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """统一请求处理方法"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise APIClientError(
                f"API请求失败: {e}",
                status_code=e.response.status_code
            ) from e
        except requests.exceptions.RequestException as e:
            raise APIClientError(f"网络请求异常: {e}") from e

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        return self._request("POST", endpoint, json=data)

    # 可根据需要添加 put/patch/delete 等方法
