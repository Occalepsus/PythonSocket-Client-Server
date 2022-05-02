import sys
from time import sleep
from signal import *

from ClientChannel import *

cli0 = ClientChannel('127.0.0.1', 0, 1, int(sys.argv[1]), lambda msg: print("0 received from 1 : " + str(msg)))
cli1 = ClientChannel('127.0.0.1', 1, 0, int(sys.argv[1]), lambda msg: print("1 received from 0 : " + str(msg)))


def stop_all():
    print("\nStopping...")
    cli0.stop()
    cli1.stop()
    return


for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
    signal(sig, lambda nb, stack: stop_all())

cli0.start()
cli1.start()

while not cli0.is_connected() and not cli1.is_connected():
    sleep(1)
sleep(2)
cli0.send(b"0: Hello")
cli1.send(b"1: How are you bro ?")

# sleep(2)
#
# cli0.stop()
# cli1.stop()

