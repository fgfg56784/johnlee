#!/usr/local/bin/python3
import psutil
import json
import requests

url = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
headers = {"Content-Type": "application/json-rpc"}
################################
#获取钥匙
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1,
    "auth": None
}# 17ce761f4f67878ab6bb47c328a89f61
###################################
# data = 


r = requests.post(url, headers=headers, data=json.dumps(data))
for key in r.json():
    print(f"{key}: {r.json()[key]}")
