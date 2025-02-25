# from src import db 
# from src import oauth 
from src.db import OauthDb,BdAuthTokenTable
from src.oauth import BaiduOauthClient

import os


def test_get_user_info(uese_id):
    # 创建数据库连接
    db_client = OauthDb()
    with db_client.get_db() as session:

        # 创建OauthClient实例
        oauth_client = BaiduOauthClient(
            app_id=os.getenv("APP_ID"),
            secret_key=os.getenv("SECRET_KEY"),
        )
        result = session.query(BdAuthTokenTable.openId,BdAuthTokenTable.accessToken).filter(BdAuthTokenTable.userId == uese_id).first()
        print(result)
        open_id,access_token = result
        # 获取用户信息
        user_info = oauth_client.get_user_info(
            openId=open_id,
            accessToken=access_token,
            userId=uese_id,
            needSubList=True
        )
    print(user_info)


if __name__ == "__main__":
    uese_id = '64339991'
    test_get_user_info(uese_id)
