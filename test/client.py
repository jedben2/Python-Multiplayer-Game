import socket

host = '127.0.0.1'
port = 12342

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    num = 0
    while int(num) < 101:
        s.send(str(num).encode())
        num = s.recv(1024).decode()
        print(num)
