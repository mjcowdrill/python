from mjc import mjcIMsg
from mjc import mjcMsgActive
from mjc import mjcMsgQ

import pytest

# @pytest.fixture
    # def m_queue():
    #     return mjcMsgQueue.mjcMsgQueue()

def create_active():
    qIn     = mjcMsgQ.mjcMsgQ()
    qOut    = mjcMsgQ.mjcMsgQ()
    x = mjcMsgActive.create(qIn, qOut)
    return x

@pytest.fixture
def m_class():
    return create_active()

def test_create_created(m_class):

    assert None != m_class

    if m_class:
        m_class.shutdown()


def test_done_stops_process(m_class):

    from time import sleep

    x       = mjcIMsg.mjcMessage1("ABC")

    m_class.send(x)

    x       = mjcIMsg.done()

    m_class.send(x)

    sleep(1)

    a       = m_class.isAlive();

    m_class.shutdown()

    assert a == False


def test_run_msg1_leavesQueueEmpty(m_class):

    xBody       = "ABC"

    msg         = mjcIMsg.mjcMessage1(xBody)

    y           = m_class.send(msg)

    msg         = mjcIMsg.done()

    y           = m_class.send(msg)

    m_class.shutdown()

    z           = m_class.qIn()
    a1          = z.take()

    if (a1):
        a1 = a1.body

    assert a1  == None


    # assert 0 == z

    # x = m_queue.take()
    #
    # assert None == x


if __name__ == "__main__":
    x = create_active()
    # test_create_created(x)
    test_run_msg1_leavesQueueEmpty(x)
