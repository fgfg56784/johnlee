# adict = {'john':23,'bob':22,'lucy':33}
# bdict = dict(('ab',['name','darong'],(12,23)))
# cdict = {}.fromkeys(['tinkiwinki','tiecy','lala','poll'],5)
# print(adict)
# print(bdict)
# print(cdict)
# for i in cdict:
#     print('%s is %s years old'% (i, cdict[i]))
# print('%(name)s' % (bdict))
# print(adict.get('lala','not found'))
# adict['lala'] = 5
# print(adict.get('lala', 'not found'))
# adict.setdefault('pop', 'music')
# print(adict)
# print(adict.items())
# print(adict.keys())
# print(adict.values())
# adict.update(bdict)
# print(adict)

import  getpass, pickle
# fname = '/root/userlist.txt'
# 记账本
import os, time, pickle
fname = '/tmp/%s.txt' % name

def save(fname):
    date = time.strftime('%Y/%m/%d')
    sh = int(input('金额: '))
    com = input('说明: ')

    with open(fname, 'rb') as save_fobj:
        da = pickle.load(save_fobj)

    balance = da[-1][-2] + sh
    info = [date, sh, 0, balance, com]
    da.append(info)

    with open(fname, 'wb') as fobj:
        pickle.dump(da, fobj)

def cost(fname):
    date = time.strftime('%Y/%m/%d')
    co = int(input('金额: '))
    com = input('说明: ')

    with open(fname, 'rb') as cost_fobj:
        da = pickle.load(cost_fobj)

    balance = da[-1][-2] - co
    info = [date, 0, co, balance, com]
    da.append(info)

    with open(fname, 'wb') as fobj:
        pickle.dump(da, fobj)

def quary(fname):
    date = time.strftime('%Y/%m/%d')
    data = '%-15s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment')
    print(data)

    with open(fname, 'rb') as red:
        line = pickle.load(red)
        for st in line:
            print('%-15s%-8s%-8s%-10s%-20s'% tuple(st))

def manu():
    cmds = {'1':save, '2':cost, '3':quary}
    info = '''(1)  收入
(2)  支出
(3)  查询
(4)  退出
请选择(1/2/3/4): '''

    if  not os.path.exists(fname):
        date = time.strftime('%Y/%m/%d')
        data = [
            [date, 0, 0, 10000, 'init']
        ]
        with open(fname, 'wb') as fi:
            pickle.dump(data, fi)

    while True:
        choice = input(info)
        if choice not in ('1234'):
            print('无效的输入')
        if choice == '4':
            print('Bye-bye')
            break

        cmds[choice](fname)



infomation ={'name':'password'}
user_file = '/tmp/userlist.txt'

def sign_up(user_file):
    global name
    name = input('请输入用户名: ')
    while True:
        passwd1 = input('请输入密码: ')
        passwd2 = input('请再次输入密码: ')

        if  r(name) or passwd1 != passwd2:
            # print('用户已存在')
            # continue
        # if passwd1 == passwd2:
            print('\033[31;1m用户已存在,或密码不一致\033[0m')
        else:
            with open(user_file, 'rb') as r_fobj:
                r = pickle.load(r_fobj)
                r.setdefault(name, passwd1)
            with open(user_file, 'wb') as user_fobj:
                pickle.dump(r, user_fobj)

            print('用户注册成功')
            break

def sign_in():
    global name
    name = input('请输入用户名: ')
    passwd = input('请输入密码: ')
    with open(user_file, 'rb') as r_fobj:
        r = pickle.load(r_fobj)

    if r[name] == passwd:
        print('登录成功')
        manu()

def view():
    with open(fname, 'wb') as user_fobj:
        pickle.dump(infomation, user_fobj)


    info = '''(1)  注册
(2)  登录
(3)  退出
请选择(1/2/3): '''
    cmds = {'1':sign_up, '2':sign_in}
    while True:
        ch = input(info).strip()
        if ch not in ('123'):
            print('无效的输入')
            continue
        if ch == 3:
            print('\033[34;1mBye-bye\033[0m]')
            break
        cmds[ch]()


if __name__ == '__main__':
    view()