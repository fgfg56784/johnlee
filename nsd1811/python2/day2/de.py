# def foo():
#     print('foo')
#     bar()
#
# def bar():
#     print('bar')
#
# foo()

# def get_info(name, age):
#     print('%s is %s years old' % (name, age))
# get_info(name='john', age=23)

#记账本
# import os, time, pickle
# fname = '/tmp/database.txt'
#
# def save(fname):
#     date = time.strftime('%Y/%m/%d')
#     sh = int(input('金额: '))
#     com = input('说明: ')
#
#     with open(fname, 'rb') as save_fobj:
#         da = pickle.load(save_fobj)
#
#     balance = da[-1][-2] + sh
#     info = [date, sh, 0, balance, com]
#     da.append(info)
#
#     with open(fname, 'wb') as fobj:
#         pickle.dump(da, fobj)
#
# def cost(fname):
#     date = time.strftime('%Y/%m/%d')
#     co = int(input('金额: '))
#     com = input('说明: ')
#
#     with open(fname, 'rb') as cost_fobj:
#         da = pickle.load(cost_fobj)
#
#     balance = da[-1][-2] - co
#     info = [date, 0, co, balance, com]
#     da.append(info)
#
#     with open(fname, 'wb') as fobj:
#         pickle.dump(da, fobj)
#
# def quary(fname):
#     date = time.strftime('%Y/%m/%d')
#     data = '%-15s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment')
#     print(data)
#
#     with open(fname, 'rb') as red:
#         line = pickle.load(red)
#         for st in line:
#             print('%-15s%-8s%-8s%-10s%-20s'% tuple(st))
#
# def manu():
#     cmds = {'1':save, '2':cost, '3':quary}
#     info = '''(1)  收入
# (2)  支出
# (3)  查询
# (4)  退出
# 请选择(1/2/3/4): '''
#
#     if  not os.path.exists(fname):
#         date = time.strftime('%Y/%m/%d')
#         data = [
#             [date, 0, 0, 10000, 'init']
#         ]
#         with open(fname, 'wb') as fi:
#             pickle.dump(data, fi)
#
#     while True:
#         choice = input(info)
#         if choice not in ('1234'):
#             print('无效的输入')
#         if choice == '4':
#             print('Bye-bye')
#             break
#
#         cmds[choice](fname)
#
# if __name__ == '__main__':
#     manu()
# def ha():
#     global name
#     name = 'john'
#     # return name
#
# if __name__ == '__main__':
#     ha()
#     print(name)

