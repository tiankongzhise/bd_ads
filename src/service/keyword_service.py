from .base import BaseAPIClient
from typing import Dict

class BaiduKeywordServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/KeywordService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_keyword(self, content_data: Dict) -> Dict:
        """新增关键词"""
        return self.post("/addWord", data=content_data)
    
    def get_keyword(self, content_data: Dict) -> Dict:
        """获取关键词列表"""
        return self.post("/getWord", data=content_data)
    