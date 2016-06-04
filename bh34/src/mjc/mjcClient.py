from mjc.mjcSocket import *

class mjcClient():

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

        self.socket = mjcSocket()
        self.host   = host
        self.port   = port

        self.socket.open(self.host, self.port)

        return self.socket

    def send(self, msg):

        if not self.socket:
            raise "Please open the client first"

        return self.socket.send(msg)
