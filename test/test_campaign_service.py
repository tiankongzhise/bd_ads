from src.db import OauthDb,BdAuthTokenTable
from src.tool import BaiduOauthClient
from src.service import BaiduCampaignServiceClient

import os

class TestBaiduCampaignServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduCampaignServiceClient)

    def test_add_campaign(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
            'campaignTypes':[
                {
                    "campaignName":'测试',
                    # "pause":True,
                    'marketingTargetId':0,
            }
            ]
        }
        return self.client.add_campaign(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduCampaignServiceClient(uese_id,user_name)
    rsp = test_client.test_add_campaign()
    print(rsp)