
class TT(object):
    def __getattr__(self, item): return 23

import sys

sys.modules[__name__] = TT()