import psutil
import json
import requests

url = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}

# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo",
#     "programs": {
#         "output": "extend",
#         "filter":{
# 
#         }
#     },
#     "auth": "",
#     "id": 1
# }
#####################
# 获取管理员的授权码
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# f9e4be0a631ddec3c7733c3235e8e803

################################
#获取主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Zabbix server",
#                 "Linux server",
#             ]
#         }
#     },
#     "auth": "f9e4be0a631ddec3c7733c3235e8e803",
#     "id": 1
# } 
########################
#获取Linux server组的ID号
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
#     "auth": "f9e4be0a631ddec3c7733c3235e8e803",
#     "id": 1
# } #  groupid = 4
#########################
#获取Template os linux  模板ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux"
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "f9e4be0a631ddec3c7733c3235e8e803",
#     "id": 1
# } #templateid 10001
#########################
#创建主机web2, 它在2 号组中,使用10001模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web2",  #修改名字
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.12",  #修改IP
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"  #修改组ID
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
                "templateid": "10001" #修改模板ID
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
            "macaddress_a": "01234",  #mac地址
            "macaddress_b": "56768"
        }
    },
    "auth": "f9e4be0a631ddec3c7733c3235e8e803",  #钥匙
    "id": 1
}
###############################
r = requests.post(url, headers = headers, data = json.dumps(data))
print(r.json())