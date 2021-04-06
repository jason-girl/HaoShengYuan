# _*_ coding:utf-8 _*_
# File Name: test01_login
# Author： Emily
# Date:  2021/3/4  10:10
# Description : 登录好生源


# 导包

from Test.Case.base_case import BaseCase
from public.get_log import LogInfo
from public.read_ini import get_value


class TestLogin(BaseCase, LogInfo):

    @LogInfo.get_error
    def test_1(self):
        self.log.info('TestCase1 Start Running')
        # 获取用户名密码
        username = get_value(get_value('Base', 'Env'), 'username')
        password = get_value(get_value('Base', 'Env'), 'password')
        url = self.login.go_system(username, password)
        text = "https://gssdev.haoshengy.com/pc_workbench/workbench/overview"
        self.assertEqual(url, text, '当前页面URL不正确--测试不通过')
