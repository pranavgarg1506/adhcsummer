#!/usr/bin/env   python

import numpy as np
import socket
import time
import thread
import os


my_ip="192.168.43.168"  # use of the sender ip
port=8888   # this no should be > 6000

                     #ipv4        UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# create a socket argument s

s.bind((my_ip,port))

def send():
    while 1:
        data_msg=raw_input("")
        s.sendto(data_msg,('192.168.43.187',port))   ## use of receiver ip


def rec():
    while 1:
        y = s.recvfrom(1000)
        print y[0]
        #os.system('espeak')

thread.start_new_thread(send,())
thread.start_new_thread(rec,())

while 1:
    pass


