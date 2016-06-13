#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

#from scapy.all import *
from scapy.all import Ether, IP, TCP, sendp

macaddr = "08:05:81:2d:23:94"
#ipaddr  = "192.168.1.236"
ipaddr  = "192.168.1.7"

ether = Ether(dst=macaddr)
ip    = IP   (dst=ipaddr)
tcp   = TCP()

frame = ether/ip/tcp/"This is my payload"
#frame = Ether(dst="15:16:89:fa:dd:09")/IP(dst="9.16.5.4")/TCP()/"This is my payload"

print(frame)
sendp(frame)
