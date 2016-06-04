#!/usr/bin/env python27

import socket
#target_host = "127.0.1.1"
target_host = "192.168.56.1"
target_port = 80

# create a socket object
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 # connect the client
#client.connect((target_host,target_port))

# send some data
#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.sendto("AAABBBCCC", (target_host,target_port))

# receive some data
#response = client.recv(4096)
data, addr = client.recvfrom(4096)

print data
