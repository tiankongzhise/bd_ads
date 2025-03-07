from src.service import BaiduMaterialBrandModServiceClient
from src.tool import BaiduOauthClient,ServiceTool
import tomllib
from tqdm import tqdm

def trans_toml_data(toml_path:str = 'bd_ads_brand.toml')->list[dict]:
    with open(toml_path,'rb') as f:
        toml_data = tomllib.load(f)
        brand_toml_list = [toml_data['bird'],toml_data['kawa'],toml_data['jinzhu']]
        brand_params_list = []
        for brand in brand_toml_list:
            brand_params_list.append(create_brand_prams(brand))
        return brand_params_list
             

def create_brand_prams(toml_data:dict)->list[dict]:
    params = {
        'status':toml_data['status'],
        'name':toml_data['name'],
        'logo':[{'type':toml_data['logo_type'],'imageUrl':toml_data['logo_url'],'name':toml_data['logo_name']}],
        'slogan':toml_data['slogan'],
        'serviceScope':toml_data['serviceScope'],
        'advantage':toml_data['advantage'],
        'brandStory':toml_data['brandStory'],
        'image':[{'type':'sixteenToNine','imageUrl':img_url} for img_url in toml_data['image']],
        'tags' :[{"tagName":"品牌认证","tagDesc":f"{toml_data['name']}旗下口碑示范校区"},{"tagName":"零基础可学","tagDesc":"18门专业零基础也能学会"},{"tagName":"小班制实操","tagDesc":"全程指导小班制教学"},{"tagName":"推荐就业","tagDesc":"入学签订就业协议推荐就业"}]
    }
    return params


def create_brand(center_id:str,user_name:str,query_params:dict):
    barnd_client = BaiduOauthClient(center_id).create_oauth_client(user_name,BaiduMaterialBrandModServiceClient)
    rsp = barnd_client.add_brand(query_params)
    return rsp


def test():
    center_id = '64339991'
    user_name = '金蛛-BCNT'
    brand_params_list = trans_toml_data()
    for brand_params in brand_params_list:
        rsp = create_brand(center_id,user_name,brand_params)
        print(f'账号:{user_name},创立品牌{brand_params['name']}:{rsp['header']['desc']}')
        if rsp['header']['desc'] != 'success':
            print(f'账号:{user_name},创立品牌{brand_params['name']}失败，原因为{rsp}')
    
    
def create_jmy_content_brand(center_id:str|None = None):
    center_id = center_id or '64339991'
    user_list = ServiceTool.get_user_list(center_id)
    brand_params_list = trans_toml_data()
    for user_name in tqdm(user_list,desc='创建品牌'):
        for brand_params in brand_params_list:
            rsp = create_brand(center_id,user_name,brand_params)
            print(f'账号:{user_name},创立品牌{brand_params['name']}:{rsp['header']['desc']}')
            if rsp['header']['desc'] != 'success':
                print(f'账号:{user_name},创立品牌{brand_params['name']}失败，原因为{rsp}')

if __name__ == '__main__':
    create_jmy_content_brand()



