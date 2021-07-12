import socket
import threading

host = '192.168.68.144'
port = 65432


def listener():
    global s, connected
    while connected:
        data = s.recv(1024)
        print("Received", repr(data))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    connected = True
    x = threading.Thread(target=listener, args=(), daemon=True)
    x.start()
    while connected:
        d = input().encode()
        if d.decode() == "exit":
            connected = False
        s.sendto(d, (host, port))
