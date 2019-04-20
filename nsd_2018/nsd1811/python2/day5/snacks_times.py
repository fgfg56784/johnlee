import os
import time
class  SnacksTimes:
    def __init__(self, name):
        self.name = name

    def times(self):

def view():
    info = '''(1)  添加
(2)  查询
(3)  退出
请选择(1/2/3): '''
    cmds = {'1': app, '2': sel}
    while True:
        co = input(info)
        if co not in '123':
            print('无效的输入')
        if co == 3:
            break 
        cmds[co]

if __name__ == "__main__":
    fname = 'snacks.data'
    path = '/var/ftp/nsd_2018/nsd1811/python2/day5'
    file_path = os.path.join(path, fname)

    [^\ 、，。\>]