from src.tool import BaiduOauthClient,ServiceTool
from src.db import  BdServiceDb,BdAdMaterialTransferTable
from src.service import BaiduMaterialArticleServiceClient,BaiduWtMaterialCategoryServiceClient
from typing import Type
from typing import Literal
from tqdm import tqdm

class MaterialMigration(object):
    def __init__(self,center_id:str,source_user_name:str,target_user_name:str,db:BdServiceDb = BdServiceDb(),table:Type[BdAdMaterialTransferTable] = BdAdMaterialTransferTable):
        self.bdClient = BaiduOauthClient(user_id=center_id)
        self.source_user_name = source_user_name
        self.target_user_name = target_user_name
        self.user_info = ServiceTool.get_user_info(center_id)[center_id]
        self.db = db
        self.table = table
    
    # def url_migration(self,material_url:str,add_img_flag:bool = False)->str:
    #     url_target_client = self.bdClient.create_oauth_client(self.target_user_name,BaiduImageManageServiceClient)
    #     query_params = {
    #         'items':[
    #             {
    #                 'content':img_url_to_base64(material_url)
    #             }
    #         ],
    #         'addImage':add_img_flag
    #     }
    #     rsp = url_target_client.upload_image(query_params)
    
    def category_migration(self,type_class:Literal['产品','文章','问答','人员','案例'])->str:
        migration_reuslt = []
        type_map = {
            '产品':3,
            '文章':4,
            '问答':5,
            '人员':6,
            '案例':7
        }
        
        source_category_client = self.bdClient.create_oauth_client(self.source_user_name,BaiduWtMaterialCategoryServiceClient)
        target_category_client = self.bdClient.create_oauth_client(self.target_user_name,BaiduWtMaterialCategoryServiceClient)
        

        
        
        
        source_category_dict = ServiceTool.get_category_list(source_category_client,type_class,type_map)
        for key,value in source_category_dict.items():
            temp_dict = {}
            temp_dict['source_user_id'] = self.user_info[self.source_user_name]
            temp_dict['target_user_id'] = self.user_info[self.target_user_name]
            temp_dict['material_id'] = key
            temp_dict['material_name'] = value['name']
            temp_dict['description'] = f'账号:{self.source_user_name}的{type_class}分类:{value["name"]},categoryId:{key}'
            
            query_params = {
                'name':value['name'],
                'type':value['type'],
            }
            rsp = target_category_client.add_category(query_params)
            if rsp['header']['desc'] != 'success':
                temp_dict['migrate_status'] = '失败'
                print(f'❌ 账户:{self.source_user_name}分类{type_class}的{value['name']}迁移失败:{rsp}')
                migration_reuslt.append(temp_dict)
                continue
            temp_dict['target_material_id'] = rsp['body']['data'][0]['categoryId']
            temp_dict['target_material_name'] = value['name']
            temp_dict['migrate_status'] = '成功'
            temp_dict['target_description'] = f'账号:{self.target_user_name}的{type_class}分类:{value["name"]},categoryId:{temp_dict["target_material_id"]},来自账户:{self.source_user_name}'
            migration_reuslt.append(temp_dict)
        print(f'✅ {self.source_user_name}的{type_class}分类数据迁移到{self.target_user_name}完毕')

        with self.db.get_session() as session:
            try:
                session.bulk_insert_mappings(self.table,migration_reuslt)
                session.commit()
                print(f'✅ {self.source_user_name}的{type_class}分类数据迁移到{self.target_user_name}成功的结果，插入数据库成功')
            except Exception as e:
                session.rollback()
                print(f'❌ {self.source_user_name}的{type_class}分类数据迁移到{self.target_user_name}成功,但结果计入数据库失败')
        
                
    
    def article_migration(self)->str:
        migration_reuslt = []
        source_article_client = self.bdClient.create_oauth_client(self.source_user_name,BaiduMaterialArticleServiceClient)
        target_article_client = self.bdClient.create_oauth_client(self.target_user_name,BaiduMaterialArticleServiceClient)
        
        
        query_params = {
                    'pageNum':1,
                    "pageSize":500,
                    "materialType":2,
        }
        
        article_rsp = source_article_client.get_article_list(query_params)
        
        if article_rsp['header']['desc'] != 'success':
            raise Exception(f'获取文章列表失败:{article_rsp}')
        article_list = article_rsp['body']['data'][0]['list']
        
        category_map = ServiceTool.get_migration_map('category')
        
        for article in tqdm(article_list,desc='文章迁移中'):
            run_result_dict = {}
            run_result_dict['source_user_id'] = self.user_info[self.source_user_name]
            run_result_dict['target_user_id'] = self.user_info[self.target_user_name]
            run_result_dict['material_class'] = 'article'
            run_result_dict['material_id'] = article['articleId']
            run_result_dict['material_name'] = article['title']
            run_result_dict['description'] = f'账号:{self.source_user_name}的文章:{article["title"]},articleId:{article["articleId"]}'
            
            temp_params = {
                'categoryId':category_map.get(article['categoryId'],{}).get(self.user_info[self.target_user_name],1),#必填
                'title':article['title'],#必填
                'image':article.get('image',None),
                'summary':article.get('summary',None),
                'content':article.get('content',None),
                'status':1 if article['status'] == 5  else 0,#必填
                'tradeId':article.get('tradeId',None),
                'materialType':article.get('materialType',None),#必填
                'articleGeneratedMode':article.get('articleGeneratedMode',None),
                'ugcImageUrl':article.get('ugcImageUrl',None),
            }
            query_params = {key: value for key, value in temp_params.items() if value is not None}
            rsp = target_article_client.add_article(query_params)
            if rsp['header']['desc'] != 'success':
                run_result_dict['migrate_status'] = '失败'
                print(f'❌ 账户:{self.source_user_name}文章{article["title"]}迁移失败:{rsp}')
                migration_reuslt.append(run_result_dict)
                continue
            run_result_dict['target_material_id'] = rsp['body']['data'][0]['articleId']
            run_result_dict['target_material_name'] = article['title']
            run_result_dict['migrate_status'] = '成功'
            run_result_dict['target_description'] = f'账号:{self.target_user_name}的文章:{article["title"]},articleId:{run_result_dict["target_material_id"]},来自账户:{self.source_user_name}'
            migration_reuslt.append(run_result_dict)
        with self.db.get_session() as session:
            try:
                session.bulk_insert_mappings(self.table,migration_reuslt)
                session.commit()
                print(f'✅ {self.source_user_name}的文章数据迁移到{self.target_user_name}成功的结果，插入数据库成功')
            except Exception as e:
                session.rollback()
                print(f'❌ {self.source_user_name}的文章数据迁移到{self.target_user_name}成功,但结果计入数据库失败,原因是{str(e)}')
                print(migration_reuslt)




