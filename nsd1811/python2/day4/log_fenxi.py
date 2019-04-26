#分析apache访问日志
#编写一个apache日志分析脚本
# import re
# import os
#
# def count_patt(file_path, patt):
#     patt_dict = {}
#     bian_patt = re.compile(patt)
#     with open(file_path, 'r') as fobj:
#         for line in fobj:
#             m = bian_patt.search(line)
#             if m:
#                 key = m.group()
#                 patt_dict[key] = patt_dict.get(key, 0) + 1   #如果result.get的不存在则返回0,并加1,  如此循环完成后字典就更新完了
#         return patt_dict
#
# if __name__ == "__main__":
#     paths = '/var/ftp/nsd_2018/nsd1811/python2/day4'
#     fname = 'access_log'
#     file_path = os.path.join(paths, fname)
#     ip = '^(\d+\.){3}\d+'
#     br = 'Chrome|FireFox|MSIE'
#     print(count_patt(file_path,ip))
#     print(count_patt(file_path,br))

# import re
# import os

# class fenxi:
#     def __init__(self, file_path, patt):
#         self.file_path = file_path
#         self.patt = patt
#     # def __str__(self):
#     def __call__(self):
#         exp = re.compile(self.patt)
#         count_dict = {}
#         with open(file_path, 'r') as fobj:
#             for line in fobj:
#                 m = exp.search(line)

#                 if m:
#                     key = m.group()
#                     count_dict[key] = count_dict.get(key, 0) + 1

#         for i in count_dict:
#             if len(i) < 20:
#                 print('%15s:%5s' % (i , count_dict[i]))
#             else:
#                 print('%-80s:%5s' % (i , count_dict[i]))

# def view():
#     info = '''(1)  统计ip
# (2)  统计浏览器
# (3)  统计访问网页
# (4)  退出
# 请选择(1/2/3): '''
#     cmds = {'1': ip_count, '2': br_count, '3': web_count}
#     while True:
#         co = input(info).strip()
#         if co not in '1234':
#             print('无效的输入')
#             continue

#         if co == '4':
#             print('Bye-bye')
#             break
#         cmds[co]()

# if __name__ == "__main__":
#     fname = 'access_log'
#     paths = '/var/ftp/nsd_2018/nsd1811/python2/day4'
#     file_path = os.path.join(paths, fname)
#     # file_path = input('请输入文件绝对路径: ')
#     ip = '^(\d+\.){3}\d+'
#     ip_count =  fenxi(file_path, ip)
#     br = 'Chrome|FireFox|MSIE'
#     br_count = fenxi(file_path, br)
#     web = '\"GET.*?\"'
#     web_count = fenxi(file_path, web)
#     view()

import os
import re
from collections import Counter

class CountPatt:
    def  count2(self, fname, patt):
        c = Counter()
        # patt_dict = {}
        spatt = re.compile(patt)
        with open(fname, 'r') as fobj:
            for line in fobj:
                m = spatt.search(line)
                if m:
                    key = m.group()
                    # patt_dict[key] = patt_dict.get(key, 0) + 1
                    c.update([key])
            # return patt_dict
            return c

if __name__ == "__main__":
    fname = 'access_log'
    paths = '/var/ftp/nsd_2018/nsd1811/python2/day4'
    file_path = os.path.join(paths, fname)
    ip = '^(\d+\.){3}\d+'
    br = 'Chrome|MSIE|FireFox'
    cp = CountPatt()
    cmds = {'1': ip, '2': br}
    info = '''(1)  统计ip
(2)  统计浏览器
(3)  退出
请选择(1/2/3): '''
    while True:
        co = input(info).strip()
        if co not in '123':
            print('无效的输入')
        if co == '3':
            break
        print(cp.count2(file_path,  cmds[co]).most_common(10))