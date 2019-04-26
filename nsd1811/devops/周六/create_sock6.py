import socket

host = ''
port = 10200
addr = (host, port)
ts = socket.socket()
ts.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ts.bind(addr)
ts.listen(1)

cli_sock, cli_addr = ts.accept()
print('客户机 (%s, %s) 已接入' % cli_addr) 
while True:
    data = cli_sock.recv(1024)
    if data == b'quit\r\n' :
        cli_sock.send(b'quit\r\n')
        break
    print(data.decode())
    say = input('> ') + '\r\n'
    cli_sock.send(say.encode())
cli_sock.close()
ts.close()