import pytest

import mjcMsgQSocket
import mjcIMsg

# @pytest.fixture
# def m_class():
#     return mjcMsgQSocket.create()

# def test_take(m_class):
#
#     #done    = mjcIMessage.done()
#
#     x = m_class.take()
#
#     assert isinstance(x, mjcIMessage.mjcMessage1)
#
#     y = x.body()
#
#     assert "done" == y


def _test_take1_OK(m_class):

    xBody       =   "ABC"

    msg         =   mjcIMsg.mjcMessage1(xBody)

    assert True ==  m_class.put(msg)

    x = m_class.take()

    assert isinstance(x, mjcIMsg.mjcMessage1)

    assert xBody == x.body()


def _test_take2_Fail(m_class):

    xBody       =   "ABC"

    msg         =   mjcIMsg.mjcMessage1(xBody)

    assert True ==  m_class.put(msg)

    x = m_class.take()
    x = m_class.take()

    assert None == x

