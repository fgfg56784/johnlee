import getpass  #导入名为getpass的模块

username = input('please enter username: ')
password = int(getpass.getpass('please enter your password: '))
print('*' * 40)
if username == 'bob' and password == 123456 :
    print('Login successful!!')
else:
    print('Login inorrect!!')
print('*' * 40)
import getpass
username = input('请输入用户名: ')
password = getpass.getpass(input('请输入密码: '))
i = 0
while i < 3 :
    if username == 'john' and password == '123456' :
        print('\033[31;1m登录成功\033[0m')
    else:
        print('登录失败')
        i += 1

























