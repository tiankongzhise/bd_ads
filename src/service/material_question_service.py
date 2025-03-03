from .base import BaseAPIClient
from typing import Dict

class BaiduMaterialQuestionModServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialQuestionModService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_question(self, content_data: Dict) -> Dict:
        """新建问答"""
        return self.post("/addQuestion", data=content_data)
    
    def delete_question(self, content_data: Dict)-> Dict:
        """批量删除问答"""
        return self.post("/deleteQuestion", data=content_data)
    
    def update_putaway(self, content_data: Dict)-> Dict:
        """批量上下架问答"""
        return self.post("/updatePutaway", data=content_data)
    
class BaiduMaterialQuestionQueryServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialQuestionQueryService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    
    def get_question_list(self, content_data: Dict) -> Dict:
        """查询问答列表"""
        return self.post("/getQuestionList", data=content_data)
