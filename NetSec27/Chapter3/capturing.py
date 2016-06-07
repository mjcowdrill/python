#!/usr/bin/python

import pcapy
import sys
from pprint import pprint as pp
from struct import pack, unpack
from time import sleep
from socket import gethostbyaddr

devs = pcapy.findalldevs()
print(devs)

if "wlan0" in devs:
    adapter="wlan0"
else:
    adapter="eth0"

print("adapter=", adapter)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
#cap = pcapy.open_live("eth0", 65536 , 1 , 0)
cap = pcapy.open_live(adapter, 65536 , 1 , 0)
sleep(1)

#z = ("cc", "3d", "82", "08", "8e", "dc") 
macs = []
ips  = []

count = 1
while True:
    #sys.stdout.write(".")

    try:
        (header, payload) = cap.next()
    except:
        (header, payload) = (None, None)
        sleep(1)

    if payload and len(payload) > 0:
        ipheader   = unpack("!BBHHHBBH4s4s", payload[14:34])
        timetolive = ipheader[5]
        protocol   = ipheader[6]

        a1 = payload[:6]
        a2 = payload[6:12]
        y  = ".".join([ "%.2x" % ord(x) for x in a1 ])
        if y not in macs:
            macs.append(y)
            print y, timetolive, protocol
        y  = ".".join([ "%.2x" % ord(x) for x in a1 ])
        if y not in macs:
            macs.append(y)
            print y, timetolive, protocol
        y  = ".".join([ "%d" % ord(x) for x in ipheader[8] ])
        if y not in ips:
            host = ""
            try:
                host = gethostbyaddr(y)
            except:
                host = "unknown"
            ips.append(y)
            print y, host
#       if z == x:
#           print "YAY1"
#           exit(0)
#       if z == x:
#           print "YAY2"
#           exit(0)
#       print x
#       count = count + 1
