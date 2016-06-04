import threading

def f1():
    lock = threading.Lock()

    print 'First try :', lock.acquire()
    print 'Second try:', lock.acquire(0)
    print "print this if not blocked..."

    print "--------"

def f2():
    lock = threading.Lock()

    print 'First try :', lock.acquire()
    #print 'Second try:', lock.acquire()  #hangs!

    #print "print this if not blocked..."


def f3():
    lock = threading.RLock()

    print 'First try :', lock.acquire()
    print 'Second try:', lock.acquire(0)    

def f4():
    lock = threading.RLock()

    with lock:

        print "f4 acquired"

        with lock:
            print "f4 acquired again"
        


f3()
f4()
