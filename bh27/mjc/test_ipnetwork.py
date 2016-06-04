from mjc import mjcIMsg
from mjc import mjcMsgQ
from mjc import mjcMsgSockServ1
from netaddr import IPNetwork,IPAddress
import socket

import pytest

from mjc import mjcMsgSocket

host = "127.0.0.1"
port = 62022

@pytest.fixture
def m_class():
    global host, port

    (q1, q2) = (mjcMsgQ.mjcMsgQ(), mjcMsgQ.mjcMsgQ())

    x = mjcMsgSockServ1.create(q1, q2, host, port)

    return x

# from ctypes import *

# host to listen on
# host   = "192.168.1.140"
# host   = "192.168.0.187"

# subnet to target
# subnet = "192.168.0.0/16"

subnet = "192.168.1.0/24"

magic_message = "PYTHONRULES!"

def _test_send_dgram(m_class):

    global port

    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message, ("%s" % ip, port))
        except:
            pass

    m_class.shutdown()


if __name__ == "__main__":
    test_send_dgram(m_class())