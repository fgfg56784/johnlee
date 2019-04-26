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
    reminders= list(input('@').split(','))
    # print(reminders)
    # msg = sys.argv[2]
    msg = input("内容: ")
    url = getpass.getpass('机器人地址:')
    print(ding_talk(url, reminders, msg))