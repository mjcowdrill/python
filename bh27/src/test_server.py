from  mjc.mjcServer import *

mjcServer = mjcServer()

host = "127.0.0.1"
port = 9999

def test_open_returns_socket():
    mjcSocket = mjcServer.open(host, port)
    assert None != mjcSocket

def test_receive_returns_length():
    data = mjcServer.receive()
    assert 4 == len(data)
