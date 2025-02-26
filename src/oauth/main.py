from .base import BaseAPIClient
from typing import Dict, Any, Optional

class BaiduOauthService(BaseAPIClient):
    def __init__(self, app_id: str, secret_key:str,**kwargs):
        super().__init__(
            base_url="https://u.baidu.com/oauth/",  # 根据实际文档替换
            app_id=app_id,
            secret_key=secret_key,
            **kwargs
        )
    
    def access_token(self,user_id:int|str,auth_code: str) -> Dict:
        """换取授权令牌"""
        content_data = {
            "appId": self.app_id,
            "authCode": auth_code,
            "secretKey": self.secret_key,
            "grantType": "auth_code",
            'userId':int(user_id)
        }
        return self.post("/accessToken", data=content_data)
    
    def refresh_token(self, user_id: int|str,refresh_token:str) -> Dict:
        """更新授权令牌"""
        content_data = {
            "appId": self.app_id,
            "refreshToken": refresh_token,
            "secretKey": self.secret_key,
            'userId':int(user_id)
        }
        return self.post("/refreshToken",data=content_data)
    
    def get_user_info(self,
                      openId:int|str,
                      accessToken:str,
                      userId:int|str,
                      needSubList:bool = False, 
                      pageSize:int = 500,
                      lastPageMaxUcId:int|str = 1
        ):
        """查询授权用户信息"""
        content_data = {
            "openId": openId,
            "accessToken": accessToken,
            "userId": userId,
            "needSubList": needSubList,
            "pageSize": pageSize,
            "lastPageMaxUcId": lastPageMaxUcId
        }
        return self.post("/getUserInfo",data=content_data)
