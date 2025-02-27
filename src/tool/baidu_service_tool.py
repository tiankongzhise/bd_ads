
class ServiceTool(object):

    def __init__(self):
        self.business_point_map = {
            '品牌':99,
            '软件开发':201904057005
        }
    @staticmethod
    def chunk_list(lst, size=100):
        """将列表按指定大小分块
        :param lst: 原始列表
        :param size: 每块大小（默认100）
        :return: 分块后的二维列表
        """
        return [lst[i:i+size] for i in range(0, len(lst), size)]
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
    def is_empty(self,value:any,empty_value:list|None = ['',[],{}]):
         
        if empty_value is None:
            if value is None:
                return True
            else:
                return False
        for empty_item in empty_value:
            if value == empty_item:
                return True
        return False

    def _set_adgroup_params(self,adgroup_item:dict,campaign_map:dict|None = None) -> dict:
        params = {}
        for key,value in adgroup_item.items():
            if key == 'campaignName':
                if campaign_map is None:
                    raise Exception('请传入计划id')
                else:
                    campaign_id = campaign_map.get(value)
                    if campaign_id is None:
                        raise Exception(f'计划{value},没有对应的campaignId')
                    params['campaignId'] = campaign_id
                    continue
                
            if key == 'adgroupName':
                params[key] = value
                continue
            
            if key == 'maxPrice':
                params[key] = value or 0.3
                continue
            
            if key == 'pcFinalUrl':
                if self.is_empty(value):
                    pass
                else:
                    params[key] = value
                continue
            if key == 'mobileFinalUrl':
                if self.is_empty(value):
                    pass
                else:
                    params[key] = value
                continue
            if key == 'pcTrackParam':
                if self.is_empty(value):
                    params[key] = 'source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}&e_bd_vid={bd_vid}'
                else:
                    params[key] = value
                continue
            if key == 'mobileTrackParam':
                if self.is_empty(value):
                    params[key] = 'source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}&e_bd_vid={bd_vid}'
                else:
                    params[key] = value
                continue
        if params.get('pcTrackParam') is None:
            params['pcTrackParam'] =  'source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}&e_bd_vid={bd_vid}'
        if params.get('mobileTrackParam') is None:
            params['mobileTrackParam'] = 'source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}&e_bd_vid={bd_vid}'
        
        if params['pcTrackParam'][0] in ['?','&']:
            params['pcTrackParam'] = params['pcTrackParam'][1:]
        if params['mobileTrackParam'][0] in ['?','&']:
            params['mobileTrackParam'] = params['mobileTrackParam'][1:]
            
        if params.get('pcFinalUrl') is None:
            if params.get('pcTrackParam'):
                del params['pcTrackParam']
        else:
            if '?' in params['pcFinalUrl']:
                params['pcTrackParam'] = '&' + params['pcTrackParam']
            else:
                params['pcTrackParam'] = '?' + params['pcTrackParam']
        if params.get('mobileFinalUrl') is None:
            if params.get('mobileTrackParam'):
                del params['mobileTrackParam']
        else:
            if '?' in params['mobileFinalUrl']:
                params['mobileTrackParam'] = '&' + params['mobileTrackParam']
            else:
                params['mobileTrackParam'] = '?' + params['mobileTrackParam']
        return params
    def create_adgroup_params(self,adgroup_item,campaign_map) -> dict:
        result = []
        adgroup_params = [self._set_adgroup_params(item,campaign_map) for item in adgroup_item]
        params_list = self.chunk_list(adgroup_params)
        return [{'adgroupTypes':params} for params in params_list]

