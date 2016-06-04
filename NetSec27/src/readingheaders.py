#!/usr/bin/python

import pcapy, sys
from struct import *
import time

cap = pcapy.open_live("wlan0", 65536, 1, 0)

while 1:
    (header,payload) = cap.next()
    try:
        if payload and sys.getsizeof(payload) > 13:
            l2hdr = payload[:14]
            if l2hdr and sys.getsizeof(l2hdr) > 13:
                l2data = unpack("!6s6sH", l2hdr)
                srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
                dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[6]), ord(l2hdr[7]), ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
                print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)
    
    # get IP header, which is 20 bytes long
    # then unpack it into what it is
        if payload and sys.getsizeof(payload) > 33:
            ipheader = unpack('!BBHHHBBH4s4s' , payload[14:34])
            timetolive = ipheader[5]
            protocol = ipheader[6]
            print("Protocol ", str(protocol), " Time To Live: ", str(timetolive))
    finally:
        #time.sleep(10)
        print "." ,
        
           
