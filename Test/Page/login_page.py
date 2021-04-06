# _*_ coding:utf-8 _*_
# File Name: login_page
# Author： Emily
# Date:  2021/3/4  15:07
# Description : 登录页面


from selenium.webdriver.common.by import By
from public.base import Base


login_username = (By.CLASS_NAME, 'el-input__inner', 1)
login_password = (By.CLASS_NAME, 'el-input__inner', 2)
login_btn = (By.CLASS_NAME, 'login__button', 0)


class LoginPage(object):

    def __init__(self, driver):
        self.element = Base(driver)

    def input_username(self, content):
        # 输入手机号
        self.element.base_input(login_username, content)

    def input_password(self, content):
        # 输入密码
        self.element.base_input(login_password, content)

    def click_login_button(self):
        # 点击登录
        self.element.base_click(login_btn)

    def get_current_url(self):
        return self.element.base_get_current_url()
