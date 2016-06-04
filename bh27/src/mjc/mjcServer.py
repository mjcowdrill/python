from mjc.mjcSockClient import *

class mjcServer():

    @property
    def socket(self):
        return self.socket

    @property
    def host(self):
        return self.host

    @property
    def port(self):
        return self.port

    def open(self, host="127.0.0.1", port=80):

        self.socket = mjcSockClient()
        self.host   = host
        self.port   = port

        self.socket.listen(self.host, self.port, 5)
        self.socket, addr = self.socket.accept()

        return self.socket

    def receive(self):

        if not self.socket:
            raise "Please open the server first"

        return self.socket.receive()
