# 导入本地服务
from src.db import  OauthDb,BdAuthTokenTable
from src.oauth import BaiduOauthService
from src.service.base import BaseAPIClient
# 导入系统库
from datetime import datetime, timedelta
import os
from typing import Type

# 导入第三方库
from dotenv import load_dotenv

load_dotenv()

#最大重试次数
MAX_RETRY_TIME = 3

class BaiduOauthClient(object):
    def __init__(self,user_id:str,db:OauthDb|None = None):
        self.db = db or OauthDb()
        self.user_id = user_id
    def get_oauth_info(self,user_id:str|None = None):
        if user_id is None:
            user_id = self.user_id

        with self.db.get_session() as session:
            return session.query(BdAuthTokenTable).filter(BdAuthTokenTable.userId == user_id).first()

    def create_oauth_client(self,user_name:str,service_mode:Type[BaseAPIClient],user_id:str|None = None,force_refresh:bool = False)->Type[BaseAPIClient]:
        if user_id is None:
            user_id = self.user_id
        oauth_info = self.get_oauth_info(user_id)
        if oauth_info is None:
            raise Exception(f'账户中心id{user_id}并未有权限信息，请先进行授权')

        if (not self.is_token_expiring_soon(oauth_info.expiresTime)) and (not force_refresh) :
            return service_mode(access_token=oauth_info.accessToken,user_name=user_name)
        
        if self.is_token_expired(oauth_info.refreshExpiresTime):
            raise Exception('refresh Token expired time,need to reoauth')
        
        app_id = os.getenv("APP_ID")
        secret_key = os.getenv("SECRET_KEY")
        oauth_service = BaiduOauthService(app_id=app_id,secret_key=secret_key)
        re_try_time = 0
        while re_try_time < MAX_RETRY_TIME:
            try:
                rsp = oauth_service.refresh_token(user_id=user_id,refresh_token=oauth_info.refreshToken)
                if rsp['code'] == 0:
                    update_data = {
                    'userId': user_id,
                    'accessToken' : rsp['data']['accessToken'],
                    'expiresTime' : rsp['data']['expiresTime'],
                    'refreshToken' : rsp['data']['refreshToken'],
                    'refreshExpiresTime' : rsp['data']['refreshExpiresTime'],
                    'openId': rsp['data']['openId'],
                    }
                    self.db.dynamic_update(BdAuthTokenTable,update_data)
                    return service_mode(access_token=update_data['accessToken'],user_name=user_name)
                else:
                    re_try_time += 1
                    print(f'refresh token failed,because of service {rsp['message']},正在重试')
                    continue
            except Exception as e:
                re_try_time += 1
                print(f'refresh token failed,because of err{e},正在重试')
        print('refresh token failed,because of max retry time')
        raise Exception('refresh token failed')
        

        

    def is_token_expired(self,expiry_time: datetime) -> bool:
        """
        判断给定的日期时间是否已经过期。
        :param expiry_time: 过期时间
        :return: 如果已经过期，返回True；否则返回False
        """
        current_time = datetime.now()
        return expiry_time < current_time
    def is_token_expiring_soon(self,expiry_time: datetime) -> bool:
        """
        判断给定的日期时间是否距离过期还有2个小时以上。
        :param expiry_time: 过期时间
        :return: 如果距离过期时间小于2小时，返回True；否则返回False
        """
        current_time = datetime.now()
        time_difference = expiry_time - current_time
        return time_difference < timedelta(hours=2)

