import socket
import threading
from netifaces import interfaces, ifaddresses, AF_INET
import time


class Host:
    @staticmethod
    def _get_ip():
        for ifaceName in interfaces():
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': ''}])]
            for a in addresses:
                if a != '' and a != "127.0.0.1":
                    return a

    def __init__(self, port, localhost):
        self.port = port
        self.ip = self._get_ip()
        if localhost: self.ip = '127.0.0.1'
        self.conns = []

    def manage_conn(self, conn, addr):
        print(f"Connected {addr}")
        connected = True
        while connected:
            time.sleep(2)
            conn.send(b't')
            data = conn.recv(1024).decode()
            print(data)
            if data == "exit": connected = False
            elif data == "connected?": conn.send(b'yes')
        print("closed")
        conn.close()
        self.conns.remove(conn)
        return

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen()
            conn, addr = s.accept()
            x = threading.Thread(target=self.manage_conn, args=(conn, addr))
            x.start()
            self.conns.append(conn)
            print(self.conns)
            while len(self.conns) > 0:
                pass
            print("no conns")
            s.close()


if __name__ == '__main__':
    host = Host(2000, True)
    host.start()
