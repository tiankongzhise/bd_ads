from src.material_migration import MaterialMigration


class testMaterialMigration(object):
    def __init__(self):
        self.center_id = '64339991'
        self.source_user_name = '金蛛教育'
        self.target_user_name = '金蛛-北大青鸟'

    def test_category_migration(self,type_class:str = '文章'):
        material_migration = MaterialMigration(self.center_id,self.source_user_name,self.target_user_name)
        material_migration.category_migration(type_class)
    
    def test_article_migration(self):
        material_migration = MaterialMigration(self.center_id,self.source_user_name,self.target_user_name)
        material_migration.article_migration()


if __name__ == '__main__':
    test = testMaterialMigration()
    # test.test_category_migration()
    test.test_article_migration()
        
