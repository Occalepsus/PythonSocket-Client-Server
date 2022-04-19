from ClientSockets import InputSocket, OutputSocket


class ClientCommunication:
    def __init__(self, host: str, origin_id: int, destination_id: int, con_id: int, callback: callable):
        self.server_ip = host
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.con_id = con_id
        self.input_socket = \
            InputSocket(host, 6000 + origin_id * 100 + destination_id * 10 + con_id, callback)
        self.output_socket = \
            OutputSocket(host, 5000 + origin_id * 100 + destination_id * 10 + con_id)

        print("Created connection {} form client {} to client {} via server {}"
              .format(con_id, origin_id, destination_id, host))

    def start(self):
        self.input_socket.start()
        self.output_socket.start()

    def stop(self):
        self.input_socket.stop()
        self.output_socket.stop()
        self.input_socket.join()
        self.output_socket.join()

    def send(self, msg):
        self.output_socket.send(msg)
