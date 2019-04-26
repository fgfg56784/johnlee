import socket 
from time import strftime

host = ''
port = 23456
addr = (host, port)
us = socket.socket(type=socket.SOCK_DGRAM)
us.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
us.bind(addr)

while True:
    comment, cli_addr = us.recvfrom(1024)
    if comment == b'quit':
        break
    print(cli_addr)
    comment = comment.decode()
    print(comment, end='')
    
    # comment = '[%s], %s' % (strftime('%H%M%S'), comment)
    comment = '减肥不要吃%s' % comment
    us.sendto(comment.encode(), cli_addr)
us.close()