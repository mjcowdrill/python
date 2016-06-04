from struct import pack, unpack
from binascii import hexlify, unhexlify

s = "a"
print("type_a=", type(s))

#u = unicode(s)
#print(type(u))

b=pack("h", 163)
print("pack_h_163=", b)
print ("b=", b)
print("type_b=", type(b))

print ("hexlify_b=", hexlify(b))

print ("int_a300_16=", int("a300", 16))

b=pack("i", int("a300", 16))
print ("pack_i_int_a300_16=", b)

print ("pack_h_int_a3_16=", pack("h", int("a3", 16)))

z = unhexlify("a3")
print("unhexlify_a3=", z)
print("z=", z)
print("%_c_ord_z=",  ("%c" % ord(z)))
#print("%_c_pct_z=",  ("%c" % z))
print ("type_z=", type(z))
print("unpack_c_z=", unpack("c", z))

print("ord_z=", ord(z))
print("str_z=", str(z))

print ("%_c_163=", "%c" % 163)

print ("pack_c_int_a300_16=", pack("c", b'\xa3'))    

utf8="£".encode("utf8")
print("utf8=", utf8)
print("type_utf8=", type(utf8))

unicode=utf8.decode("utf8")
print("type_unicode=", type(unicode))
print("unicode={}.".format(unicode))
      
