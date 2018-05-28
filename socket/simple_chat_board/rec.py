#!/usr/bin/env   python

import numpy as np
import socket
import time

rec_ip="127.0.0.1"  # use of the receiver ip or ip 127.0.0.1
port=8888   # this no should be > 6000

			#ipv4		UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# create a socket argument s

s.bind((rec_ip,port))  # bind the ip and port  it should be tupple

while 1:
	msg_rec=s.recvfrom(1000)
	print msg_rec
	data_msg=raw_input("Enter the msg to reply:- ")
	s.sendto(data_msg,(msg_rec[1]))
