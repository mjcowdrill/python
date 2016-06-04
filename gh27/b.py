#!/usr/bin/python

x=1

def f():
    x=2
    print("f={}".format(x))

f()
print("x={}".format(x))

def g():
    global x
    x = 2
    print("g={}".format(x))


g()


print("x={}".format(x))

