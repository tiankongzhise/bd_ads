from .base import BaseAPIClient
from typing import Dict

class BaiduAdgroupServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/AdgroupService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_adgroup(self, content_data: Dict) -> Dict:
        """新增推广单元"""
        return self.post("/addAdgroup", data=content_data)
    
    def get_adgroup(self, content_data: Dict) -> Dict:
        """获取推广单元列表"""
        return self.post("/getAdgroup", data=content_data)
    