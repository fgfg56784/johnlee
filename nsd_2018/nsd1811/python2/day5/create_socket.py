# import socket
# import pickle

# host = ''  #表示0.0.0.0
# port = 12345 #端口号
# addr = (host, port) #绑定ip,端口号
# s = socket.socket()  #默认创建tcp套接字
# #程序执行结束后,操作系统会默认保留套接字1分钟,在1分钟内无法使用相同套接字连接
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 取消一分钟限制
# s.bind(addr) #绑定地址到套接字
# s.listen(1)   #启动监听过程, netstat -tupln | grep 12345

# # cli_sock, cli_addr = s.accept()  #等待客户端链接,收到连接返回(客户端套接字)
# # print('客户机', cli_addr)  #服务机打印客户机地址信息
# # cmds = {'1':'hao are you?\r\n', '2':'what\'s your name?\r\n', '3':'\xe4\xbd\xa0\xe9\xa3\x9f\xe9\xa5\xad\xe6\x9c\xaa\xe5\x90\x96?\r\n'}
# while True:
#     try:
#         cli_sock, cli_addr = s.accept()  #等待客户端链接,收到连接返回(客户端套接字)
#     except KeyboardInterrupt:
#         print()
#         break
#     print('客户机', cli_addr)  #服务机打印客户机地址信息
#     while True:
#         data = cli_sock.recv(1024)  #客户机输入内容
#         if  data  in  [b'quit']:             # b'\r\n', b'bye\r\n', 
#             print(b'Bye-bye')
#             break
#         print(data.decode())  #服务机打印客户机输入内容
#     # a = input('内容(1/2/3): ')
#         a = input('> ') + '\r\n'
#     # co = cmds[a]
#     # fname = '/tmp/neirong.txt'
#     # with open(fname, 'wb') as fobj:
#     #     pickle.dump(a, fobj)
#     # with open(fname, 'rb') as fobj:
#     #     ne = pickle.load(fobj)
#         cli_sock.send(a.encode())  #发送给客户机的内容
#     cli_sock.close()  #关闭套件字连接
# s.close() #关闭监听

import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.bind(addr)
s.listen(1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

cli_sock, cli_addr = s.accept()
print('客户机: %s' % cli_addr)
data = cli_sock.recv(1024)
print(data)
cli_sock.send(b'hello\r\n')
cli_sock.close()
s.close()

