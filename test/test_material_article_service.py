from src.tool import BaiduOauthClient
from src.service import BaiduMaterialArticleServiceClient

class TestBaiduMaterialArticleServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduMaterialArticleServiceClient)

    def test_get_article_list(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                    'pageNum':1,
                    "pageSize":500,
                    "materialType":2,
        }
        return self.client.get_article_list(query_params)
    
    def test_update_putaway(self,article_id:list):
        query_params = {
            'articleIdList':article_id,
            'status':4
        }
        return self.client.update_putaway(query_params)
    
    
    def test_del_article(self,article_id:list):
        rsp = self.test_update_putaway(article_id)
        print(f'更新文章状态成功:{rsp}')
        query_params = {
            'articleIdList':article_id
        }
        return self.client.delete_article(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduMaterialArticleServiceClient(uese_id,user_name)
    rsp = test_client.test_get_article_list()
    if rsp['header']['desc'] != 'success':
        print('获取文章列表失败')
    article_id_list = []
    for article_info in rsp['body']['data'][0]['list']:
        article_id_list.append(article_info['articleId'])
    rsp = test_client.test_del_article(article_id_list)
    print(f'删除文章成功:{rsp}')
    
    
