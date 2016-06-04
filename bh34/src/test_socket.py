from mjc.mjcSocket import *

mjcSocket = mjcSocket()

def test_send_returns_length():
   assert 4 == mjcSocket.send("test") 

def test_receive_returns_length():
   assert 4 == len(mjcSocket.receive())
