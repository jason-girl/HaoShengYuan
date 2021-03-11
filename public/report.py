# _*_ coding:utf-8 _*_
# File Name: report
# Author： Emily
# Date:  2021/3/10  11:06
# Description : 生成最新的测试报告


import os


def create_report(report):
    info_list = os.listdir(report)
    info_list.sort(key=lambda fn: os.path.getmtime(report + "\\" + fn))
    file_new = os.path.join(report, info_list[-1])
    return file_new
