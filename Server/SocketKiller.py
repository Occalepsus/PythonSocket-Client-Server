import socket
import sys
import traceback


def is_socket_connected(sock):
    try:
        sock.send(b"ping")
        return True
    except:
        return False


class Killer:
    def __init__(self, threads_to_kill):
        self.threads = threads_to_kill

    def __call__(self, signo, frame):
        print('')
        print('Closing threads...')

        for thread_to_end in self.threads:
            try:
                thread_to_end.stop()
                # thread_to_end.shutdown(socket.SHUT_RDWR)
                # thread_to_end.close()
            except Exception as e:
                print(traceback.format_exc())
                print(e)
            thread_to_end.join()

        print('All threads ended')
