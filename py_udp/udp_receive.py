#!/usr/bin/env python

'''udp_receive.py--Receives and prints a single UDP packet from the
specified port.

N.B., UDP port must be open in firewall.

Example: udp_receive.py 21566

Kevin Bartlett
2009-03-30

'''

import sys, socket

udpInPort = int(sys.argv[1])
UDPTIMEOUT = 1
udpInBufferLength = 1000

localIP = '' # (Symbolic name meaning the local host)
localAddr = (localIP,udpInPort)

inUdpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
inUdpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#inUdpSocket.settimeout(UDPTIMEOUT)

# ...Bind incoming UDP socket to address of local machine.
inUdpSocket.bind(localAddr)

# Note: I've seen elsewhere that to receive broadcast packets, you
# should bind with one of these two methods:
#   inUdpSocket.bind(("0.0.0.0",udpInPort))
#   inUdpSocket.bind(("<broadcast>",udpInPort))
# However, I've found this isn't necessary.

try:
   udpData = inUdpSocket.recv(udpInBufferLength)
except:
   udpData = []      

# Close incoming UDP socket.        
inUdpSocket.close()

#print 'udpData is ' + str(udpData)
print str(udpData)
