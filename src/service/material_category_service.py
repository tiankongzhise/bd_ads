from .base import BaseAPIClient
from typing import Dict

class BaiduWtMaterialCategoryServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/WtMaterialCategoryService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_category(self, content_data: Dict) -> Dict:
        """新增/更新分类"""
        return self.post("/updateCategory", data=content_data)
    
    def get_category_list(self, content_data: Dict) -> Dict:
        """获取分类列表"""
        return self.post("/getCategoryList", data=content_data)
    
    def delete_category(self, content_data: Dict)-> Dict:
        """删除分类"""
        return self.post("/deleteCategory", data=content_data)

