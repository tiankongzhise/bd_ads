from .base import BaseAPIClient
from typing import Dict

class BaiduMccServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/feed/v1/MccFeedService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def get_user_list(self, content_data: Dict) -> Dict:
        """获取推广计划列表"""
        return self.post("/getUserListByMccid", data=content_data)
    