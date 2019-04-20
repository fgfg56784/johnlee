import socket

host = '176.121.202.118'
port = 23456
addr = (host, port)
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data  = input('(quit to end)> ') + '\r\n'
    c.sendto(data.encode(), addr)
    info = c.recvfrom(1024)
    data = info[0]
    print(data.decode())
