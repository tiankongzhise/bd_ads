from src.tool import BaiduOauthClient,ServiceTool
from src.service import BaiduAdvancedSegmentServiceClient
import json
from tqdm import tqdm

class TestBaiduAdvancedSegmentServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduAdvancedSegmentServiceClient)

    def test_add_segment(self,query_params:dict|None|list = None):
        if query_params is None:
            with open('bd_ads_brand_segment.json','r',encoding='utf-8') as f:
                query_params = json.load(f)
        if isinstance(query_params,list):
            query_params = {
                'items':query_params
            }
        if 'items' not in query_params.keys():
            query_params = {
                'items':[query_params]
            }

            
            
        return self.client.add_segment(query_params)
    
    def test_get_segment(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                'ids':[],
                'idType':2,
                'segmentTypes':[510]
            }
        return self.client.get_segment(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    user_list = ServiceTool.get_user_list(uese_id)
    for user_name in tqdm(user_list,desc='新建品牌信息'):
        test_client = TestBaiduAdvancedSegmentServiceClient(uese_id,user_name)
        rsp = test_client.test_add_segment()
        print(f'账号:{user_name},新建品牌信息结果:{rsp}')
