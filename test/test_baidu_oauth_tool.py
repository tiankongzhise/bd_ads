from src.tool import BaiduOauthClient
from src.service import BaiduCampaignServiceClient


def test_BaiduOauthClient():
    user_id = '64339991'
    client = BaiduOauthClient(user_id=user_id)
    campaign_client = client.create_oauth_client(user_name='金蛛-北大青鸟',service_mode=BaiduCampaignServiceClient,user_id=user_id)

if __name__ == '__main__':
    test_BaiduOauthClient()