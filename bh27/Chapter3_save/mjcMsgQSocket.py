import mjcMsgQ
import socket
import mjcIMsg

class mjcMsgQSocket(mjcMsgQ.mjcMsgQ):

    # @property
    # def host(self):
    #     return self._host
    #
    # @property
    # def port(self):
    #     return self._port

    def __init__(self, _socket):
        mjcMsgQ.mjcMsgQ.__init__(self)
        self._socket = _socket


    def isEmpty(self):
        return True

    def put(self, _mjcIMessage):
        self._socket.send(_mjcIMessage.body)

        return True


    def take(self, _msgLen):

        chunks      = []
        bytes_recd  = 0

        while bytes_recd < _msgLen:

            chunk = self.sock.recv(min(_msgLen - bytes_recd, 2048))

            if chunk == '':
                raise RuntimeError("socket connection broken")

            chunks.append(chunk)

            bytes_recd = bytes_recd + len(chunk)

        return mjcIMsg.mjcMessage1(''.join(chunks))

    def len(self):
        return 0

    def shutdown(self):
        # self._socket.shutdown()
        self._socket.close()


def createSender(_host, _port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((_host, _port))
    x = mjcMsgQSocket(sock)
    return x


if __name__ == "__main__":
    x = 1