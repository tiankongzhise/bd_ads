from src.service import BaiduWtShareMaterialServiceClient
from src.tool import BaiduOauthClient




class TestBaiduWtShareMaterialServiceClientClient(object):
    def __init__(self,center_id:str):
        self.center_id = center_id
        self.oauth_client = BaiduOauthClient(user_id=center_id)
    
    
    def test_add_share_material(self,source_user_name:str,target_user_name:str):
        share_material_params = {"sourceUserName":source_user_name,"targetUserName":target_user_name}
        share_material_client = self.oauth_client.create_oauth_client(source_user_name,BaiduWtShareMaterialServiceClient)
        rsp = share_material_client.add_share_info(share_material_params)
        print(f'{source_user_name}账号向{target_user_name}账号发起分享请求,返回结果为{rsp}')





if __name__ == '__main__':
    # center_id = '64339991'
    center_id = '64261939'
    source_user_name = '金蛛-迷茫(高学历)'
    taeget_user_name = '金蛛教育'
    test_client = TestBaiduWtShareMaterialServiceClientClient(center_id)
    test_client.test_add_share_material(source_user_name,taeget_user_name)
