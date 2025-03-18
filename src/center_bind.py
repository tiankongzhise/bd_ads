from tkzs_bd_db_tool import get_session
from tkzs_bd_db_tool import models
from src.tool.baidu_oauth_tool import BaiduOauthClient
from src.service.mcc_service import BaiduMccServiceClient


def get_db_bind_userid(center_id:str)->list:
    with get_session() as session:
        bind_list = session.query(models.BdAdCenterBindTable.user_id).filter(models.BdAdCenterBindTable.center_id == center_id).all()
        bind_list = [bind[0] for bind in bind_list]
    return bind_list

def get_bd_center_bind_user(center_id:str):
    oauth_client = BaiduOauthClient(center_id)
    baidu_center_client = oauth_client.create_oauth_client('金蛛教育',BaiduMccServiceClient)
    query_params = {
        'mccId':center_id
    }
    rsp = baidu_center_client.get_user_list(query_params)
    result = []
    if rsp['header']['desc'] == 'success':
        for user_info in rsp['body']['data']:
            temp_dict = {}
            temp_dict['user_id'] = str(user_info['userid'])
            temp_dict['user_name'] = user_info['username']
            temp_dict['center_id'] = str(user_info['mccid'])
            temp_dict['center_name'] = user_info['fatname']
            result.append(temp_dict)
        return result
    else:
        raise Exception(f'获取用户信息失败，原因为{rsp}')

def new_bind_user(center_id:str)->list:
    db_bind_userid = get_db_bind_userid(center_id)
    db_center_bind_user = get_bd_center_bind_user(center_id)
    new_bind_user = [user for user in db_center_bind_user if user['user_id'] not in db_bind_userid]
    return new_bind_user

def add_new_bind_user(center_id:str)->dict:
    new_bind_user_list = new_bind_user(center_id)
    try:
        with get_session() as session:
            session.bulk_insert_mappings(models.BdAdCenterBindTable,new_bind_user_list)
            session.commit()
        print(f'账户中心:{center_id}新增{len(new_bind_user_list)}个用户，已经同步到数据库')
        return {'status':'success','message':f'账户中心:{center_id}新增{len(new_bind_user_list)}个用户，已经同步到数据库'}
    except Exception as e:
        print(f'账户中心:{center_id}新增{len(new_bind_user_list)}个用户，同步到数据库失败，原因为{e}')
        return {'status':'fail','message':f'账户中心:{center_id}新增{len(new_bind_user_list)}个用户，同步到数据库失败，原因为{e}'}
    

if __name__ == '__main__':
    center_id = '64339991'
    # print(get_db_bind_userid(center_id))
    # print(get_bd_center_bind_user(center_id))
    # print(new_bind_user(center_id))
    print(add_new_bind_user(center_id))