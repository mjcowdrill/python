
from mjc.mjcClient import *
from mjc.mjcServer import *

host = "127.0.0.1"
port = 9999

def test_send_and_receive():
    c = mjcClient()
    s = mjcServer()
    c.open(host, port)

    c.send("test")
    sk = s.open(host, port)
    data = sk.receive()

    assert "test" == data
