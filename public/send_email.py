# _*_ coding:utf-8 _*_
# File Name: send_email
# Author： Emily
# Date:  2021/3/16  9:46
# Description : 发送邮件相关


import smtplib


from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.read_ini import get_value


def send_mail(file_new):
    # 读取user.ini配置信息
    host = get_value("User", "host_server")
    sender = get_value("User", "from")
    receiver = get_value("User", "to")
    user = get_value("User", "user")
    pwd = get_value("User", "password")
    subject = get_value("User", "subject")

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg["From"] = sender
    msg["To"] = receiver

    # 邮件正文内容
    msg.attach(MIMEText('附件为本次UI自动化测试报告，为保证最佳浏览效果，请使用Chrome打开查看', 'plain', 'utf-8'))

    # 构造附件，传入最新的测试报告文件
    sendfile = open(file_new, 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="UITestReport.html"'
    msg.attach(att)

    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.connect(host)
    smtp.login(user, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功")
