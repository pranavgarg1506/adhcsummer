#!/usr/bin/env   python

import numpy as np
import socket
import time

rec_ip="127.0.0.1"  # use of the receiver ip or ip 127.0.0.1
port=8888   # this no should be > 6000

			#ipv4		UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# create a socket argument s


while 1:
	data_msg=raw_input("Enter the msg:- ")
	s.sendto(data_msg,(rec_ip,port))
	

