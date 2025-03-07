from math import isnan
from typing import Type,Literal
from src.service.base import BaseAPIClient
from src.db import BdAdMaterialTransferTable,BdServiceDb

class ServiceTool(object):

    def __init__(self):
        self.business_point_map = {
            '品牌':99,
            '软件开发':201904057005
        }
        self.define_pc_final_url = 'https://www.jinzhuedu.org'
        self.define_mobile_final_url = 'https://m.jinzhuedu.org'
        self.define_pc_track_param = 'source=bd-pc&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}&e_bd_vid={bd_vid}'
        self.define_mobile_track_param = 'source=bd-mo&e_userid={userid}&e_planid={planid}&e_unitid={unitid}&e_keywordid={keywordid}&e_creative={creative}&e_matchtype={matchtype}&e_dongtai={dongtai}&e_trig_flag={trig_flag}&e_crowdid={crowdid}&e_kw_enc_utf8={kw_enc_utf8}&e_bd_vid={bd_vid}'
    @staticmethod
    def chunk_list(lst, size=100):
        """将列表按指定大小分块
        :param lst: 原始列表
        :param size: 每块大小（默认100）
        :return: 分块后的二维列表
        """
        return [lst[i:i+size] for i in range(0, len(lst), size)]
    def _set_campaign_params(self,campaign_item:dict) -> dict:
            
        params = {
                "pause":True,
                'marketingTargetId':0,
                'campaignBidType':1,
                'campaignOcpcBidType':1,
                'campaignOcpcBid':50,
                'campaignTransTypes':[3,18,30,79],
                'campaignDeepTransTypes':[75]
        }
        campaign_name = campaign_item.get('campaignName')
        if campaign_name is None:
            raise Exception('请传入计划名称')
        params['campaignName'] = campaign_name

        business_point_name = campaign_item.get('businessPointName')
        if business_point_name is None:
                business_point_name = '软件开发'
        business_point_id = self.business_point_map.get(business_point_name)
        if business_point_id is None:
            raise Exception(f'没有对应的businessPointId,请检查{business_point_name}是否正确')
        params['businessPointId'] = business_point_id
        return params
         
    def create_campaign_params(self,campaign_item:dict) -> dict:
        campaign_params = [self._set_campaign_params(item) for item in campaign_item]
        params_list = self.chunk_list(campaign_params)
        return [{'campaignTypes':params} for params in params_list]
    def is_empty(self,value:any,empty_value:list|None = ['',[],{}]):
        if value is None:
            return True
        
        try:
            if isinstance(value,float) and isnan(value):
                return True
        except:  # noqa: E722
            pass


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
                    params[key] = self.define_pc_track_param
                else:
                    params[key] = value
                continue
            if key == 'mobileTrackParam':
                if self.is_empty(value):
                    params[key] = self.define_mobile_track_param
                else:
                    params[key] = value
                continue
        if params.get('pcTrackParam') is None:
            params['pcTrackParam'] = self.define_pc_track_param
        if params.get('mobileTrackParam') is None:
            params['mobileTrackParam'] = self.define_mobile_track_param

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
        adgroup_params = [self._set_adgroup_params(item,campaign_map) for item in adgroup_item]
        params_list = self.chunk_list(adgroup_params)
        return [{'adgroupTypes':params} for params in params_list]
    
    def _get_campaign_id(self,campaign_name:str,campaign_map:dict)->int:
        if campaign_map is None:
            raise Exception('请传入计划id')
        else:
            campaign_id = campaign_map.get(campaign_name)
            if campaign_id is None:
                raise Exception(f'计划{campaign_name},没有对应的campaignId')
            return int(campaign_id)
    def _get_adgroup_id(self,adgroup_name:str,campaign_target:str|int,campaign_map:dict,adgroup_map:dict)->int:
        if adgroup_map is None:
            raise Exception('请传入广告组id')
        if isinstance(campaign_target,str):
            campaign_id = self._get_campaign_id(campaign_target,campaign_map)
        if isinstance(campaign_target,int):
            campaign_id = campaign_target
        adgroup_id = adgroup_map.get(campaign_id).get(adgroup_name)
        if adgroup_id is None:
            raise Exception(f'广告组{adgroup_name},没有对应的adgroupId')
        return int(adgroup_id)

    def _set_tabs(self,tabs:list[str])->str:
        ...
    def _set_keyword_params(self,keyword_item:dict,adgroup_map:dict,campaign_map:dict) -> dict:
        params = {}
        # 获取计划id
        campaign_id = keyword_item.get('campaignId')
        campaign_name = keyword_item.get('campaignName')
        if campaign_id is None:
            if campaign_name is None:
                raise Exception('请传入计划id或者计划名称')
            campaign_id = self._get_campaign_id(campaign_name,campaign_map)
        campaign_id = int(campaign_id)

        # 设置广告组id
        adgroup_id = keyword_item.get('adgroupId')
        adgroup_name = keyword_item.get('adgroupName')
        if adgroup_id is None:
            if adgroup_name is None:
                raise Exception('请传入广告组id或者广告组名称')
            adgroup_id = self._get_adgroup_id(adgroup_name,campaign_id,campaign_map,adgroup_map)
        params['adgroupId'] = int(adgroup_id)

        # 设置关键词
        keyword = keyword_item.get('keyword')
        if keyword is None:
            raise Exception('请传入关键词')
        params['keyword'] = keyword

        # 设置匹配方式
        match_target = keyword_item.get('matchTarget')
        if match_target is None:
            params['matchType'] = 2
            params['phraseType'] = 1
        elif match_target in ['精确匹配','精确']:
            params['matchType'] = 1
            params['phraseType'] = 1
        elif match_target in ['短语匹配','短语']:
            params['matchType'] = 2
            params['phraseType'] = 1
        elif match_target in ['广泛匹配','广泛']:
            params['matchType'] = 2
            params['phraseType'] = 3
        elif match_target in ['智能匹配','智能']:
            params['matchType'] = 2
            params['phraseType'] = 3
        
        price = keyword_item.get('price')
        if price:
            params['price'] = price

        pc_destination_url = keyword_item.get('pcDestinationUrl')
        if not self.is_empty(pc_destination_url):
            params['pcFinalUrl'] = pc_destination_url
        
        mobile_destination_url = keyword_item.get('mobileDestinationUrl')
        if not self.is_empty(mobile_destination_url):
            params['mobileFinalUrl'] = mobile_destination_url
        
        tabs = keyword_item.get('tabs')
        if tabs:
            params['tabs'] = self._set_tabs(tabs)
        
        deeplink = keyword_item.get('deeplink')
        if deeplink:
            params['deeplink'] = deeplink
        
        mini_program_url = keyword_item.get('miniProgramUrl')
        if mini_program_url:
            params['miniProgramUrl'] = mini_program_url
        
        pc_final_url = keyword_item.get('pcFinalUrl')
        if pc_final_url:
            params['pcFinalUrl'] = pc_final_url
        
        pc_track_param = keyword_item.get('pcTrackParam')
        if pc_track_param is None:
            pc_track_param = self.define_pc_track_param
        elif pc_track_param[0] in ['?','&']:
            pc_track_param = pc_track_param[1:]
        if pc_final_url:
            if '?' in pc_final_url:
                params['pcTrackParam'] = '&' + pc_track_param
            else:
                params['pcTrackParam'] = '?' + pc_track_param
        
        mobile_final_url = keyword_item.get('mobileFinalUrl')
        if mobile_final_url:
            params['mobileFinalUrl'] = mobile_final_url
        
        mobile_track_param = keyword_item.get('mobileTrackParam')
        if mobile_track_param is None:
            mobile_track_param = self.define_mobile_track_param
        elif mobile_track_param[0] in ['?','&']:
            mobile_track_param = mobile_track_param[1:]
        if mobile_final_url:
            if '?' in mobile_final_url:
                params['mobileTrackParam'] = '&' + mobile_track_param
            else:
                params['mobileTrackParam'] = '?' + mobile_track_param
        
        return params


    def create_keyword_params(self,keyword_item:list[dict],adgroup_map:dict,campaign_map:dict) -> dict:
        keyword_params = [self._set_keyword_params(item,adgroup_map,campaign_map) for item in keyword_item]
        params_list = self.chunk_list(keyword_params,size=10000)
        return [{'keywordTypes':params} for params in params_list]
    



    def _set_creative_tabs(self,tabs:list[str]):
        ...
    def _set_creative_params(self,creative_item:dict,adgroup_map:dict,campaign_map:dict) -> dict:
        params = {}
        # 获取计划id
        campaign_id = creative_item.get('campaignId')
        campaign_name = creative_item.get('campaignName')
        if campaign_id is None:
            if campaign_name is None:
                raise Exception('请传入计划id或者计划名称')
            campaign_id = self._get_campaign_id(campaign_name,campaign_map)
        campaign_id = int(campaign_id)
        params['campaignId'] = int(campaign_id)

        # 设置广告组id
        adgroup_id = creative_item.get('adgroupId')
        adgroup_name = creative_item.get('adgroupName')
        if adgroup_id is None:
            if adgroup_name is None:
                raise Exception('请传入广告组id或者广告组名称')
            adgroup_id = self._get_adgroup_id(adgroup_name,campaign_id,campaign_map,adgroup_map)
        params['adgroupId'] = int(adgroup_id)

        # 设置创意
        creative_title = creative_item.get('title')
        if creative_title is None:
            raise Exception('请传入创意标题')
        params['title'] = creative_title
        creative_description1 = creative_item.get('description1')
        if creative_description1 is None:
            raise Exception('请传入创意描述1')
        params['description1'] = creative_description1
        creative_description2 = creative_item.get('description2')
        if creative_description2:
            params['description2'] = creative_description2
        
        # 设置标签
        creative_label = creative_item.get('tabs')
        if creative_label:
            params['tabs'] = self._set_creative_tabs(creative_label)
        
        deeplink = creative_item.get('deeplink')
        if deeplink:
            params['deeplink'] = deeplink
        
        ulink = creative_item.get('ulink')
        if ulink:
            params['ulink'] = ulink
        
        mini_program_url = creative_item.get('miniProgramUrl')
        if mini_program_url:
            params['miniProgramUrl'] = mini_program_url
        
        pc_final_url = creative_item.get('pcFinalUrl')
        if self.is_empty(pc_final_url):
            pc_final_url = self.define_pc_final_url
        params['pcFinalUrl'] = pc_final_url
        
        pc_track_param = creative_item.get('pcTrackParam')
        if pc_track_param is None:
            pc_track_param = self.define_pc_track_param
        elif pc_track_param[0] in ['?','&']:
            pc_track_param = pc_track_param[1:]
        if pc_final_url:
            if '?' in pc_final_url:
                params['pcTrackParam'] = '&' + pc_track_param
            else:
                params['pcTrackParam'] = '?' + pc_track_param
        
        mobile_final_url = creative_item.get('mobileFinalUrl')
        if self.is_empty(mobile_final_url):
            mobile_final_url = self.define_mobile_final_url
        params['mobileFinalUrl'] = mobile_final_url
        
        mobile_track_param = creative_item.get('mobileTrackParam')
        if mobile_track_param is None:
            mobile_track_param = self.define_mobile_track_param
        elif mobile_track_param[0] in ['?','&']:
            mobile_track_param = mobile_track_param[1:]
        if mobile_final_url:
            if '?' in mobile_final_url:
                params['mobileTrackParam'] = '&' + mobile_track_param
            else:
                params['mobileTrackParam'] = '?' + mobile_track_param
        return params



    def create_creative_params(self,creative_item:list[dict],adgroup_map:dict,campaign_map:dict) -> dict:
        creative_params = [self._set_creative_params(item,adgroup_map,campaign_map) for item in creative_item]
        params_list = self.chunk_list(creative_params,size=3000)
        return [{'creativeTypes':params} for params in params_list]
    
    @staticmethod
    def update_center_info(center_id:str) -> dict:
        from src.service import BaiduMccServiceClient
        from src.db import BdAdCenterBindTable,BdServiceDb
        from .baidu_oauth_tool import BaiduOauthClient
        oauth_client = BaiduOauthClient(center_id)
        mcc_client = oauth_client.create_oauth_client('BDCC-金蛛账号中心',BaiduMccServiceClient)
        queryParam = {
            'mccId':center_id
        }
        rsp = mcc_client.get_user_list(queryParam)
        if rsp['header']['desc'] != 'success':
            raise Exception(f'获取账户中心信息失败:{rsp}')
        user_list = rsp['body']['data']
        
        result = []
        db = BdServiceDb()
        with db.get_session() as session:
            try:
                db_user_info = session.query(BdAdCenterBindTable).filter(BdAdCenterBindTable.center_id == center_id).all()
            except Exception as e:
                raise f'更新账户中心信息失败，原因是无法从数据库获取历史中心数据，数据库报错:{e}'
        temp_list = []
        for temp in db_user_info:
            temp_list.append(int(temp.user_id))
            
        print(f'temp_list:{temp_list}')
        
        for user_info in user_list:
            if user_info['userid'] in temp_list:
                continue
            result.append({
                'center_id':user_info['mccid'],
                'center_name':user_info['fatname'],
                'user_id':user_info['userid'],
                'user_name':user_info['username'],
            })

        with db.get_session() as session:
            try:
                session.bulk_insert_mappings(BdAdCenterBindTable,result)
                session.commit()
                print(f'更新{center_id}账户中心信息成功')
            except Exception as e:
                session.rollback()
                print(f'更新账户中心信息失败:{e}')
                raise e
    @staticmethod        
    def get_user_info(mcc_id:str) -> dict:
        from src.db import BdAdCenterBindTable,BdServiceDb
        db = BdServiceDb()
        with db.get_session() as session:
            rsp = session.query(BdAdCenterBindTable).filter(BdAdCenterBindTable.center_id == mcc_id).all()
            result = {mcc_id:{}}
            for item in rsp:
                result[mcc_id].update({
                    item.user_id:item.user_name,
                    item.user_name:item.user_id
                })
            
        return result
    @staticmethod   
    def get_user_list(mcc_id:str) -> list:
        '''返回账户管理中心所管理的全部账户名称'''
        from src.db import BdAdCenterBindTable,BdServiceDb
        db = BdServiceDb()
        with db.get_session() as session:
            rsp = session.query(BdAdCenterBindTable).filter(BdAdCenterBindTable.center_id == mcc_id).all()
            result = [item.user_name for item in rsp]
            return result
        
    
    @staticmethod
    def get_category_list(client:Type[BaseAPIClient],type_class:Literal['产品','文章','问答','人员','案例'],type_map:dict):
        queryParam = {
            'type':type_map[type_class],
            'pageSize':500,
            'pageNum':1
        }
        rsp = client.get_category_list(queryParam)
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
    @staticmethod
    def get_migration_map(migrate_type:str,db_client:BdServiceDb|None = None)->dict:
        result = {}
        if db_client is None:
            client = BdServiceDb()
        with client.get_session() as session:
            rsp = session.query(BdAdMaterialTransferTable).filter(BdAdMaterialTransferTable.material_class == migrate_type).all()
        for item in rsp:
            if item.migrate_status == '成功':
                if result.get(item.material_id) is None:
                    result.update({
                        item.material_id:{item.target_user_id:item.target_material_id}
                    })
                else:
                    result[item.material_id].update({
                            item.target_user_id:item.target_material_id
                        })
        return result

