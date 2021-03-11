# _*_ coding:utf-8 _*_
# File Name: run
# Author： Emily
# Date:  2021/3/9  16:44
# Description : 程序入口


# import unittest
# from Test.Case.test01_login import TestLogin
#
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TestLogin))
# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

import os
import sys
import time
import unittest


from config import setting
from package.HTMLTestRunner_cn import HTMLTestRunner
from public.report import create_report

sys.path.append(os.path.dirname(__file__))


def add_case(test_path=setting.TEST_DIR):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='test*.py')
    return discover


def run_case(all_case, result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""
    print(result_path)
    now = time.strftime("%Y-%m-%d")
    filename = result_path + '/' + now + 'result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='好生源UI自动化测试报告',
                            description='环境：windows 10 浏览器：chrome')
    runner.run(all_case)
    fp.close()
    create_report(setting.TEST_REPORT)


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
