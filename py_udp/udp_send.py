#!/usr/bin/env python

'''udp_send.py--Sends a UDP packet containing a string to the
specified host. This program is called by the Matlab routine
py_udp_send.m as a workaround for a problem sending UDP packets using
Peter Rydesater`s TCP/UDP/IP Toolbox under Windows.

Input arguments are target host name or IP address (in string form),
numeric port number and the string to be sent.

Example: python udp_send.py '192.0.34.166' 3333 'Test data'

Kevin Bartlett
2009-03-30

'''

import sys, socket

targetIP = sys.argv[1]
port = sys.argv[2]
data = sys.argv[3]

#print 'targetIP is ' + targetIP
#print 'port is ' + str(port)
#print 'data is ' + data

port = int(port)
targetAddr = (targetIP,port)
outUdpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
outUdpSocket.sendto(data,targetAddr)
outUdpSocket.close()                               


