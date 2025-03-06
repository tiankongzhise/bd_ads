from .base import BaseAPIClient
from typing import Dict

class BaiduWtShareMaterialServiceClient(BaseAPIClient):
    def __init__(self, access_token: str, user_name:str,**kwargs):
        super().__init__(
            base_url="https://api.baidu.com/json/sms/service/WtShareMaterialService/",  # 根据实际文档替换
            access_token=access_token,
            user_name=user_name,
            **kwargs
        )
    
    def add_share_info(self, content_data: Dict) -> Dict:
        """发起申请"""
        #{"sourceUserName":"金蛛-JAVA","targetUserName":"金蛛教育"}
        return self.post("/addShareInfo", data=content_data)
    
    def get_share_info_list(self, content_data: Dict)-> Dict:
        """获取申请列表"""
        #{"shareType":0,"status":[1,2,3,4],"userName":"","pagingParam":{"pageNo":1,"pageSize":20}}
        return self.post("/getShareInfoList", data=content_data)
    
    def update_share_info_status(self, content_data: Dict)-> Dict:
        """修改申请状态"""
        return self.post("/updateShareInfoStatus", data=content_data)


