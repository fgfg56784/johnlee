import socket

server = '176.121.202.118'
port = 12345
addr = (server, port)

c = socket.socket()
c.connect(addr)

while True:
    data = input('(quit to end)> ') + '\r\n'
    c.send(data.encode())
    if data == 'quit\r\n':
        break
    rdata = c.recv(1024)
    print(rdata.decode(), end='')
c.close()
