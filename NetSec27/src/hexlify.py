#!/usr/bin/python

import struct
import binascii

values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values
print 'Format string  :', s.format
print 'Uses           :', s.size, 'bytes'
print 'Packed Value   :', binascii.hexlify(packed_data)

a = binascii.hexlify(packed_data)

packed_data2 = binascii.unhexlify(a)

if packed_data != packed_data2 :
	print "ERROR"
else:
	print "OK"

b = s.unpack(packed_data2)
print "b=", b

cnt=0
a	= ord("1")
print cnt, a, ":"

cnt += 1
a	= ord(" ")
print cnt, a, ":"

cnt += 1
a	= "%.1x" % (ord("1"))
print cnt, a, ":"

cnt += 1
a	= "%.2x" % (ord("1"))
print cnt, a, ":"

cnt += 1
a	= "%.4x" % (ord("1"))
print cnt, a, ":"

cnt += 1
a	= "%.4f" % (ord("1"))
print cnt, a, ":"

print "int-11-16, %x" % int("11", 16)

print "int-11-2, %x" % int("11", 2)

print "int-FF-16, %X" % int("FF", 16)

print "int-FF-16, {0:b}".format(int("FF", 16))

print '%(language)s has %(number)03d quote types.' % {"language": "Python", "number": 2}