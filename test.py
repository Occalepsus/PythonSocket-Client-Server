import sys

from Client.ClientCommunication import *

cli0 = ClientCommunication('localhost', 0, 1, int(sys.argv[1]), lambda msg: print("0 received from 1 : " + str(msg)))
cli1 = ClientCommunication('localhost', 1, 0, int(sys.argv[1]), lambda msg: print("1 received from 0 : " + str(msg)))

cli0.start()
cli1.start()

cli0.send(b"0: Hello")
cli1.send(b"0: How are you bro ?")

cli0.stop()
cli1.stop()
