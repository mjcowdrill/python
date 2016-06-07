#!/usr/bin/python

import pcapy
import sys
from pprint import pprint as pp
from struct import pack, unpack

devs = pcapy.findalldevs()
print(devs)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
#cap = pcapy.open_live("eth0", 65536 , 1 , 0)
cap = pcapy.open_live("wlan0", 65536 , 1 , 0)

#z = ("cc", "3d", "82", "08", "8e", "dc") 
z = []

count = 1
while True:
    #sys.stdout.write(".")
    (header, payload) = cap.next()
    if payload and len(payload) > 0:
        ipheader   = unpack("!BBHHHBBH4s4s", payload[14:34])
        timetolive = ipheader[5]
        protocol   = ipheader[6]

        a1 = payload[:6]
        a2 = payload[6:12]
        y  = ".".join([ "%.2x" % ord(x) for x in a1 ])
        if y not in z:
            z.append(y)
            print y, timetolive, protocol
        y  = ".".join([ "%.2x" % ord(x) for x in a1 ])
        if y not in z:
            z.append(y)
            print y, timetolive, protocol
#       if z == x:
#           print "YAY1"
#           exit(0)
#       if z == x:
#           print "YAY2"
#           exit(0)
#       print x
#       count = count + 1
