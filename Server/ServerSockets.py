import socket
import sys
import traceback
from threading import Thread


def create_socket(ip, port):
    new_socket = socket.socket()
    new_socket.bind((ip, port))
    new_socket.listen(5)
    new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return new_socket


class SocketServer(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = create_socket(ip, port)
        self.socket.settimeout(0.5)
        self.isConnected = False
        self.isRunning = True

    def handle(self):
        pass

    def run(self):
        print("Port {} is ready for connection...".format(self.port))
        while self.isRunning:
            if not self.isConnected:
                try:
                    (self.socket, (ip, port)) = self.socket.accept()
                    self.isConnected = True
                    print("Client {}:{} connected".format(ip, port))
                except socket.timeout:
                    continue
            else:
                try:
                    self.handle()
                except socket.timeout:
                    continue

        self.isConnected = False
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print('Socket closed, bye !')

    def stop(self):
        # self.isConnected = False
        self.isRunning = False
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.ip, self.port))
        # self.socket.close()


# Receiving data from client
class InputSocket(SocketServer):
    def __init__(self, ip: str, port: int, callback):
        SocketServer.__init__(self, ip, port)
        self.callback = callback

    def handle(self):
        msg = self.socket.recv(1024)
        if msg == b'':
            self.stop()
        else:
            self.callback(msg)
            print('Data received')


# Sending data to client
class OutputSocket(SocketServer):
    def __init__(self, ip, port):
        SocketServer.__init__(self, ip, port)
        self.sending_list = []

    def send(self, data):
        if self.isConnected:
            self.socket.send(data)
            print('Data sent')
        else:
            print('No client connected')
