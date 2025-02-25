from base import BaseAPIClient
from typing import Dict

class BaiduContentAPIClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/CampaignService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_campaign(self, content_data: Dict) -> Dict:
        """新增推广计划"""
        return self.post("/addCampaign", data=content_data)
    
    