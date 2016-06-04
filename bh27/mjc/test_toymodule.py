import mjcToyModule

from struct import pack,unpack

print mjcToyModule.x
print mjcToyModule.y

print bytearray([1,2,3,4])==bytearray(b'\x01\x02\x03\x04')
y = bytearray(b'\x61\x62\x63\x64')
x = bytearray([1,2,3,4])

z = int("0x61", 16)

# print "%s" % str(z)

a = pack("iii", 97, 98, 99)
b = pack("ccc", "a", "b", "c")
c = pack("d", 2.7)
d = pack("25s", "this is a string")
# print struct.pack("hhh", 61,62,3)

print a
print b
print c
print d, "---"

print unpack("d", c)
e = pack("ccc", b"a", b"b", b"c").decode("utf-8")
print "type(e)=", type(e)
print "e=", e
f = unicode("abc")    # in python 3, name unicode is not defined, use str=unicode
print "type(f)=", type(f)
g = str("abc")
print "type(str)=", type(g)
print "type(bytes)", type(b"abc")   #<type 'str'>, (in python 3, this shows <class 'bytes'>
"""

In 3, 'b' strings are <class 'bytes'>, in 2 they are <type 'str'>

In 3 non-b strings are <class 'str'>, in 2 they are <type 'str'>

In 2 if you decode a 'b' OR non-b "str", you get a <type 'unicode'>, in 3 you cannot decode a non-b, and either way, you get a <class 'str'>



"""
