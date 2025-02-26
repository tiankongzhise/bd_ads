from src.tool import BaiduOauthClient
from src.service import BaiduCreativeServiceClient

class TestBaiduCreativeServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduCreativeServiceClient)

    def test_add_creative(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
            'creativeTypes':[
                {
                    'campaignId':'775709713',
                    'adgroupId':11056083632,
                    "title":'创意测试1',
                    'description1':'描述测试1',
                    'description2':'描述测试2',
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
                    'mobileFinalUrl':'https://m.jinzhuedu.org',
                    'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}'
                    },
                {
                    'campaignId':'775709713',
                    'adgroupId':11056083633,
                    "title":'创意测试1',
                    'description1':'描述测试1',
                    'description2':'描述测试2'
                 }


            ]
        }
        return self.client.add_creative(query_params)
    


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduCreativeServiceClient(uese_id,user_name)
    rsp = test_client.test_add_creative()
    print(rsp)