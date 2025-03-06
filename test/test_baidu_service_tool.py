from src.tool import ServiceTool

class TestServiceTool(object):
    def __init__(self,user_id):
        self.user_id = user_id
    
    def test_update_center_info(self):
        rsp = ServiceTool.update_center_info(self.user_id)
        print(rsp)
    
    def test_get_user_info(self):
        rsp = ServiceTool.get_user_info(self.user_id)
        print(rsp)

    def test_get_migration_map(self):
        rsp = ServiceTool.get_migration_map('category')
        print(rsp)

if __name__ == '__main__':
    mcc_id = '64339991'
    test_service_tool = TestServiceTool(mcc_id)
    # test_service_tool.test_update_center_info()
    test_service_tool.test_get_user_info()
    # test_service_tool.test_get_migration_map()
