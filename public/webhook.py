# _*_ coding:utf-8 _*_
# File Name: webhook
# Author： Emily
# Date:  2021/3/16  14:51
# Description : 钉钉机器人通知


import json
import requests


from public.read_ini import get_value


class WebHook(object):
    def __init__(self):
        self.url = get_value("WEBHOOK", "web_hook_url")

    def web_hook(self, text, mobile):
        url = self.url
        program = {
            "msgtype": "text",
            "text": {"content": text},
            "at": {
                "atMobiles": mobile,
                "isAtAll": False
            }
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(program), headers=headers)