from src.tool import BaiduOauthClient
from src.service import BaiduMaterialArticleServiceClient

class TestBaiduMaterialArticleServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduMaterialArticleServiceClient)

    def test_get_article_list(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
            'keywordTypes':[
                {
                    'pageNum':1,
                    "pageSize":500,
                    "materialType":2,
                    }
                # {
                #     'pageNum':1,
                #     "pageSize":500,
                #     "materialType":7,
                #     },

            ]
        }
        return self.client.get_article_list(query_params)
    


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛教育'
    test_client = TestBaiduMaterialArticleServiceClient(uese_id,user_name)
    rsp = test_client.test_get_article_list()
    print(rsp)
