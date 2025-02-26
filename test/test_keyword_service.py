from src.tool import BaiduOauthClient
from src.service import BaiduKeywordServiceClient

class TestBaiduKeywordServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduKeywordServiceClient)

    def test_add_keyword(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
            'keywordTypes':[
                {
                    'adgroupId':11056083632,
                    "keyword":'关键词测试1',
                    "matchType":2,
                    'phraseType':1
                    },
                {
                    'adgroupId':11056083633,
                    "keyword":'关键词测试2',
                    "matchType":2,
                    'phraseType':1
                    },

            ]
        }
        return self.client.add_keyword(query_params)
    


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduKeywordServiceClient(uese_id,user_name)
    rsp = test_client.test_add_keyword()
    print(rsp)