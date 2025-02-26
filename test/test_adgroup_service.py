from src.tool import BaiduOauthClient
from src.service import BaiduAdgroupServiceClient

class TestBaiduAdgroupServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduAdgroupServiceClient)

    def test_add_adgroup(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
            'adgroupTypes':[
                {
                    'campaignId':775709713,
                    "adgroupName":'单元测试',
                    'maxPrice':0.3,
                    "pause":True,
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
                    'mobileFinalUrl':'https://m.jinzhuedu.org',
                    'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
            },
            {
                    'campaignId':775709713,
                    "adgroupName":'单元测试1',
                    'maxPrice':0.3,
                    "pause":True,
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
                    'mobileFinalUrl':'https://m.jinzhuedu.org',
                    'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
            }
            ]
        }
        return self.client.add_adgroup(query_params)
    
    def test_get_adgroup(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                'adgroupFields':[
                    'adgroupId',
                    'campaignId',
                    'adgroupName'
                ],
                'ids':[775709713],
                'idType':3
            }
        return self.client.get_adgroup(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduAdgroupServiceClient(uese_id,user_name)
    rsp = test_client.test_add_adgroup()
    print(rsp)