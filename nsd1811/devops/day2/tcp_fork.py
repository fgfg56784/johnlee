import os
import time
import socket

class TcpServer:
    def __init__(self, host = '', port = 21567 ):
        self.addr = (host, port)
        self.ts = socket.socket()
        self.ts.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ts.bind(self.addr)
        self.ts.listen(1)
    
    def ixid(self, c_sock):  #具体操作
        while True:
            # print('客户机  %s' % c_addr)
            data = c_sock.recv(4096) 
            if data == b'quit\r\n':
                break

            print(data.decode('utf8'))  
            mas = '[%s] %s' % (time.strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf8'))
            c_sock.send(mas.encode('utf8'))

        c_sock.close()

    def acceptloop(self):  #循环接受请求,并用fork的方式回应请求
        while True:
            cli_sock, cli_addr = self.ts.accept()
            retval = os.fork()
            if retval:  #如果是父进程则关闭套接字连接
                cli_sock.close()  

                while True:   #当子进程pid为False时, 不再监视
                    result = os.waitpid(-1, 1)[0]   # waitpid 第一个值为子进程pid
                    if result == 0:   # 0 == False
                        break
            else:
                self.ts.close()  #关闭连接
                self.ixid(cli_sock) #进行套接字请求操作
                exit()

        cli_sock.close()

if __name__ == "__main__":
    s = TcpServer()
    s.acceptloop()
