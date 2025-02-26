from src.tool import BaiduOauthClient,ServiceTool
from src.service import BaiduCampaignServiceClient

class BaiduBuildAds(object):
    def __init__(self,user_id:str,user_name:str):
        self.user_name = user_name
        self.user_id = user_id
        self.oauth_client = BaiduOauthClient(user_id)
        self.campaign_map = {}
        self.adgroup_map = {}
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


def main():
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    build_ads = BaiduBuildAds(uese_id,user_name)
    campaign_name = ['测试2','测试5','测试3']
    business_point_name = '品牌'
    build_ads.create_campaign(campaign_name,business_point_name)

if __name__ == '__main__':
    main()