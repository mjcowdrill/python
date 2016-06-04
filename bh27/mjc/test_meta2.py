#!/home/mark/.virtualenvs/bh27/bin/python2.7

class MyMeta(type):
    def __call__(cls, *args, **kwds):
        print '__call__ of ', str(cls)
        print '__call__ *args=', str(args)
        return type.__call__(cls, *args, **kwds)
    
class MyKlass(object):
    __metaclass__ = MyMeta

    def __init__(self, a, b):
        print 'MyKlass object with a=%s, b=%s' % (a, b)

print 'gonna create foo now...'
foo = MyKlass(1, 2)
