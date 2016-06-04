import mjcActive
import socket
import mjcMsgQSocket
import time
import mjcIMsg

class mjcSocketListenerQ(mjcActive.mjcMsgActive):

    def __init__(self, _qIn, _qOut, _host, _port):

        mjcActive.mjcMsgActive.__init__(self)

        self.qIn(_qIn)
        self.qOut(_qOut)

        # create an INET, STREAMing socket
        self._serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._host          = _host
        self._port          = _port

    def send(self, msg):

        # global host, port

        client = mjcMsgQSocket.createSender(self._host, self._port)

        # x = mjcIMsg.mjcMessage1(msg.body)

        client.put(msg)

        client.shutdown()

    #The dispatch loop: pump messages until done
    def _run(self):

        # bind the socket to a public host,

        self._serversocket.bind((self._host, self._port))

        # become a server socket
        self._serversocket.listen(1)

###
        while True:

            print("while-")

            (self._clientsocket, self._address) = self._serversocket.accept()
            # now do something with the clientsocket

            if not self._clientsocket:
                print("No socket accepted")
                break

            if not self._qIn:
                raise "msgQueue not defined"

            request = self._clientsocket.recv(1024,)
            msgPtr  = mjcIMsg.mjcMessage1(request)

            if msgPtr:
                self.body.append(msgPtr.body)
                #self._x = True

                ret = msgPtr.execute()

                if ret and self._qOut:
                    self._qOut.put(ret)

                if msgPtr.body == self._DONE.body:
                    break

            time.sleep(0.25)
###

        # just print out what the client sends
        # request = self._clientsocket.recv(1024)

        # print "[*] Received: %s" % request
        # self._qIn.put("{}".format(request))

        # send back a packet
        # self._clientsocket.send("ACK!")
        # print self._clientsocket.getpeername()
        if self._clientsocket:
            self._clientsocket.close()

        if self._serversocket:
            self._serversocket.close()

        print("run finished")

# Start everything up, using Run as the thread mainline
def create(_qIn, _qOut, _host, _port):

    if not _qIn or not _qOut:
        raise "Please define queue"

    c = mjcSocketListenerQ(_qIn, _qOut, _host, _port)

    # self._thread    = threading.Thread(None, self.run)

    c._start()

    return c