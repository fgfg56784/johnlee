# 模拟栈结构
# list = []
# def push_it():
#     item = input('请输入内容: ')
#     if item:
#         list.append(item)
#         with open(fname, 'w') as f:
#             f.writelines(list)

# def pop_it():
#     if list:
#         print('从栈中弹出: %s' % (list.pop()))
#     else:
#         print('空栈')

# def view_it():
#     print('\033[31;1m%s\033[0m' % list)

# def show_manu():
#     cmds = {'0':push_it, '1':pop_it, '2':view_it}
#     info = '''(0)  压栈
# (1)  出栈
# (2)  查询 
# (3)  退出
# 请输入(0/1/2/3):  '''
#     while True:
#         coi = input(info).strip()[0]
#         # if coi not in ['0','1','2','3']:
#         #     print('输入无效,请重试')
#         #     continue

#         # if coi == '0':
#         #     push_it()
#         # elif coi ==  '1':
#         #     pop_it()
#         # elif coi == '2':
#         #     view_it()
#         # else:
#         if coi == '3':
#          print('Bye-bye')
#          break

#          cmds[coi]()

# if __name__ == "__main__":
#     fname = '/tmp/list.txt'
#     show_manu()

# adict = dict((['a', 'b'], ['age', 23]))
# print(adict)
# bdict = {'a':1, 'b':2, 'c':3}
# cdict = {}.fromkeys(('john','alice'), 23)
# print(bdict)
# print(cdict)
# for each_key in adict:
#     print('%s ha %s' % (each_key, adict[each_key]))
# print('%(a)s' % adict)
# print('%(age)s' % adict)

# print(adict['age'])
# adict['email'] = 'haha@dd.com'
# print(adict)

# del adict['email']
# print(adict)
# adict.pop('age')
# print(adict)
# adict.clear

# print('bob' in bdict)
# print(len(bdict))
# print(hash('age'))
# printe_list = {}
# def sign_up():
#     name = input('请输入用户名: ')
#     passwd1 = input('请输入密码: ')
#     passwd2 = input('请再次输入密码: ')
#     if passwd1 == passwd2:
#         print('用户创建成功')
#         name_list[name] = passwd2
#     else:
#         print('密码不一致,请重新输入')

# def sign_in():
#     name = input('请输入用户名: ')
#     passwd = getpass.getpass('密码: ')
#     if  name_list(name) == passwd:
#         print('\033[31;1m登录成功\033[0m')
#         exit(0)
#     else:
#         print('登录失败')

# def manu():
#     info = '''(0)  注册
# (1)  登录
# (2)  退出
# 请选择(0/1/2): '''
#     cmds = {'0': sign_up, '1':sign_in}
#     while True:
#         choice = input(info)
#         if choice not  in ['1', '2', '0']:
#             print('输入无效,请重试')

#         if choice == '2':
#             print('\nBye-bye')
#             break
#         cmds[choice]()

# if __name__ == "__main__":
#     manu()ash('haha'))

# bdict = adict.copy()
# print(adict)
# bdict['age'] = 222
# print(bdict)

# # print(adict.get('ag', 'not found'))
# # print(adict.setdefault('age', 23))
# # print(adict.items())
# # print(adict.keys())
# print(adict.values())
# dict2 = dict((['name', 'john'],['say', 'hello']))
# adict.update(dict2)
# print(adict)

# import getpass
# except KeyboardInterrupt:
#     print('Bye-bye')
#     exit()

# name_list = {}
# def sign_up():
#     name = input('请输入用户名: ')
#     passwd1 = input('请输入密码: ')
#     passwd2 = input('请再次输入密码: ')
#     if passwd1 == passwd2:
#         print('用户创建成功')
#         name_list[name] = passwd2
#     else:
#         print('密码不一致,请重新输入')

# def sign_in():
#     name = input('请输入用户名: ')
#     passwd = getpass.getpass('密码: ')
#     if  name_list(name) == passwd:
#         print('\033[31;1m登录成功\033[0m')
#         exit(0)
#     else:
#         print('登录失败')

# def manu():
#     info = '''(0)  注册
# (1)  登录
# (2)  退出
# 请选择(0/1/2): '''
#     cmds = {'0': sign_up, '1':sign_in}
#     while True:
#         choice = input(info)
#         if choice not  in ['1', '2', '0']:
#             print('输入无效,请重试')

#         if choice == '2':
#             print('\nBye-bye')
#             break
#         cmds[choice]()

# if __name__ == "__main__":
#     manu()

print('ha')