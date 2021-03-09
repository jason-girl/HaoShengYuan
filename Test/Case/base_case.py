# _*_ coding:utf-8 _*_
# File Name: base_case
# Author： Emily
# Date:  2021/3/4  15:52
# Description : 基础case


import unittest
from selenium import webdriver
from Test.Business.login_business import LoginBusiness


class BaseCase(unittest.TestCase):

    # 定义初始化方法
    def setUp(self) -> None:
        # 获取浏览器驱动对象
        self.driver = webdriver.Chrome()
        # 打开url
        url = 'https://gssdev.haoshengy.com/pc_workbench/login'
        self.driver.get(url)
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(10)
        self.login = LoginBusiness(self.driver)

    # 定义teardown
    def tearDown(self) -> None:
        # 关闭浏览器
        self.driver.quit()
