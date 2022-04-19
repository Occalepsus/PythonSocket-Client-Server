import socket
import sys
import time
from threading import Thread
from signal import *

from ServerConnection import ServerConnection
from SocketKiller import *
from ServerSockets import *


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 CommunicationServerSocket.py <ip address> <connections>")
        sys.exit(1)

    sockets = [ServerConnection(sys.argv[1], int(con[0]), int(con[1]), int(con[2])) for con in sys.argv[2:]]

    for socket in sockets:
        socket.start()

    for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
        signal(sig, Killer(sockets))

# import signal
# import socketserver
# from signal import *
# from struct import *
# import time
#
#
# class MyHandler:
#     def __init__(self, server):
#         self.server = server
#
#     def __call__(self, signo, frame):
#         print('\nClosing server.')
#         server.server_close()
#         print('Server closed, bye !')
#         exit()
#
#
# class MyTCPHandler(socketserver.BaseRequestHandler):
#     """
#     The request handler class for our server.
#
#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """
#
#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
#         time.sleep(10)
#         print(unpack('ic0l', self.data))
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())
#
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 5000
#
#     # Create the server, binding to localhost on port 9999
#     with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#
#         for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
#             signal(sig, MyHandler(123))
#
#         # activates the server
#         server.serve_forever()
