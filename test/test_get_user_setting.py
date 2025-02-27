from src.tool import UserSetting



if __name__ == '__main__':
    user_setting = UserSetting()
    file_list = user_setting.get_user_setting_list()
    for file in file_list:
        user_name = user_setting.get_user_name(file)
        campaign_setting = user_setting.get_campaign_setting(file)
        adgroup_setting = user_setting.get_adgroup_setting(file)
        keyword_setting = user_setting.get_keyword_setting(file)
        creative_setting = user_setting.get_creative_setting(file)
    print(user_name)
    print(campaign_setting)
    print(adgroup_setting)
    print(keyword_setting)
    print(creative_setting)