
class ServiceTool(object):

    def __init__(self):
        self.business_point_map = {
            '品牌':99,
            '软件开发':201904057005
        }
    def _campaign_params(self,campaign_name:str,business_point_name:str|None) -> dict:
            if business_point_name is None:
                  business_point_name = '软件开发'
            params = {
                    "campaignName":campaign_name,
                    "pause":True,
                    'marketingTargetId':0,
                    'businessPointId':self.business_point_map[business_point_name],
                    'campaignBidType':1,
                    'campaignOcpcBidType':1,
                    'campaignOcpcBid':50,
                    'campaignTransTypes':[3,18,30,79],
                    'campaignDeepTransTypes':[75]
            }
            return params
         
    def create_campaign_params(self,campaign_name:str,business_point_name:str|None) -> dict:

            if isinstance(campaign_name,str):
                campaign_params = [self._campaign_params(campaign_name,business_point_name)]

            if isinstance(campaign_name,list):
                campaign_params = [self._campaign_params(item,business_point_name) for item in campaign_name]
            
            return {'campaignTypes':campaign_params}

