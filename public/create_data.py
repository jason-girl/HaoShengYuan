# _*_ coding:utf-8 _*_
# File Name: create_data
# Author： Emily
# Date:  2021/3/16  10:11
# Description : 随机生成数据


import random
import string

from datetime import timedelta, date


# 生成名称
def cr_name(flag):
    """
    flag=1: 生成活动名称
    flag=2: 生成模板名称
    """
    last = random.randint(99, 1000)
    # 获取[a-z][A-Z]中的任意一个字母
    eng_list = string.ascii_letters
    eng = random.choice(eng_list)
    name = None
    if flag == 1:
        name = "UAT活动{}{}".format(last, eng)
    elif flag == 2:
        name = "UAT模板{}{}".format(last, eng)
    else:
        pass
    return name


# 生成数字(浮点数保留2位小数)
def cr_num(up, down, num_type='int'):
    """
    up: 随机数上限
    down: 随机数下限
    """
    num = None
    # num_type='int'：表示生成整数；num_type='float'：表示生成浮点数；num_type默认值为'int'
    if num_type == 'int':
        num = random.randint(up, down)
    elif num_type == 'float':
        num_float = random.uniform(up, down)
        num = round(num_float, 2)
    else:
        pass
    return str(num)


# 生成电话号码
def cr_phone():
    last = random.randint(999999999, 10000000000)
    phone = "9{}".format(last)
    return phone
