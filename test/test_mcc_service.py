
from src.db import BdServiceDb,BdAdCenterBindTable
from src.tool import BaiduOauthClient
from src.service import BaiduMccServiceClient

import os

class TestBdAdCenterBindTable(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduMccServiceClient)

    def test_get_user_list(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                'mccId':'64339991'
            }
        return self.client.get_user_list(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBdAdCenterBindTable(uese_id,user_name)
    rsp = test_client.test_get_user_list()
    print(rsp)
