from .base import BaseAPIClient
from typing import Dict

class BaiduCreativeServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/CreativeService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_creative(self, content_data: Dict) -> Dict:
        """新增关键词"""
        return self.post("/addCreative", data=content_data)
    
    def get_creative(self, content_data: Dict) -> Dict:
        """获取关键词列表"""
        return self.post("/getCreative", data=content_data)
    