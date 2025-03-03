from .base import BaseAPIClient
from typing import Dict

class BaiduMaterialArticleServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/MaterialArticleService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_article(self, content_data: Dict) -> Dict:
        """新建文章"""
        return self.post("/addArticle", data=content_data)
    
    def get_article_list(self, content_data: Dict) -> Dict:
        """查询文章列表"""
        return self.post("/getArticleList", data=content_data)
    
    def delete_article(self, content_data: Dict)-> Dict:
        """删除文章"""
        return self.post("/deleteArticle", data=content_data)
    def update_putaway(self, content_data: Dict)-> Dict:
        """上下架文章"""
        return self.post("/updatePutaway", data=content_data)
    