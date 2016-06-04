
import socket
import pytest

@pytest.fixture()
def m_class():
    return socket.socket()

def _test_getservbyname(m_class):
    assert 21 == socket.getservbyname("ftp", "tcp")

opts = {"host"        : "localhost"
    ,   "port"        : 80
    ,   "family"      : socket.AF_INET
    ,   "sockType"    : socket.SOCK_STREAM
    ,   "proto"       : 1
    ,   "flags"       : int(1)
    }

def _test_getAddrInfo():
    global opts

    assert opts["flags"] == 1
    assert type(opts["flags"]) == int

    socket.getaddrinfo("localhost", 80, socket.AF_INET, socket.SOCK_STREAM, 1, 1)

    socket.getaddrinfo(opts["host"]
                     , opts["port"]
                     , opts["family"]
                     , opts["sockType"]
                     , opts["proto"]
                     , opts["flags"])
