from .base import BaseAPIClient
from typing import Dict

class BaiduLeadsNoticeServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/LeadsNoticeService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def get_notice_list(self, content_data: Dict) -> Dict:
        """获取线索信息"""
        return self.post("/getNoticeList", data=content_data)
    