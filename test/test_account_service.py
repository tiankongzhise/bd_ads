from src.db import OauthDb,BdAuthTokenTable
from src.tool import BaiduOauthClient
from src.service import BaiduAccountServiceClient

import os

class TestBaiduAccountServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduAccountServiceClient)

    def test_get_account_info(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                'accountFields':[
                    'userId',
                    'balance',
                    'budget'
                ]
            }
        return self.client.get_account_info(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduAccountServiceClient(uese_id,user_name)
    rsp = test_client.test_get_account_info()
    print(rsp)