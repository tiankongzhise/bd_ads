from .base import BaseAPIClient
from typing import Dict

class BaiduMaterialBrandModServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialBrandModService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_brand(self, content_data: Dict) -> Dict:
        """新建品牌"""
        return self.post("/addBrand", data=content_data)
    
    def delete_brand(self, content_data: Dict)-> Dict:
        """删除品牌"""
        return self.post("/deleteBrand", data=content_data)
    
    def update_putaway(self, content_data: Dict)-> Dict:
        """发布/取消品牌"""
        return self.post("/updatePutaway", data=content_data)
    
class BaiduMaterialBrandQueryServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialBrandQueryService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    
    def get_brand_list(self, content_data: Dict) -> Dict:
        """查询品牌介绍信息"""
        return self.post("/getBrandList", data=content_data)
