import pytest
import mjcSockListenQ
import mjcMsgQSocket
import mjcMsgQ
import mjcIMsg

host = "127.0.0.1"
port = 62029

@pytest.fixture
def m_class():
    global host, port

    (q1, q2) = (mjcMsgQ.mjcMsgQ(), mjcMsgQ.mjcMsgQ())

    x           = mjcSockListenQ.create(q1, q2, host, port)

    return x


def test_create_created(m_class):

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

    test_create_created(x)


