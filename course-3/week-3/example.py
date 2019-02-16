import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(command)

while True:
    data = sock.recv(512)
    if len(data) < 12:
        print('\n****DONE****')
        break
    print(data.decode())

sock.close()
