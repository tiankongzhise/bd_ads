from src.tool import BaiduOauthClient
from src.service import BaiduWtMaterialCategoryServiceClient

class TestBaiduWtMaterialCategoryServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduWtMaterialCategoryServiceClient)

    def test_get_category_list(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                    'pageNum':1,
                    "pageSize":500,
                    "type":4
        }
        rsp =  self.client.get_category_list(query_params)
        if rsp['header']['desc'] != 'success':
            raise Exception(f'获取分类列表失败:{rsp}')
        category_list = rsp['body']['data'][0]['list']
        result = {}
        for category_info in category_list:
            result[category_info['categoryId']] = {
                'name':category_info['name'],
                'type':category_info['type']
            }
        return result
    


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduWtMaterialCategoryServiceClient(uese_id,user_name)
    rsp = test_client.test_get_category_list()
    print(rsp)
