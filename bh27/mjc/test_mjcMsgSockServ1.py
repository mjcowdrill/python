from mjc import mjcIMsg
from mjc import mjcMsgQ
from mjc import mjcMsgSockServ1

import pytest

from mjc import mjcMsgSocket

host = "127.0.0.1"
port = 62023

@pytest.fixture
def m_class():
    global host, port

    (q1, q2) = (mjcMsgQ.mjcMsgQ(), mjcMsgQ.mjcMsgQ())

    x = mjcMsgSockServ1.create(q1, q2, host, port)

    return x

def test_create_created(m_class):

    global host, port

    assert m_class != None

    client      = mjcMsgSocket.createSender(host, port)

    msg         = mjcIMsg.mjcMessage1("ABC")
    client.put(msg)
    ack         = client.take()
    if ack and ack.body:
        print("client got ack.body={}".format(ack.body))

    m_class.shutdown()

    m_class = None

    client.shutdown()

    client = None

if __name__ == "__main__":

    x = m_class()

    test_create_created(x)


