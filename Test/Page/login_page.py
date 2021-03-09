# _*_ coding:utf-8 _*_
# File Name: login_page
# Author： Emily
# Date:  2021/3/4  15:07
# Description : 登录页面


from selenium.webdriver.common.by import By
from config.eleconfig.login_ele import *


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def input_username(self, content):
        # 输入手机号
        self.driver.find_elements(By.CLASS_NAME, login_username[0])[login_username[1]].send_keys(content)

    def input_password(self, content):
        # 输入密码
        self.driver.find_elements(By.CLASS_NAME, login_password[0])[login_password[1]].send_keys(content)

    def click_login_button(self):
        # 点击登录
        self.driver.find_elements(By.CLASS_NAME, login_btn[0])[login_btn[1]].click()

    def get_current_url(self):
        return self.driver.current_url
