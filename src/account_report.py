from src.service import BaiduOpenApiReportServiceClient
from src.tool import BaiduOauthClient
from src.db.datebase import get_db,engine
from src.db.models import BaiduAccoutCostRrport,Base



class BaiduAccountReportClient(object):
    def __init__(self, center_id: str, user_name:str,**kwargs):
        oauth_client = BaiduOauthClient(user_id=center_id)
        self.auth_client = oauth_client.create_oauth_client(user_name,BaiduOpenApiReportServiceClient)
        self.user_name = user_name
    def _return_msg(self,code:int,msg:str,data:list|dict|None = None):
        return {'code':code,'msg':msg,'data':data}
    def get_account_cost_report(self,start_date:str,end_date:str):
        try:
            query_params = {
                'reportType':1783967,
                'timeUnit':'DAY',
                "startDate": start_date,
                "endDate": end_date,
                "columns": [
                    "date",
                    'userName',
                    'userId',
                    "product",
                    "impression",
                    "click",
                    "cost"
                ],
                'startRow':0,
                'rowCount':999
        }
            rsp = self.auth_client.get_report_data(query_params)
            try:
                if rsp['header']['desc'] == 'success':
                    data = rsp['body']['data'][0]['rows']
                    print(f'获取百度{self.user_name}账户，{start_date}到{end_date}的账户报表数据成功')
                    with get_db() as session:
                        session.bulk_insert_mappings(BaiduAccoutCostRrport,data)
                        session.commit()
                    print(f'百度{self.user_name}账户，{start_date}到{end_date}的账户报表数据数据库写入成功')
                    return self._return_msg(code=0,msg='success',data=data)
                else:
                    return self._return_msg(code=1,msg=f"获取百度{self.user_name}账户，{start_date}到{end_date}的账户报表数据失败，原因为{rsp}")
            except Exception as e:
                session.rollback()
                raise f'BaiduAccountReportClient.get_account_cost_report写入数据失败，原因为{e}'
        except Exception as e:
            raise f'BaiduAccountReportClient.get_account_cost_report获取数据失败，原因为{e}'
            



if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        raise f'BaiduAccountReportClient.get_account_cost_report创建数据库失败，原因为{e}'
    center_id = '64339991'
    user_name_list = ['金蛛-新账户1','金蛛-北大青鸟','金蛛-BCSP','金蛛-新账户5']
    start_date = '2025-02-20'
    end_date = '2025-03-16'
    for user_name in user_name_list:
        client = BaiduAccountReportClient(center_id=center_id,user_name=user_name)
        client.get_account_cost_report(start_date=start_date,end_date=end_date)

