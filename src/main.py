from src.tool import BaiduOauthClient,ServiceTool
from src.service import BaiduCampaignServiceClient,BaiduAdgroupServiceClient,BaiduCreativeServiceClient,BaiduKeywordServiceClient
from src.tool import UserSetting

def define_adgroup_params():
     params = [
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
     return params

def define_keyword_params():
    params = [
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'keyword':'精确匹配关键词',
            'matchTarget':'精确'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试pcurl',
            'keyword':'短语匹配关键词',
            'matchTarget':'短语匹配'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试代码匹配符',
            'keyword':'广泛匹配关键词',
            'matchTarget':'广泛'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试无追踪代码',
            'keyword':'智能匹配关键词',
            'matchTarget':'智能'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试有url',
            'keyword':'出价加默认匹配方式',
            'price':0.3
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试无url',
            'keyword':'测试所有层级均无URL',
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试无url',
            'keyword':'测试关键词URL',
            'pcFinalUrl':'https://www.jinzhuedu.org',
            'mobileFinalUrl':'https://m.jinzhuedu.org',
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试有url',
            'keyword':'测试关键词默认追踪参数',
            'pcFinalUrl':'https://www.jinzhuedu.org?123',
            'mobileFinalUrl':'https://m.jinzhuedu.org?123',
            'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}',
            'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}'
        }

    ]
    return params

def define_creative_params():
    params = [
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'title':'完整创意,111111111',
            'description1':'描述1,描述1,描述1,描述1,描述1,描述1,',
            'description2':'描述2',
            'pcFinalUrl':'https://www.jinzhuedu.org',
            'mobileFinalUrl':'https://m.jinzhuedu.org',
            'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}',
            'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'title':'无URL创意,111111',
            'description1':'描述1,描述1,描述1,描述1,描述1,描述1,描述1,',
            'description2':'描述2',
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'title':'无追踪代码创意,111111',
            'description1':'描述1,描述1,描述1,描述1,描述1,描述1,描述1,',
            'description2':'描述2',
            'pcFinalUrl':'https://www.jinzhuedu.org',
            'mobileFinalUrl':'https://m.jinzhuedu.org',
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'title':'只有追踪代码创意',
            'description1':'描述1,描述1,描述1,描述1,描述1,描述1,描述1,',
            'description2':'描述2',
            'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}',
            'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'title':'测试创意有追踪代码自动替换标识符',
            'description1':'描述1,描述1,描述1,描述1,描述1,描述1,描述1,',
            'description2':'描述2',
            'pcFinalUrl':'https://www.jinzhuedu.org?123',
            'mobileFinalUrl':'https://m.jinzhuedu.org?123',
            'pcTrackParam':'?source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}',
            'mobileTrackParam':'?source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}'
        },
        {
            'campaignName':'测试6',
            'adgroupName':'单元测试mourl',
            'title':'测试创意默认追踪参数替换标识符',
            'description1':'描述1,描述1,描述1,描述1,描述1,描述1,描述1,',
            'description2':'描述2',
            'pcFinalUrl':'https://www.jinzhuedu.org',
            'mobileFinalUrl':'https://m.jinzhuedu.org',
        }
    ]
    return params


class BaiduBuildAds(object):
    def __init__(self,user_id:str,user_name:str):
        self.user_name = user_name
        self.user_id = user_id
        self.oauth_client = BaiduOauthClient(user_id)
        self.campaign_map = {}
        self.adgroup_map = {}
        self.keyword_success = []
        self.creative_success = []
        self.creative_group_success = []
        self.fail = {
            '计划':[],
            '单元':[],
            '创意':[],
            '关键词':[],
            '创意':[],
            '高级样式':[]
        }
    
    def create_campaign(self,campaign_item:list[dict]) -> dict:
        campaign_service = self.oauth_client.create_oauth_client(self.user_name,BaiduCampaignServiceClient)
        campaign_params = ServiceTool().create_campaign_params(campaign_item)
        for params in campaign_params:
            rsp = campaign_service.add_campaign(params)
            if rsp['header']['desc'] != 'success':
                for fail in rsp['header']['failures']:
                    self.fail['计划'].append({'失败位置':'新建计划','失败计划名称':campaign_params['campaignTypes'][fail['id']]['campaignName'],'失败原因':fail['message']})
            if rsp['body']['data']:
                for item in rsp['body']['data']:
                    self.campaign_map[item['campaignName']] = item['campaignId']
                    self.campaign_map[item['campaignId']] = item['campaignName']
        
    def _adgroup_fail_message(self,params,rsp_fail_msg:dict) -> dict:
        fail_index = rsp_fail_msg['id']
        param = params['adgroupTypes'][fail_index]
        return {'失败位置':'新建单元','所属计划ID':param['campaignId'],'失败单元名称':param['adgroupName'],'失败原因':rsp_fail_msg['message']}
    def _keyword_fail_message(self,params,rsp_fail_msg:dict) -> dict:
        fail_index = rsp_fail_msg['id']
        param = params['keywordTypes'][fail_index]
        return {'失败位置':'新建关键词','所属单元ID':param['adgroupId'],'失败关键词名称':param['keyword'],'失败原因':rsp_fail_msg['message']}
    
    def _creative_fail_message(self,params,rsp_fail_msg:dict) -> dict:
        fail_index = rsp_fail_msg['id']
        param = params['creativeTypes'][fail_index]
        return {'失败位置':'新建创意','所属单元ID':param['adgroupId'],'失败创意标题':param['title'],'失败创意描述1':param['description1'],'失败创意描述2':param['description2'],'失败原因':rsp_fail_msg['message']}

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
    def _upadte_keyword_success(self,keyword_info_list:dict)->None:
        firsr_keyword_info = keyword_info_list[0]
        last_keyword_info = keyword_info_list[-1]
        first_keyword_info_str = f'计划ID:{firsr_keyword_info["campaignId"]},单元ID:{firsr_keyword_info["adgroupId"]},关键词:{firsr_keyword_info["keyword"]}'
        last_keyword_info_str = f'计划ID:{last_keyword_info["campaignId"]},单元ID:{last_keyword_info["adgroupId"]},关键词:{last_keyword_info["keyword"]}'
        self.keyword_success.append(f'{first_keyword_info_str}->->->{last_keyword_info_str}创建成功')
        
    def create_keyword(self,keyword_item:list[dict]) -> dict:
        keyword_service = self.oauth_client.create_oauth_client(self.user_name,BaiduKeywordServiceClient)
        keyword_params = ServiceTool().create_keyword_params(keyword_item,self.adgroup_map,self.campaign_map)
        for params in keyword_params:
            rsp = keyword_service.add_keyword(params)
            for fail_msg in rsp['header']['failures']:
                self.fail['关键词'].append(self._keyword_fail_message(params,fail_msg))
            if rsp['body']['data']:
                self._upadte_keyword_success(rsp['body']['data'])
    def _update_creative_success(self,creative_info_list:dict)->None:
        firsr_creative_info = creative_info_list[0]
        last_creative_info = creative_info_list[-1]
        first_creative_info_str = f'计划ID:{firsr_creative_info["campaignId"]},单元ID:{firsr_creative_info["adgroupId"]},创意标题:{firsr_creative_info["title"]},创意描述1:{firsr_creative_info["description1"]},创意描述2:{firsr_creative_info.get("description2")}'
        last_creative_info_str = f'计划ID:{last_creative_info["campaignId"]},单元ID:{last_creative_info["adgroupId"]},创意标题:{last_creative_info["title"]},创意描述1:{last_creative_info["description1"]},创意描述2:{last_creative_info.get("description2")}'
        self.creative_success.append(f'{first_creative_info_str}->->->{last_creative_info_str}创建成功')
    def create_creative(self,creative_item:list[dict]) -> dict:
        creative_service = self.oauth_client.create_oauth_client(self.user_name,BaiduCreativeServiceClient)
        creative_params = ServiceTool().create_creative_params(creative_item,self.adgroup_map,self.campaign_map)
        for params in creative_params:
            rsp = creative_service.add_creative(params)
            for fail_msg in rsp['header']['failures']:
                self.fail['创意'].append(self._creative_fail_message(params,fail_msg))
            if rsp['body']['data']:
                self._update_creative_success(rsp['body']['data'])
    def print_result_message(self):
        print('创建结果如下：')
        print(f'计划映射: {self.campaign_map}')
        print(f'单元映射: {self.adgroup_map}')
        print(f'关键词成功创建: {self.keyword_success}')
        print(f'创意成功创建: {self.creative_success}')
        print(f'失败信息: {self.fail}')
            


def test():
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    build_ads = BaiduBuildAds(uese_id,user_name)
    campaign_name = ['测试6','测试7','测试3']
    business_point_name = '品牌'
    build_ads.create_campaign(campaign_name)
    adgroup_list = define_adgroup_params()
    build_ads.create_adgroup(adgroup_list)
    keyword_list = define_keyword_params()
    build_ads.create_keyword(keyword_list)
    creative_list = define_creative_params()
    build_ads.create_creative(creative_list)
    build_ads.print_result_message()

def main():
    user_setting = UserSetting()
    user_setting_file_list = user_setting.get_user_setting_file_list()
    user_id = '64339991'
    for user_setting_file in user_setting_file_list:
        user_name = user_setting.get_user_name(user_setting_file)
        build_ads = BaiduBuildAds(user_id,user_name)
        campaign_setting = user_setting.get_campaign_setting(user_setting_file)
        build_ads.create_campaign(campaign_setting)
        adgroup_setting = user_setting.get_adgroup_setting(user_setting_file)
        build_ads.create_adgroup(adgroup_setting)
        keyword_setting = user_setting.get_keyword_setting(user_setting_file)
        build_ads.create_keyword(keyword_setting)
        creative_setting = user_setting.get_creative_setting(user_setting_file)
        build_ads.create_creative(creative_setting)
        build_ads.print_result_message()
if __name__ == '__main__':
    main()
