

from threading import Thread
import mjcIMsg
import time
import mjcMsgQSocket
# import thread

class mjcActive():

    def qIn(self, _qIn = None):

        if (_qIn != None):
            self._qIn = _qIn

        return self._qIn

    def qOut(self, _qOut = None):

        if (_qOut != None):
            self._qOut = _qOut

        return self._qOut

    # @property
    # def thread(self):
    #     return self._thread

    @property
    def body(self):
        return self._body

    #Start everything up, using Run as the thread mainline
    def __init__(self):

        # t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
        # t.start()

        self.body       = []
        self._thread    = None
        # self._msgPtr  = None
        self._qIn       = None
        self._qOut      = None
        self._DONE      = mjcIMsg.done()   #CONST


    def _start(self):

        self._thread =  Thread(target=self._run, name="Thread1")

        return self._thread.start()

    # def __enter__(self):
    #     return self

    # def someWork(self):
    #     pass
    #
    #
    # def moreWork(self):
    #     pass

    #The dispatch loop: pump messages until done
    def _run(self):

        while True:

            print("-")

            if not self._qIn:
                raise "msgQueue not defined"

            msgPtr = self._qIn.take()

            if msgPtr:
                self.body.append(msgPtr.body)
                #self._x = True

                ret = msgPtr.execute()

                if ret and self._qOut:
                    self._qOut.put(ret)

                if msgPtr.body == self._DONE.body:
                    break

            time.sleep(0.25)


        print("run finished")

    # Enqueue a message
    def send(self, _msg):

        if not _msg:
            raise "Message not defined"

        self._qIn.put(_msg)

        time.sleep(0.25)

        # if _msg.body() == self._done.body():
        #     self._thread.join()

    #Shut down: send sentinel and wait for queue to drain
    def shutdown(self):

        time.sleep(0.25)

        if not self.isAlive():
            self.clearQin()
            return

        self.send(self._DONE)

        self._thread.join()

        self.clearQin()

    def clearQin(self):
        self.qIn().__init__()

    # #Shut down: send sentinel and wait for queue to drain
    # def __exit__(self, type, value, traceback):
    #     self.shutdown()

    def isAlive(self):
        if not self._thread:
            return False
        time.sleep(0.25)
        return self._thread.isAlive()

    def queuedIn(self):
        q = self.qIn()
        if not q:
            return 0
        return q.len()

    def queuedOut(self):
        q = self.qOut()
        if not q:
            return 0
        return q.len()



# Start everything up, using Run as the thread mainline
def create(_qIn, _qOut):

    if not _qIn or not _qOut:
        raise "Please define queue"

    c = mjcActive()

    # self._thread    = threading.Thread(None, self.run)
    c.qIn(_qIn)
    c.qOut(_qOut)

    c._start()

    return c

