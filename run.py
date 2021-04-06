# _*_ coding:utf-8 _*_
# File Name: run
# Author： Emily
# Date:  2021/3/9  16:44
# Description : 程序入口


import time
import unittest

from public import setting
from public.HTMLTestRunner_cn import HTMLTestRunner
from public.report import create_report
from public.send_email import send_mail
from public.webhook import WebHook
from public.read_ini import get_value
from Test.Case.test01_login import TestLogin
from Test.Case.test02_login import TestLogin1


def add_case():
    """加载所有的测试用例"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestLogin1)
    all_case = unittest.TestSuite([suite1, suite2])
    return all_case


def run_case(all_case, result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""
    # 获取WebHook要@的人
    phone = get_value("WEBHOOK", "phone")

    # debug状态
    status = get_value("Base", "is_debug")

    # 如果是debug模式，不发WebHook
    if status == 'False':
        # WebHook发送开始通知
        WebHook().web_hook(
            '开始执行UI自动化测试任务\n测试环境：{}\n浏览器：Chrome Browser'.format(
                get_value("Base", "Env")
            ),
            phone
        )
    else:
        pass

    now = time.strftime("%Y-%m-%d")
    filename = result_path + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='好生源UI自动化测试报告',
                            description='环境：windows 10 浏览器：chrome')
    result = runner.run(all_case)
    fp.close()
    # 调用模块生成最新的报告
    report = create_report(setting.TEST_REPORT)
    # 调用发送邮件模块
    send_mail(report)
    # 如果是debug模式，不发WebHook
    if status == 'False':
        WebHook().web_hook(
            '版本号：{}\n测试环境：DEV\n浏览器：Chrome Browser\nUI自动化测试任务结束啦，快去邮箱查看测试报告吧!\
            \n运行总数：{}\n成功数量：{}\n失败数量：{}\n错误数量：{}\n跳过数量：{}'.format(
                get_value("VERSION", "version"), len(result.result),
                result.success_count, result.failure_count, result.error_count, result.skip_count
            ),
            phone
        )
    else:
        pass


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
