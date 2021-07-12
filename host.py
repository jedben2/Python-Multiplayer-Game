import socket
import threading
from netifaces import interfaces, ifaddresses, AF_INET

class Host:
    @staticmethod
    def _getip():
        for ifaceName in interfaces():
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': ''}])]
            for a in addresses:
                if a != '' and a != "127.0.0.1":
                    return a

    def __init__(self, port, localhost):
        self.port = port
        self.ip = self._getip()
        if localhost: self.ip = '127.0.0.1'
        self.conns = []

    def manage_conn(self, conn, addr):
        print(f"Connected {conn}, {addr}")
        connected = True
        while connected:
            pass

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen()
            conn, addr = s.accept()
            x = threading.Thread(target=self.manage_conn)
            x.start()


if __name__ == '__main__':
    host = Host(2000, True)
    host.start()