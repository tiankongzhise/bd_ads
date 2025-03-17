from .base import BaseAPIClient
from typing import Dict

class BaiduOpenApiReportServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/OpenApiReportService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def get_report_data(self, content_data: Dict) -> Dict:
        """一站式多渠道报告"""
        return self.post("/getReportData", data=content_data)
    