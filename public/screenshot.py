# _*_ coding:utf-8 _*_
# File Name: screenshot
# Author： Emily
# Date:  2021/3/15  10:57
# Description : 截图相关


from public import setting


def insert_img(driver, file_name):
    """
    截图
    :param driver: 启动浏览器
    :param file_name: 截图文件名
    :return: 返回指定路径的截图文件
    """
    file_path = setting.TEST_REPORT + "/screenshot/" + file_name
    return driver.get_screenshot_as_file(file_path)
