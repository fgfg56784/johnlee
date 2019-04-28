#!/usr/local/bin/python3
import psutil
import json
import requests

url = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
headers = {"Content-Type": "application/json-rpc"}
################################
#获取钥匙
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1,
#     "auth": None
# }# 17ce761f4f67878ab6bb47c328a89f61
###################################
#获取软件版本
# data = {
#     "jsonrpc": "2.0",
#     "method": "configuration.export",
#     "params": {
#         "options": {
#             "hosts": [
#                 "10161"
#             ]
#         },
#         "format": "xml"
#     },
#     "auth": "17ce761f4f67878ab6bb47c328a89f61",
#     "id": 1
# }
#  @# xml version="1.0" encoding="UTF-8"
#  @# <version>4.2   <date>2019-04-27T00:20:16Z
###################################################
#获取主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "filter": {
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server",
#                 "web2"
#             ]
#         }
#     },
#     "auth": "17ce761f4f67878ab6bb47c328a89f61",
#     "id": 1
# }
###################################################
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "17ce761f4f67878ab6bb47c328a89f61",
#     "id": 1
# }# Linux servers groupid = 2,  Zabbix servers guoupid = 4
###################################################
#获取模板ID等信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "17ce761f4f67878ab6bb47c328a89f61",
#     "id": 1
# } # Template OS Linux templateid = 10001
###################################################
#创建监控主机
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.11",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "tags": [
            {
                "tag": "Host name",
                "value": "Linux server"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "macros": [
            {
                "macro": "{$USER_ID}",
                "value": "123321"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "17ce761f4f67878ab6bb47c328a89f61",
    "id": 1
}
###################################################
r = requests.post(url, headers=headers, data=json.dumps(data))
for key in r.json():
    print(f"{key}: {r.json()[key]}")
