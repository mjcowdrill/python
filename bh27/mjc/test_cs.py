#!/home/mjc/Desktop/python/envs/bh27/bin/python2.7

from mjc.mjcSockClient import createSender
from mjc.mjcSockServer import create

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start


# class EchoServer():
#
#     def __init__(self, _host, _port):
#         self._host          = _host
#         self._port          = _port
#         self._serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self._serversocket.bind((self._host, self._port))
#         self._serversocket.listen()
#
#     def receive():
#         (self._clientsocket, self._address) = self._serversocket.accept()
#         request = self._clientsocket.recv(1024,)
#         self._clientsocket.sendall(request)

def test_can_receive():

    host = "127.0.0.1"
    port = 62021

    server  = create(host, port)

    client  = createSender(host, port)

    client.put("A")

    ret =  client.take()

    server.shutdown()

    assert "A" == ret


if __name__ == "__main__":

    test_can_receive()
