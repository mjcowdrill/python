#!/usr/bin/python

import struct
import binascii

values = (3, 'ab', 2.7000000000000000000000)
print 'Original values:', values

endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network'),
    ]

for code, name in endianness:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print
    print 'Format string  :', s.format, 'for', name
    print 'Uses           :', s.size, 'bytes'
    print 'Packed Value   :', binascii.hexlify(packed_data)
    print 'Unpacked Value :', s.unpack(packed_data)

a   = "402ccccd";
b   = binascii.unhexlify(a)
s2  = struct.Struct("!f")
c   = s2.unpack(b)
print "c=", c
 
#packed_data = s.pack(*values)
a   = packed_data[6:]
#s2  = struct.Struct("!f")
c   = s2.unpack(a)
print "c=", c
