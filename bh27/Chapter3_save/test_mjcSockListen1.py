import pytest
import mjcSockListen1
import mjcMsgQSocket
import mjcMsgQ
import mjcIMsg

host = "127.0.0.1"
port = 62029

@pytest.fixture
def m_class():
    global host, port

    (q1, q2) = (mjcMsgQ.mjcMsgQ(), mjcMsgQ.mjcMsgQ())

    x = mjcSockListen1.create(q1, q2, host, port)

    return x

def test_create_created(m_class):

    global host, port

    # (host, port) = ("127.0.0.1", 62029)
    # qIn         = mjcMsgQ.mjcMsgQ()
    # qOut        = mjcMsgQ.mjcMsgQ()

    # server      = mjcSockListen1.create(qIn, qOut, host, port)

    assert m_class != None

    client      = mjcMsgQSocket.createSender(host, port)

    msg         = mjcIMsg.mjcMessage1("ABC")
    client.put(msg)

    client.shutdown()

    m_class.shutdown()

if __name__ == "__main__":

    x = m_class()

    test_create_created(x)


