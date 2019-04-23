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
    
    def ixid(self, c_sock):
        while True:
            # print('客户机  %s' % c_addr)
            data = c_sock.recv(4096)
            if data == b'quit\r\n':
                break

            print(data.decode('utf8'))
            mas = '[%s] %s' % (time.strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf8'))
            c_sock.send(mas.encode('utf8'))

        c_sock.close()

    def acceptloop(self):
        while True:
            cli_sock, cli_addr = self.ts.accept()
            retval = os.fork()
            if retval:
                cli_sock.close()

                while True:
                    result = os.waitpid(-1, 1)[0]
                    if result == 0:
                        break
            else:
                self.ts.close()
                self.ixid(cli_sock)
                exit()

        cli_sock.close()

if __name__ == "__main__":
    s = TcpServer()
    s.acceptloop()
