# _*_ coding:utf-8 _*_
# File Name: base
# Author： Emily
# Date:  2021/3/12  10:00
# Description :


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法(提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        element, index = loc[:2], loc[-1]
        try:
            ele = WebDriverWait(
                self.driver, timeout=timeout, poll_frequency=poll
            ).until(
                lambda x: x.find_elements(*element)
            )[index]
        except (NoSuchElementException, TimeoutError, IndexError):
            return False
        else:
            return ele

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 获取当前页面地址
    def base_get_current_url(self):
        return self.driver.current_url
