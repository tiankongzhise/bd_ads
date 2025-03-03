from src.tool import BaiduOauthClient,img_url_to_base64
from src.db import  OauthDb,BdAuthTokenTable,BdServiceDb,BdAdMaterialTransferTable
from src.service import BaiduMaterialArticleServiceClient

class MaterialMigration(object):
    def __init__(self,center_id:str,source_user_name:str,target_user_name:str):
        bdClient = BaiduOauthClient(user_id=center_id)
        self.source_user_name = source_user_name
        self.target_user_name = target_user_name
    
    def url_migration(self,material_url:str)->str:
        url_source_client = BaiduOauthClient(user_name=self.source_user_name)
        url_target_client = BaiduOauthClient(user_name=self.target_user_name)
        
        




if __name__ == "__main__":
    uese_id = '64339991'
    user_name = '金蛛-北大青鸟'
    test_client = TestBaiduCampaignServiceClient(uese_id,user_name)
    rsp = test_client.test_add_campaign()
    print(rsp)
