from socket import *

class mjcSocket():

#   @property
#   def socket():
#       return self.socket

    def open(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

#   def bind(self, host, port):
#       pass

    def send(self, msg):
        return len(msg)
        
    def receive(self):
        buffer = ""
        while 1:
            data = self.socket.recv(1024)
            if not data:
                break
            else:
                buffer += data

        return buffer
        
    def accept(self):
        return (mjcSocket(), "address")
        
    def listen(self, host, port, timeout):
        self.socket.bind((host,port))
        self.socket.listen(timeout)
        socket, addr = self.socket.accept()
        return (socket, addr)

