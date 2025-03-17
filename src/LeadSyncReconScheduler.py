from src.service import BaiduLeadsNoticeServiceClient
from src.tool import BaiduOauthClient
from src.db.datebase import get_db
from src.db.models import LeadsNoticePush

class LeadSyncReconScheduler(object):
    def __init__(self,center_id:str,user_name:str):
        self.user_name = user_name
        self.center_id = center_id
    
    def get_db_leads_data(self):
        result = []
        with get_db() as db:
            db_data = db.query(LeadsNoticePush).all()
        
        for item in db_data:
            result.append(item.clueId)
        return result
            
    
    def get_bd_leads_data(self,start_date:str,end_date:str) -> list:
        bd_leads_client = UserLeadsNoticeClient(center_id,user_name)
        bd_leads_data,rsp = bd_leads_client.get_notice_list(start_date,end_date)
        print(rsp)
        return bd_leads_data
    
    def compare_clue_id(self,db_data:list,bd_data:list):
        result = []
        for item in bd_data:
            if item['clueId'] not in db_data:
                result.append(item)
        return result
    def _return_msg(self,code:int,msg:str,data:list|dict|None = None):
        return {'code':code,'msg':msg,'data':data}
    def recon_leads_data(self,data:list):
        insert_cluid = []
        try:
            with get_db() as db:
                for item in data:
                    if item['cluePhoneNumber'] == '18566120258' or item['cluePhoneNumber'] == '18566184256':
                        print(f'{item['clueId']}为测试数据cluePhoneNumber:{item['cluePhoneNumber']}，跳过')
                        continue
                    db.add(LeadsNoticePush(**item))
                    insert_cluid.append(item['clueId'])
                db.commit()
            return self._return_msg(code=0,msg='success',data=insert_cluid)
        except Exception as e:
            return self._return_msg(code=1,msg=str(e))
    
    def run(self, start_date:str, end_date:str)->list:
        db_leads_data = self.get_db_leads_data()
        bd_leads_data = self.get_bd_leads_data(start_date,end_date)
        diff_data = self.compare_clue_id(db_leads_data,bd_leads_data)
        print(f'diff_data:{diff_data}')
        result = self.recon_leads_data(diff_data)
        return result
        


class UserLeadsNoticeClient(object):
    def __init__(self,center_id:str,user_name:str):
        self.center_id = center_id
        self.oauth_client = BaiduOauthClient(user_id=center_id)
        self.leads_notice_service = None
        self.user_name = user_name
    
    def login(self,user_name:str):
        self.user_name = user_name
        self.leads_notice_service = self.oauth_client.create_oauth_client(user_name,BaiduLeadsNoticeServiceClient)
    
    def _return_msg(self,code:int,msg:str,data:list|dict|None = None):
        return {'code':code,'msg':msg,'data':data}
    
    def _solution_type_map(self,solution_type:str|None):
        if solution_type is None:
            raise ValueError('solution_type不能为None')
        map_dict = {
            'consult':'咨询',
            'phone':'电话',
            'form':'表单',
            'wechat':'微信'
        }
        return map_dict[solution_type]
    def format_leads_notice_data(self,data:list):
        result = []
        for item in data:
            temp_dict = {}
            if item.get('cluePhoneNumber','') == '' and  item.get('wechatAccount','') == '':
                # 如果电话号码和微信账号都为空，则跳过该条数据
                continue
            temp_dict['ucid'] = item.get('userId')
            temp_dict['clueId'] = item.get('clueId')
            temp_dict['commitTime'] = item.get('commitTime')
            temp_dict['solutionTypeName'] = self._solution_type_map(item.get('solutionType'))#需要转换
            temp_dict['cluePhoneNumber'] = item.get('cluePhoneNumber')
            temp_dict['flowChannelName'] = item.get('flowChannelName')
            temp_dict['formDetail'] = item.get('formDetail','')
            temp_dict['imName'] = item.get('imName')
            temp_dict['clueUserMsgCount'] = item.get('clueUserMsgCount',-1)
            temp_dict['humanServiceMsgCount'] = item.get('humanServiceMsgCount',-1)
            temp_dict['aiServiceMessageNum'] = item.get('aiServiceMessageNum',-1)
            temp_dict['ip'] = item.get('ip','0.0.0.0'),
            temp_dict['wechatAccount'] = item.get('wechatAccount')
            temp_dict['url'] = item.get('url')
            temp_dict['consultUrl'] = item.get('consultUrl')
            result.append(temp_dict)
        return result
            
            
        
    def _get_notice_list(self,startDate:str,endDate:str,solutionType:str):
        get_notice_list_params = {"startDate":startDate,"endDate":endDate,'solutionType':solutionType}
        rsp = self.leads_notice_service.get_notice_list(get_notice_list_params)
        if rsp['header']['desc'] != 'success':
            msg = f'账号:{self.user_name},获取{solutionType}线索列表失败，原因为{rsp}'
            print(msg)
            return self._return_msg(code=1,msg=msg)
        
        return self._return_msg(code=0,msg='success',data=self.format_leads_notice_data(rsp['body']['data'][0]['noticeDetailList']))
    
    def get_notice_list(self,startDate:str,endDate:str):
        if self.leads_notice_service is None:
            self.login(self.user_name)
        
        data = []
        result = {
            'success_count':0,
            'fail_count':0,
            'success_data':0,
            'success':[],
            'fail':[],

        }
        
        solutionType_list = ['consult','phone','form','wechat']
        for solutionType in solutionType_list:
            rsp = self._get_notice_list(
                startDate= startDate,
                endDate = endDate,
                solutionType = solutionType
            )
            if rsp['code'] == 0:
                data.extend(rsp['data'])
                result['success'].append({'账户':self.user_name,'solutionType':solutionType})
                result['success_count'] += 1
            else:
                result['fail'].append({'账户':self.user_name,'solutionType':solutionType})
                result['fail_count'] += 1
        result['success_data'] = len(data)
        print(f'{self.user_name}账号的获取结果{result}')
        return data,result





if __name__ == '__main__':
    center_id = '64339991'
    user_name = '金蛛-新账户1'
    start_date = '2025-03-15 00:00:00'
    end_date = '2025-03-17 23:59:59'

    # user_leads_notice_client = UserLeadsNoticeClient(center_id,user_name)
    # user_leads_notice_client.login('金蛛-新账户1')
    # data,rsp = user_leads_notice_client.get_notice_list(start_date,end_date)
    result = LeadSyncReconScheduler(center_id,user_name).run(start_date,end_date)
    print(result)
