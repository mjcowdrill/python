"""
This class defines an interface for "messages" that can be sent between the "mjc" objects
"""

class mjcIMsg:

    pass
    def execute(self):
        pass


    def body(self):
        pass


class mjcMessage1(mjcIMsg):

    @property
    def body(self):
        return self._body

    def __init__(self, _body):
        self.body = _body

    def execute(self):

        if not self.body:
            return mjcMessage1("")

        print("body=" + self.body)

        return mjcMessage1(self.body)


    # def body(self, _body = None):
    #     if (_body != None):
    #         self._body = _body
    #
    #     return self._body


def done():
    return mjcMessage1("done")
