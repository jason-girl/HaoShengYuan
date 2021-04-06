### 概述

HsyUi_AutoTest是基于Python+Selenium+Unittest的UI自动化测试框架，采用了PO（Page Object）设计模式，将页面对象与用例进行分离，提高了代码的复用性，降低了维护成本。

### 功能

* 生成测试报告
* 自动截图
* 自动发送测试报告
* 自动发送钉钉推送
* 生成运行日志

### 目录结构

│  run.py// 用例执行入口
│
├─config // 配置文件
│  │  user.ini // 元素配置
│  │  __init__.py
│
├─public
│  │  base.py // 元素操作基类
│  │  create_data.py // 创建数据
│  │  get_log.py // 获取日志
│  │  HTMLTestRunner_cn.py
│  │  read_ini.py  // 读取配置文件
│  │  report.py // 获取测试报告
│  │  screenshot.py // 截图
│  │  send_email.py // 发送邮件
│  │  setting.py // 设置
│  │  webhook.py // 钉钉推送
│  │  __init__.py
│
├─report // 测试报告
│  │
│  └─screenshot// 截图存放
│
├─Test ---------------------- // 测试用例
│ ├─Business ---------------- // 业务层
│ │ ├─__init__.py 
│ │ └─login_business.py ----- // 登录业务逻辑
│ ├─Case -------------------- // 用例层
│ │ ├─__init__.py 
│ │ ├─base_case.py ---------- // 用例基类
│ │ └─test01_login.py ------- // 登录测试用例
│ ├─Page -------------------- // 页面层
│ │ ├─__init__.py 
│ │ └─login_page.py --------- // 登录页面
│ └─__init__.py 

### 说明

1.元素配置及读取

* 具体元素定位直接放在page页面里面

```python
login_username = (By.CLASS_NAME, 'el-input__inner', 1)
login_password = (By.CLASS_NAME, 'el-input__inner', 2)
login_btn = (By.CLASS_NAME, 'login__button', 0)
```

base.py

```python
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
```

* 可以根据需求使用不同的定位方式

