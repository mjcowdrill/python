from struct import pack, unpack
from binascii import hexlify, unhexlify

s = "a"
print(type(s))

u = unicode(s)
print(type(u))

b=pack("h", 163)
print(type(b))
print (b)

print (hexlify(b))

print (int("a300", 16))

b=pack("i", int("a300", 16))
print (b)

print (pack("h", int("a3", 16)))

z = unhexlify("a3")
print ("type_z=", type(z))

print ("bytes=", bytes(163))

print ("%c" % 163)


#for i in range(100):
#    print 163+i, pack("h", 163+i)
    

