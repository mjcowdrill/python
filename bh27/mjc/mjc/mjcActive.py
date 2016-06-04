"""
Active object that creates a thread to manage two mjcMsgQ's for receive and send

"""

from threading import Thread


# import thread

class mjcActive():

    # @property
    # def thread(self):
    #     return self._thread


    #Start everything up, using Run as the thread mainline
    def __init__(self):

        # t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
        # t.start()

        self._thread    = None
        self._DONE      = "done!"


    def _start(self):

        self._thread =  Thread(target=self._run, name="Thread1")

        return self._thread.start()


    #The dispatch loop: pump messages until done
    def _run(self):
        pass

    # Enqueue a message
    def send(self, _msg):
        pass

    # Shut down: send sentinel and wait for queue to drain
    def shutdown(self):

        if not self.isAlive():
            return

        self.send(self._DONE)

        self._thread.join()


    def isAlive(self):
        if not self._thread:
            return False
        return self._thread.isAlive()

