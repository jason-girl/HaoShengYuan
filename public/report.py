# _*_ coding:utf-8 _*_
# File Name: report
# Author： Emily
# Date:  2021/3/10  11:06
# Description : 生成最新的测试报告


import os


def create_report(report):
    """
    :param report: 测试报告目录
    fn: 代表info_list里面的文件名称
    report + "\\" + fn: 报告的绝对路径
    :return: 返回最新的报告文件
    """
    info_list = os.listdir(report)
    # 将report 文件夹下的文件进行排序
    info_list.sort(key=lambda fn: os.path.getmtime(report + "\\" + fn))
    file_new = os.path.join(report, info_list[-1])
    return file_new
