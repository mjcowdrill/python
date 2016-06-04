"""
This is a type of mjcActive object that receives 1 and sends 1 mjcIMsg object via a socket

 It doesnt provide a way to send data to the socket, this must be done separately, eg using mjcMsgSocket

 It optionally stores the data in the 2 mjcMsgQ associated with the parent mjcActive class
"""


import socket

import mjcMsgActive

from mjcIMsg import mjcMessage1

class mjcMsgSockServ1(mjcMsgActive.mjcMsgActive):

    def __init__(self, _host, _port):

        mjcMsgActive.mjcMsgActive.__init__(self)

        # self.qIn(_qIn)
        # self.qOut(_qOut)

        # create an INET, STREAMing socket
        self._serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._host          = _host
        self._port          = _port


    #The dispatch loop: pump messages until done
    def _run(self):

        # bind the socket to a public host,

        print("Bind to {}/{}".format(self._host, self._port))

        self._serversocket.bind((self._host, self._port))

        # become a server socket
        self._serversocket.listen(1)

        (self._clientsocket, self._address) = self._serversocket.accept()
        # now do something with the clientsocket

        if not self._clientsocket:
            return

        # just print out what the client sends
        request = self._clientsocket.recv(1024)

        print "[*] Received: %s" % request

        if self.qIn():
            self.qIn().put(mjcMessage1("{}".format(request)))

        if self._clientsocket:
            print("getpeername {}".format(self._clientsocket.getpeername()))

        # send back a packet
        ack = "ACK!"
        # ack = None

        if ack:
            self._clientsocket.sendall(ack)

        if ack and self.qOut():
            self.qOut().put(mjcMessage1(ack))

        if self._clientsocket:
            self._clientsocket.close()
            self._clientsocket = None

        if self._serversocket:
            self._serversocket.close()
            self._serversocket = None

        print("run finished")

# Start everything up, using Run as the thread mainline
def create(_qIn, _qOut, _host, _port):

    from time import sleep

    if not _qIn or not _qOut:
        raise "Please define queue"

    c = mjcMsgSockServ1(_host, _port)

    c.qIn(_qIn)
    c.qOut(_qOut)

    # self._thread    = threading.Thread(None, self.run)

    c._start()

    sleep(1)

    return c
