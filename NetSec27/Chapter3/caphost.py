#!/usr/bin/python

import pcapy
import sys
from pprint import pprint as pp
from struct import pack, unpack
from time import sleep
from socket import gethostbyaddr

def get_ip(b):

    try:
        ip = ".".join([ "%d" % ord(x) for x in b ])
    except:
        ip = ""

#   if not ip:
#       print("Cant find ip for ", b)

    return ip

def get_host(x):
    try:
        h = gethostbyaddr(x)
    except:
        h = ""
#   if not h:
#       print("Cant find host for ", x)
    if type(h) == tuple:
        h = h[0]
        if "amazonaws" in h:
            return ""
        h = h.split(".")[-3:]
        h = ".".join(h)
    return h

devs = pcapy.findalldevs()
print(devs)

if "wlan0" in devs:
    adapter="wlan0"
else:
    adapter="eth0"

print("adapter=", adapter)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
cap = pcapy.open_live(adapter, 65536 , 1 , 0)

#z = ("cc", "3d", "82", "08", "8e", "dc") 
hosts  = []

count = 1
while True:

    try:
        (header, payload) = cap.next()
    except:
        sleep(0.25)
        (header, payload) = (None, None)

    if payload and len(payload) > 0:
        ipheader   = unpack("!BBHHHBBH4s4s", payload[14:34])
        timetolive = ipheader[5]
        protocol   = ipheader[6]
        source     = ipheader[8]
        destination= ipheader[9]

        source       = get_ip(source)
        source       = get_host(source)

        destination  = get_ip(destination)
        destination  = get_host(destination)

        if (source and source not in hosts) or (destination and destination not in hosts):
            if  source and source not in hosts:
                hosts.append(source)
            if  destination and destination not in hosts:
                hosts.append(destination)

            if source or destination:
               print("{} {} <=> {}".format(protocol, source, destination))

