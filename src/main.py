from src.tool import BaiduOauthClient,ServiceTool
from src.service import BaiduCampaignServiceClient,BaiduAdgroupServiceClient,BaiduCreativeServiceClient,BaiduKeywordServiceClient

class BaiduBuildAds(object):
    def __init__(self,user_id:str,user_name:str):
        self.user_name = user_name
        self.user_id = user_id
        self.oauth_client = BaiduOauthClient(user_id)
        self.campaign_map = {'测试6': 776577181, 776577181: '测试6', '测试7': 776577180, 776577180: '测试7'}
        self.adgroup_map = {776577181: {'单元测试有url': 11060930714, 11060930714: '单元测试有url', '单元测试无url': 11060930715, 11060930715: '单元测试无url', '单元测试pcurl': 11060930718, 11060930718: '单元测试pcurl', '单元测试mourl': 11060930719, 11060930719: '单元测试mourl', '单元测试无追踪代码': 11060930716, 11060930716: '单元测试无追踪代码', '单元测试代码匹配符': 11060930717, 11060930717: '单元测试代码匹配符'}, 776577180: {'单元测试出价': 11060930720, 11060930720: '单元测试出价'}}
        self.fail = {
            '计划':[],
            '单元':[],
            '创意':[],
            '关键词':[]
        }
    
    def create_campaign(self,campaign_name:str|list[str],business_point_name:str|None = None) -> dict:
        campaign_service = self.oauth_client.create_oauth_client(self.user_name,BaiduCampaignServiceClient)
        campaign_params = ServiceTool().create_campaign_params(campaign_name,business_point_name)
        rsp = campaign_service.add_campaign(campaign_params)
        if rsp['header']['desc'] != 'success':
            for fail in rsp['header']['failures']:
                self.fail['计划'].append({'失败位置':'新建计划','失败计划名称':campaign_params['campaignTypes'][fail['id']]['campaignName'],'失败原因':fail['message']})
        if rsp['body']['data']:
            for item in rsp['body']['data']:
                self.campaign_map[item['campaignName']] = item['campaignId']
                self.campaign_map[item['campaignId']] = item['campaignName']
        print(f'\n失败记录:{self.fail}\n')
        print(f'\n计划映射表{self.campaign_map}\n')
        
    def _adgroup_fail_message(self,params,rsp_fail_msg:dict) -> dict:
        fail_index = rsp_fail_msg['id']
        param = params['adgroupTypes'][fail_index]
        return {'失败位置':'新建单元','所属计划ID':param['campaignId'],'失败单元名称':param['adgroupName'],'失败原因':rsp_fail_msg['message']}
    
    def _update_adgroup_map(self,adgroup_info:dict)->None:
        if self.adgroup_map.get(adgroup_info['campaignId']) is None:
            self.adgroup_map[adgroup_info['campaignId']] = {}
        self.adgroup_map[adgroup_info['campaignId']].update({adgroup_info['adgroupName']:adgroup_info['adgroupId']})
        self.adgroup_map[adgroup_info['campaignId']].update({adgroup_info['adgroupId']:adgroup_info['adgroupName']})
            
    def create_adgroup(self,adgroup_item:list[dict]) -> dict:
        adgroup_service = self.oauth_client.create_oauth_client(self.user_name,BaiduAdgroupServiceClient)
        adgroup_params = ServiceTool().create_adgroup_params(adgroup_item,self.campaign_map)
        for params in adgroup_params:
            rsp = adgroup_service.add_adgroup(params)
            if rsp['header']['desc'] != 'success':
                for fail_msg in rsp['header']['failures']:
                    self.fail['单元'].append(self._adgroup_fail_message(params,fail_msg))
            if rsp['body']['data']:
                for item in rsp['body']['data']:
                    self._update_adgroup_map(item)
            print(rsp)
            print(f'\n失败记录:{self.fail}\n')
            print(f'\n计划映射表{self.adgroup_map}\n')
            
            


def main():
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    build_ads = BaiduBuildAds(uese_id,user_name)
    campaign_name = ['测试6','测试7','测试3']
    business_point_name = '品牌'
    build_ads.create_campaign(campaign_name)
    adgroup_list = [
            {
                    'campaignName':'测试6',
                    "adgroupName":'单元测试有url',
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
                    'mobileFinalUrl':'https://m.jinzhuedu.org',
                    'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
            },
            {
                    'campaignName':'测试6',
                    "adgroupName":'单元测试无url',
          },
            {
                    'campaignName':'测试6',
                    "adgroupName":'单元测试pcurl',
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
                    'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
            },
            {
                    'campaignName':'测试6',
                    "adgroupName":'单元测试mourl',
                    'mobileFinalUrl':'https://www.jinzhuedu.org',
                    'pcTrackParam':'&source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
                    'mobileTrackParam':'&source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}',
            },
            {
                    'campaignName':'测试6',
                    "adgroupName":'单元测试无追踪代码',
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'mobileFinalUrl':'https://www.jinzhuedu.org',
          },
            {
                    'campaignName':'测试6',
                    "adgroupName":'单元测试代码匹配符',
                    'pcFinalUrl':'https://www.jinzhuedu.org?123',
                    'mobileFinalUrl':'https://www.jinzhuedu.org?123',
          },
            {
                    'campaignName':'测试7',
                    "adgroupName":'单元测试出价',
                    'pcFinalUrl':'https://www.jinzhuedu.org',
                    'mobileFinalUrl':'https://www.jinzhuedu.org',
                    'maxPrice':0.3
          }      
    ]
    build_ads.create_adgroup(adgroup_list)
    

if __name__ == '__main__':
    main()
