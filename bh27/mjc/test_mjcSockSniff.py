from mjc import mjcIMsg
from mjc import mjcSockSniff

import pytest

from mjc import mjcMsgQ

host = "127.0.0.1"
port = 62025

@pytest.fixture
def m_class():
    global host, port

    (q1, q2) = (mjcMsgQ.mjcMsgQ(), mjcMsgQ.mjcMsgQ())

    x           = mjcSockSniff.create(q1, q2, host, port)

    return x


def _test_create_created(m_class):

    global host, port

    # (host, port) = ("127.0.0.1", 62029)
    # qIn         = mjcMsgQ.mjcMsgQ()
    # qOut        = mjcMsgQ.mjcMsgQ()

    # server      = mjcSockListen1.create(qIn, qOut, host, port)

    assert m_class != None

    msg     = mjcIMsg.mjcMessage1("ABC")

    m_class.send(msg)

    msg         = mjcIMsg.done()

    m_class.send(msg)

    m_class.shutdown()


if __name__ == "__main__":

    x = m_class()

    _test_create_created(x)


