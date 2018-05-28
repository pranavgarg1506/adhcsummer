#!/usr/bin/env   python

import numpy as np
import socket
import time
import matplotlib.pyplot as plt

rec_ip="127.0.0.1"  # use of the receiver ip or ip 127.0.0.1
port=8888   # this no should be > 6000

			#ipv4		UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# create a socket argument s

s.bind((rec_ip,port))  # binding of port and ip


timeout1 = time.time() + 60*(.25)               # to set the timer
#timeout2 = time.time() + 60*(.50)

# data_list=[]       # to print the msg given in certain time
hi_count1=0			# word count
hello_count1=0			# word count

#hi_count2=0
#hello_count2=0

#while timeout2 > time.time():
	

while timeout1 > time.time() :   			# to count the words in the timeout interval
	data=s.recvfrom(1000)
	#data_list.append(data[0])
	if data[0]=='hi':
		hi_count1=hi_count1+1
	elif data[0]=='hello':
		hello_count1=hello_count1+1


	#if data[0]=='hi':
	#	hi_count2=hi_count2+1
	#elif data[0]=='hello':
	#	hello_count2=hello_count2+1


print hi_count1,hello_count1

#print hi_count2,hello_count2




plt.bar('hi',hi_count1,label="hi-used",color="r")
plt.bar('hello',hello_count1,label="hello-used",color="b")

#plt.bar('hi',hi_count2,label="hi-used",color="r")
#plt.bar('hello',hello_count2,label="hello-used",color="b")
plt.show()







