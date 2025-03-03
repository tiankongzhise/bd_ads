from .base import BaseAPIClient
from typing import Dict

class BaiduMaterialBindModServiceServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialBindModService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_material_bind(self, content_data: Dict) -> Dict:
        """添加物料绑定关系"""
        return self.post("/addMaterialBind", data=content_data)
    
    def delete_material_bind(self, content_data: Dict)-> Dict:
        """删除物料绑定关系"""
        return self.post("/deleteMaterialBind", data=content_data)
    
class BaiduMaterialCenterBindQueryServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialCenterBindQueryService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    
    def get_material_bind(self, content_data: Dict) -> Dict:
        """查询物料绑定关系"""
        return self.post("/getMaterialBind", data=content_data)
