# adict = dict(['ab', ['name', 'john'], ('age', 22)])
# bdict = {}.fromkeys(['jerry', 'john', 'lucy'], 7)
# print(adict)
# print(bdict)
# for i in adict:
#     print('%s and %s' % (i, adict[i]))

# adict['email'] = 'jerry@ha.com'
# print(adict)

# print(adict.get('qq', 'not found'))
# print(adict.keys())
# print(adict.values())
# print(adict.items())
# adict.pop('email')
# print(adict)

#add dict 
# import getpass
# name_dict = {}
# def register():
#     name1 = input('请输入注册账户: ')
#     while True:
#         passwd1 = input('请输入密码: ')
#         passwd2 = input('请再次输入密码: ')
#         if passwd1 == passwd2:
#             name_dict[name1] = passwd1
#             print('\033[31;1m用户注册成功!\033[0m')
#             break
#         print('密码不一致,请重试')

# def login():
#     name = input('请输入用户名: ')
#     password = getpass.getpass('请输入密码: ')
#     if name:
#         if name_dict[name] == password:
#             print('\033[34;1m登录成功\033[0m')
#             exit(0)
#         else:
#             print('登录失败')

# def manu():
#     cmds = {'0': register, '1': login}
#     info = '''(0)  注册
# (1)  登录
# (2)  退出
# 请选择0/1/2: '''

#     while True:
#         coi = input(info).strip()
#         if coi not in [ '0', '1', '2' ]:
#            print('输入无效,请重试')
#            continue

#         if coi == 2:
#             print('Bye-bye')
#             break
#         cmds[coi]()

# if __name__ == "__main__":
#     manu()