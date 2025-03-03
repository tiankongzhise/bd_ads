from .base import BaseAPIClient
from typing import Dict

class BaiduMaterialPersonModServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialPersonModService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_person(self, content_data: Dict) -> Dict:
        """新建人员"""
        return self.post("/addPerson", data=content_data)
    
    def delete_person(self, content_data: Dict)-> Dict:
        """批量删除人员"""
        return self.post("/deletePerson", data=content_data)
    
    def update_putaway(self, content_data: Dict)-> Dict:
        """批量发布/取消发布人员"""
        return self.post("/updatePutaway", data=content_data)
    
class BaiduMaterialPersonQueryServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialPersonQueryService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    
    def get_person_list(self, content_data: Dict) -> Dict:
        """查询人员列表"""
        return self.post("/getPersonList", data=content_data)
