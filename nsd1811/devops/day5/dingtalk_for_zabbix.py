#!/usr/local/bin/python3

import requests
import json
import getpass
import sys

def ding_talk(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}

    data = {
        "msgtype": "text", 
            "at": {"atMobiles": reminders,   
                "isAtAll": False},
            "text": {
                "content":msg}
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

if __name__ == "__main__":
    # reminders= list(sys.argv[1].split(','))
    # reminders= list(input('@').split(','))
    reminders = 13250580881
    # print(reminders)
    # msg = sys.argv[2]
    # msg = input("内容: ")
    msg = sys.argv[1]
    # url = getpass.getpass('机器人地址:')
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bea71a64e7abc78428b275ee814c5d9e9616031b71dc6fa7474557c94ea290ed'
    print(ding_talk(url, reminders, msg))