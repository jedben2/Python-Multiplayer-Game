import socket
import threading

host = '127.0.0.1'
port = 2000

# def listener():
#     global s, connected
#     while connected:
#         data = s.recv(1024)
#         print("Received", repr(data))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    connected = True
    # x = threading.Thread(target=listener, args=(), daemon=True)
    # x.start()
    while connected:
        data = input(">>> ")
        if data == "exit": connected = False
        s.send(data.encode("utf-8"))
        data_new = s.recv(1024)
        print(data_new.decode())

    print("closed")
