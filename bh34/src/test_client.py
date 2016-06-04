from  mjc.mjcClient import *

mjcClient = mjcClient()

host = "127.0.0.1"
port = 9999

def test_open_returns_socket():
    mjcSocket = mjcClient.open(host, port)
    assert None != mjcSocket

def test_send_returns_length():
    len = mjcClient.send("test")
    assert 4 == len
