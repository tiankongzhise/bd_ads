from .base import BaseAPIClient
from typing import Dict

class BaiduMaterialProductServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialProductService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_product(self, content_data: Dict) -> Dict:
        """创建产品"""
        return self.post("/addProduct", data=content_data)
    
    def get_product_list(self, content_data: Dict) -> Dict:
        """查询产品列表"""
        return self.post("/getProductList", data=content_data)
    
    def delete_product(self, content_data: Dict)-> Dict:
        """删除产品"""
        return self.post("/deleteProduct", data=content_data)
    def update_putaway(self, content_data: Dict)-> Dict:
        """上架/下架产品"""
        return self.post("/updatePutaway", data=content_data)
    