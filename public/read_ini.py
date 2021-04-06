# _*_ coding:utf-8 _*_
# File Name: read_ini
# Author： Emily
# Date:  2021/3/16  15:47
# Description :  读取配置文件


import configparser

from public import setting


def get_value(key, value):
    con = configparser.ConfigParser()
    con.read(setting.CONFIG_DIR, encoding='utf-8')
    data = con.get(key, value)
    return data
