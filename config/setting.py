# _*_ coding:utf-8 _*_
# File Name: setting
# Author： Emily
# Date:  2021/3/10  10:43
# Description :


import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR, "Test", "Case")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "report")
