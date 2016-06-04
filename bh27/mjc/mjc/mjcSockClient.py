"""
This is a wrapper class for socket client
"""

import socket

class mjcSockClient():

    # @property
    # def host(self):
    #     return self._host
    #
    # @property
    # def port(self):
    #     return self._port

    def __init__(self, _socket):
        self._socket = _socket


    def isEmpty(self):
        return True

    def put(self, _msg):
        self._socket.send(_msg)

        return True


    def take(self, _msgLen = 2048):

        if not self._socket:
            return ""

        chunks      = []
        bytes_recd  = 0

        while bytes_recd < _msgLen:

            chunk = None

            try:
                chunk = self._socket.recv(min(_msgLen - bytes_recd, 2048))

            except:
                break

                # if chunk == '':
                #     break #raise RuntimeError("socket connection broken")
            if chunk:

                chunks.append(chunk)

                bytes_recd = bytes_recd + len(chunk)

            if not chunk:
                break

        return ''.join(chunks)

    def len(self):
        return 0

    def shutdown(self):
        self._socket.close()

def createSender(_host, _port):

    from time import sleep

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((_host, _port))
    x = mjcSockClient(sock)

    sleep(1)

    return x


if __name__ == "__main__":
    x = 1
