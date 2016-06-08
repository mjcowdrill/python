#!/usr/bin/python

import pcapy
import sys
from pprint import pprint as pp
from struct import pack, unpack
from time import sleep
#from socket import gethostbyaddr
from binascii import hexlify, unhexlify

devs = pcapy.findalldevs()
print(devs)

seek = ("eth1", "eth0", "wlan0")
for x in seek:
    if x in devs:
        adapter=x
        break

print("adapter=", adapter)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
cap = pcapy.open_live(adapter, 65536 , 1 , 0)

vers  = {}

def loopit():
    
    count = 1
    while True:
    
        try:
            (header, payload) = cap.next()
        except:
            sleep(0.25)
            (header, payload) = (None, None)
    
        if payload and len(payload) > 0:
            ipheader   = unpack("!BBHHHBBH4s4s", payload[14:34])
    
            #ver       = ipheader[0] >> 4
            ver        = ipheader[0] // 16
            ln         = len(payload)
    
            if ver not in vers.keys():
                print(ver, ln, hexlify(payload))
                vers[ver] = ln
            elif vers[ver] < ln:
                vers[ver] = ln


try:
   loopit()
except KeyboardInterrupt:
    print("")
    for i in sorted(vers):
        print(i, vers[i])
    raise
