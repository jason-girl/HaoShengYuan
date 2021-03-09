# _*_ coding:utf-8 _*_
# File Name: run
# Author： Emily
# Date:  2021/3/9  16:44
# Description : 程序入口


import unittest
from Test.Case.test01_login import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
