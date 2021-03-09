# _*_ coding:utf-8 _*_
# File Name: login_business
# Author： Emily
# Date:  2021/3/4  15:35
# Description : 登录业务


import time

from Test.Page.login_page import *


class LoginBusiness(object):

    def __init__(self, driver):
        self.login_business = LoginPage(driver)

    # 登录系统
    def go_system(self, username, password):
        self.login_business.input_username(username)
        self.login_business.input_password(password)
        self.login_business.click_login_button()
        time.sleep(2)
        return self.login_business.get_current_url()
