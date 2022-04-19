from ServerSockets import *


class ServerConnection:
    def __init__(self, ip: str, a_id: int, b_id: int, con_id: int):
        self.a_id = a_id
        self.b_id = b_id
        self.a_input_socket = InputSocket(ip, 5000 + 100 * a_id + 10 * b_id + con_id, lambda msg: self.send_to_b(msg))
        self.a_output_socket = OutputSocket(ip, 6000 + 100 * a_id + 10 * b_id + con_id)
        self.b_input_socket = InputSocket(ip, 5000 + 100 * b_id + 10 * a_id + con_id, lambda msg: self.send_to_a(msg))
        self.b_output_socket = OutputSocket(ip, 6000 + 100 * b_id + 10 * a_id + con_id)

        print("Created connection {} between {} and {}".format(con_id, a_id, b_id))
        print("Available ports: {} and {}".format(self.a_input_socket.port, self.b_input_socket.port))

    def start(self):
        self.a_input_socket.start()
        self.a_output_socket.start()
        self.b_input_socket.start()
        self.b_output_socket.start()

    def close(self):
        self.a_input_socket.socket.close()
        self.a_output_socket.socket.close()
        self.b_input_socket.socket.close()
        self.b_output_socket.socket.close()

    def join(self):
        self.a_input_socket.join()
        self.a_output_socket.join()
        self.b_input_socket.join()
        self.b_output_socket.join()

    def stop(self):
        self.a_input_socket.stop()
        self.a_output_socket.stop()
        self.b_input_socket.stop()
        self.b_output_socket.stop()

    def shutdown(self, how):
        self.a_input_socket.socket.shutdown(how)
        self.a_output_socket.socket.shutdown(how)
        self.b_input_socket.socket.shutdown(how)
        self.b_output_socket.socket.shutdown(how)

    def send_to_a(self, msg):
        print("Sending to {}: {}".format(self.a_id, msg))
        self.a_output_socket.send(msg)

    def send_to_b(self, msg):
        print("Sending to {}: {}".format(self.b_id, msg))
        self.b_output_socket.send(msg)
