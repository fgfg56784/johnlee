import socket 
server = '176.121.202.118'
port = 10200
addr = (server, port)
tc = socket.socket()
tc.connect(addr)

while True:
    say = input('(quit to end)> ') + '\r\n'
    tc.send(say.encode())
    data = tc.recv(1024)
    if data == b'quit\r\n':
        break
    print(data.decode())  
tc.close()