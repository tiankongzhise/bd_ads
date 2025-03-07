from .base import BaseAPIClient
from typing import Dict

class BaiduAdvancedSegmentServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/AdvancedSegmentService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def get_segment(self, content_data: Dict) -> Dict:
        """查询组件"""
        return self.post("/getSegment", data=content_data)
    
    def add_segment(self, content_data: Dict) -> Dict:
        """添加组件"""
        return self.post("/addSegment", data=content_data)
    def update_segment(self, content_data: Dict)-> Dict:
        """更新组件"""
        return self.post("/updateSegment", data=content_data)
    
    def delete_segment(self, content_data: Dict)-> Dict:
        """删除组件"""
        return self.post("/deleteSegment", data=content_data)
    