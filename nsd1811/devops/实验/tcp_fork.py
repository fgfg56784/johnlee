import os
import socket
from time import strftime

class TcpServer:
    def __init__(self, host='', port=12312):
        self.addr = (host, port)
        self.ts = socket.socket()
        self.ts.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ts.bind(self.addr)
        self.ts.listen(1)

    def forklink(self, c_sock):
        while True:
            redata = c_sock.recv(4096)
            if redata == b'quit\r\n' or b'\r\n':
                c_sock.close()
                break
            sedata = '[%s]  %s' % (strftime('%Y/%m/%d %H:%M:%S'), redata.decode('utf8'))
            c_sock.send(sedata.encode('utf8'))
        self.ts.close()

    def serverloop(self):
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
                self.forklink(cli_sock)
                exit()

        cli_sock.close()

if __name__ == "__main__":
    s1 = TcpServer()
    s1.serverloop()