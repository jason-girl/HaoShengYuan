# _*_ coding:utf-8 _*_
# File Name: test01_login
# Author： Emily
# Date:  2021/3/4  10:10
# Description : 登录好生源


# 导包

from Test.Case.base_case import BaseCase


class TestLogin(BaseCase):

    def test_1(self):
        url = self.login.go_system('95555555555', '12345678')
        text = "https://gssdev.haoshengy.com/pc_workbench/workbench/overview"
        self.assertEqual(url, text, '当前页面URL不正确--测试不通过')
