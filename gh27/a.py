#!/usr/bin/python


# Python 3
# a,b,*rest = "abcdef"
# print("rest={}".format(rest))

def fun1(a=None, b=None):
    print("fun1={}".format(a))


b = (1,2,3)

#fun1(b)
fun1(4,5)


def fun2(*a):
    print("fun2={}".format(a))

#fun2(b)
fun2(4,5,6)

def fun3(**a):
    print("fun3={}".format(a))

# fun3({"a":1, "b":2})


def f4(a, b, k1='k1', k2='k2',
       *args, **kwargs):
    print('a: {!r}, b: {!r}, '
        'k1: {!r}, k2: {!r}'
        .format(a, b, k1, k2))
    print('args:', repr(args))
    print('kwargs:', repr(kwargs))
    #print('kwargs:', repr(sorted(kwargs)))

f4(1,2,3,4,5,key1=6, key2=7)
