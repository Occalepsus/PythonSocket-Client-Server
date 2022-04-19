import socket
from threading import Thread


class ClientSocket(Thread):
    def __init__(self, host: str, port: int):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.5)
        self.isRunning = False

    def start(self):
        self.socket.connect((self.host, self.port))
        self.isRunning = True
        Thread.start(self)

    def handle(self):
        pass

    def run(self):
        while self.isRunning:
            try:
                self.handle()
            except socket.timeout:
                continue
            except socket.error as e:
                print("Socket error : " + e)
                break

        self.isConnected = False
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print('Socket closed, bye !')

    def stop(self):
        self.isRunning = False


class InputSocket(ClientSocket):
    def __init__(self, host: str, port: int, callback: callable(bytes)):
        ClientSocket.__init__(self, host, port)
        self.callback = callback

    def handle(self):
        msg = self.socket.recv(1024)
        if msg == b'':
            self.stop()
        else:
            print('Data received')
            self.callback(msg)


class OutputSocket(ClientSocket):
    def __init__(self, host: str, port: int):
        ClientSocket.__init__(self, host, port)

    def send(self, msg):
        if self.isRunning:
            self.socket.send(msg)
            print('Data sent')
