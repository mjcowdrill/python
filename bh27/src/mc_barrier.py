import time
from threading import Thread,Semaphore

class Barrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Semaphore(1)
        self.barrier = Semaphore(0)

    def wait(self):
        self.mutex.acquire()
        self.count = self.count + 1
        self.mutex.release()
        if self.count == self.n: self.barrier.release()
        self.barrier.acquire()
        self.barrier.release()

b = Barrier(2)

def func1():
    time.sleep(3)
    #
    b.wait()
    #
    print('Working from func1')
    return 

def func2():
    time.sleep(5)
    #
    b.wait()
    #
    print('Working from func2')
    return    

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()  
