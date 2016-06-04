import mjcActive
import socket
import mjcMsgQSocket
import time

class mjcSocketListener1(mjcActive.mjcMsgActive):

    def __init__(self, _qIn, _qOut, _host, _port):

        mjcActive.mjcMsgActive.__init__(self)

        self.qIn(_qIn)
        self.qOut(_qOut)

        # create an INET, STREAMing socket
        self._serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._host          = _host
        self._port          = _port


    #The dispatch loop: pump messages until done
    def _run(self):

        # bind the socket to a public host,

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
        self._qIn.put("{}".format(request))

        # send back a packet
        self._clientsocket.send("ACK!")
        print self._clientsocket.getpeername()
        self._clientsocket.close()

        self._serversocket.close()

        print("run finished")

# Start everything up, using Run as the thread mainline
def create(_qIn, _qOut, _host, _port):

    if not _qIn or not _qOut:
        raise "Please define queue"

    c = mjcSocketListener1(_qIn, _qOut, _host, _port)

    # self._thread    = threading.Thread(None, self.run)

    c._start()

    return c