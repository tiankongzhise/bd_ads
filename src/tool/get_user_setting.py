import pandas as pd
import os

class UserSetting(object):
    def __init__(self,file_path:str = './data',file_name:str|None = None):
        self.user_setting_file = []
        if file_name:
            self.user_setting_file.append(os.path.join(file_path,file_name))
        else:
            for file in os.listdir(file_path):
                if file.endswith('.xlsx'):
                    self.user_setting_file.append(os.path.join(file_path,file))
    
    def get_campaign_setting(self,file_path) -> dict:
        user_setting_df = pd.read_excel(file_path,sheet_name='计划')
        user_setting_dict = user_setting_df.to_dict('records')
        return user_setting_dict

    def get_adgroup_setting(self,file_path) -> dict:
        user_setting_df = pd.read_excel(file_path,sheet_name='广告组')
        user_setting_dict = user_setting_df.to_dict('records')
        return user_setting_dict
    def get_keyword_setting(self,file_path) -> dict:
        user_setting_df = pd.read_excel(file_path,sheet_name='关键词')
        user_setting_dict = user_setting_df.to_dict('records')
        return user_setting_dict
    
    def get_creative_setting(self,file_path) -> dict:
        user_setting_df = pd.read_excel(file_path,sheet_name='创意')
        user_setting_dict = user_setting_df.to_dict('records')
        return user_setting_dict
    def get_user_setting_file_list(self):
        return self.user_setting_file
    
    def get_user_name(self,file_path) -> str:
        file_name = os.path.basename(file_path)
        user_name = file_name.split('.')[0]
        return user_name
