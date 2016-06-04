#!/home/mjc/Desktop/python/envs/bh27/bin/python2.7

import time

def follow(thefile, target):
    print "follow"
    #thefile.seek(0,2)   # goto end of file
    while True:
        print ".",
        line = thefile.readline()
        if not line:
            time.sleep(0.1)   # sleep briefly
            continue
        target.send(line)


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

@coroutine
def printer():
    while True:
        line = (yield)
        print line,


if __name__ == "__main__":
    print "Hi"

    f = open("test_cofunc.py")
    if not f:
        raise "error"

    follow(f, printer())
    """f.seek(0,2)   # goto end of file
    #while True:
        print ".",
        line = f.readline()
        if not line:
            time.sleep(0.1)   # sleep briefly
            continue
        else:
            print(line) """
