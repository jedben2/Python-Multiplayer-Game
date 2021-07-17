import socket

host = '127.0.0.1'
port = 12342

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    num = 0
    while int(num) < 101:
        num = int(conn.recv(1024).decode())
        print(num)
        conn.send(str(num + 1).encode())