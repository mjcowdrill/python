import mjcIMsg

class mjcMsgQ():

    def __init__(self):

        self._storage = []

    def isEmpty(self):

        return len(self)

    
    def put(self, _mjcIMessage):

        self._storage.append(_mjcIMessage)

        return True


    def take(self):

        if len(self._storage) > 0:
            return self._storage.pop()

        return None

    def len(self):
        if not self._storage:
            return 0
        return len(self._storage)