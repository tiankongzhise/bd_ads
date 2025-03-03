from .base import BaseAPIClient
from typing import Dict

class BaiduImageManageServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/ImageManageService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def upload_image(self, content_data: Dict) -> Dict:
        """上传图片"""
        return self.post("/uploadImage", data=content_data)
    
    def get_image_list(self, content_data: Dict) -> Dict:
        """查询文章列表"""
        return self.post("/getImageList", data=content_data)
    
    def delete_image(self, content_data: Dict)-> Dict:
        """删除图片"""
        return self.post("/delImage", data=content_data)
    def mod_image(self, content_data: Dict)-> Dict:
        """编辑图片"""
        return self.post("/modImage", data=content_data)
    def share_image(self, content_data: Dict)-> Dict:
        """分享图片"""
        return self.post("/shareImage", data=content_data)
