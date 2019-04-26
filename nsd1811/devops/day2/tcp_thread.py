from threading import Thread
from time import strftime
import socket
import os

class TcpThreadServer:
    def __init__(self, host = '' , port = 12345):
        self.addr = (host, port)
        self.tts = socket.socket()
        self.tts.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tts.bind(self.addr)
        self.tts.listen(1)

    def ixid(self, c_sock):
        while True:
            data = c_sock.recv(4096)
            if data == b'quit\r\n':
                break

            mas = '[%s] %s' % (strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf8'))
            c_sock.send(mas.encode('utf8'))

    def threadloop(self):
        while True:
            cli_sock, cli_addr = self.tts.accept()
            
            retval = os.fork()
            if retval:
                cli_sock.close()
                
                while True:
                    pid = os.waitpid(-1, 1)[0]
                    if pid == 0:
                        break
            
            else:
                self.tts.close()
                self.ixid(cli_sock)
                exit()
        cli_sock.close()

if __name__ == "__main__":
    s = TcpThreadServer()
    s.threadloop()