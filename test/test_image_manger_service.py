from src.tool import BaiduOauthClient,url_to_base64
from src.service import BaiduImageManageServiceClient

class TestBaiduImageManageServiceClient(object):
    def __init__(self,user_id:str,user_name:str):
        oauth_client = BaiduOauthClient(user_id)
        self.client = oauth_client.create_oauth_client(user_name,BaiduImageManageServiceClient)

    def test_upload_img(self,query_params:dict|None = None,img_url:str|None = None,add_image:bool = False):
        if query_params is None:
            if img_url is None:
                raise Exception('query_params and img_url can be None at the same time')
            query_params = {
            'items':[
                {
                    'content':url_to_base64(img_url)
                }
            ],
            'addImage':add_image
        }
        return self.client.upload_image(query_params)
    
    def test_get_image_list(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                'pageNo':1,
                'pageSize':1000
            }
        return self.client.get_image_list(query_params)
    
    def test_share_image(self,query_params:dict|None = None):
        if query_params is None:
            query_params = {
                'imageId':'106214056',
                'url':'https://fc-feed.cdn.bcebos.com/0/pic/41f64c85b3ecc966b93963689d80aedf.jpg',
                'targetUserId':'64261942'
            }
        return self.client.share_image(query_params)


if __name__ == "__main__":
    uese_id = '64339991'
    source_user_name = '金蛛教育'
    target_user_name = '金蛛-迷茫(低学历)'
    img_url = 'https://jmy-pic.baidu.com/0/pic/14cb89a80e88c8dfe673e0806de3a96f.jpg'
    source_client = TestBaiduImageManageServiceClient(uese_id,source_user_name)
    target_client = TestBaiduImageManageServiceClient(uese_id,target_user_name)
    rsp = source_client.test_get_image_list()
    print(rsp)
