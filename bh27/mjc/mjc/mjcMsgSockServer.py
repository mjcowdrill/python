"""
This is a type of mjcActive object that receives many and sends many mjcIMsg object via a socket

 It also provides a way to send data to the socket, using the send method

 It optionally stores the data in the 2 mjcMsgQ associated with the parent mjcActive class

"""


import socket

import mjcMsgActive
import mjcIMsg
import mjcMsgSocket


class mjcMsgSockServer(mjcMsgActive.mjcMsgActive):

    def __init__(self, _host, _port):

        mjcMsgActive.mjcMsgActive.__init__(self)

        # create an INET, STREAMing socket
        self._serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._host          = _host
        self._port          = _port

    def send(self, msg):

        # global host, port

        client = mjcMsgSocket.createSender(self._host, self._port)

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

            # if not self._qIn:
            #     raise "msgQueue not defined"

            request = self._clientsocket.recv(1024,)
            msg     = mjcIMsg.mjcMessage1(request)

            if msg:

                if self.qIn():
                    self.qIn().put(msg)

                self.body.append(msg.body)
                #self._x = True

                ret = msg.execute()

                if ret and self.qOut():
                    self.qOut().put(ret)

                if msg.body == self._DONE.body:
                    break

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

    from time import sleep

    if not _qIn or not _qOut:
        raise "Please define queue"

    c = mjcMsgSockServer(_host, _port)

    c.qIn(_qIn)
    c.qOut(_qOut)

    # self._thread    = threading.Thread(None, self.run)

    c._start()

    sleep(1)

    return c
