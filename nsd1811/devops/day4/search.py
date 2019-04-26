#! /usr/local/bin/python3

import requests

class  SearchDelivery:
    def __init__(self, cpname, tracknumber):
        self.cpname = cpname
        # self.tracknumber = tracknumber
        self.params = {cpname: tracknumber}

    def __call__(self):
        # url = 'http://www.kuaidi100.com/query?type=%s&postid=%s' % (self.cpname, self.tracknumber)
        url = 'http://www.kuaidi100.com/query'
        # ret1 = requests.get(url)
        ret1 = requests.get(url, params = self.params)
        ret2 = ret1.json()
        ret3 = ret2['data']
        for i  in ret3:
            ms = f"{i['time']}, {i['context']}"
            print(ms)

if __name__ == "__main__":
    cpdict = {1:'shentong',2:'youzhengguonei',3:'yuantong',4:'shunfeng',5:'yunda',6:'zhongtong',7:"tiantian",8:"debang"}
    info = '''快递公司列表
(1)  申通快递
(2)  中国邮政
(3)  圆通快递
(4)  顺丰快递
(5)  韵达快递
(6)  中通快递
(7)  天天快递
(8)  德邦物流
(9)  退出
请选择(1~9): '''
    while True:
        try:
            co = input(info).strip()
        except (KeyboardInterrupt, EOFError):
            print('\nBye-bye')
            break

        if co not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('无效的输入')
            continue
        co = int(co)
        if co == 9:
            print('Bye-bye')
            break
        cpname = cpdict[co]
        try:
            tracknumber = input('输入快递单号: ')
        except (KeyboardInterrupt, EOFError):
            continue
            
        cp1 = SearchDelivery(cpname, tracknumber)
        cp1()



