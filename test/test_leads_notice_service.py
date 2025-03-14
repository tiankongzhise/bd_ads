from src.service import BaiduLeadsNoticeServiceClient
from src.tool import BaiduOauthClient




class TestBaiduLeadsNoticeServiceClient(object):
    def __init__(self,center_id:str):
        self.center_id = center_id
        self.oauth_client = BaiduOauthClient(user_id=center_id)
    
    
    def test_get_notice_list(self,user_name:str,startDate:str,endDate:str):
        
        leads_notice_service = self.oauth_client.create_oauth_client(user_name,BaiduLeadsNoticeServiceClient)
        get_notice_list_common_params = {"startDate":startDate,"endDate":endDate}
        solutionType_list = ['consult']
        get_notice_list_common_params['solutionType'] = solutionType_list[0]
        rsp = leads_notice_service.get_notice_list(get_notice_list_common_params)
        print(f'{user_name}账号的{solutionType_list[0]},返回结果为{rsp}')





if __name__ == '__main__':
    center_id = '64339991'
    user_name = '金蛛-北大青鸟'
    start_date = '2025-02-20 00:00:00'
    end_date = '2025-03-14 23:59:59'

    test_client = TestBaiduLeadsNoticeServiceClient(center_id)
    test_client.test_get_notice_list(user_name,start_date,end_date)
