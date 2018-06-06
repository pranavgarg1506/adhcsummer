#!/usr/bin/python3

import cv2
import time
import numpy as np


def call_camera():
	i=0
	data=[]
	while 1:
		
		# start the webcam and read the data into the frame
		cap = cv2.VideoCapture(0)
		frame = cap.read()[1]
		# convert the image into grayscale
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		# save all the data into the data vriable
		data.append(gray_image)
		# save the data into the csvfile  _______________________________________-    PENDING



		cv2.imshow('lolol',gray_image)
		# code for saving the image in a loopy manner
		res = 'image'+str(i)+'.jpg'
		cv2.imwrite(res,gray_image)
		if cv2.waitKey(0) & 0xFF == ord('q'):
			break
		cv2.destroyAllWindows()
		# release the camera so that it can be again started
		cap.release()
		# camera wil start after 2 seconds 
		time.sleep(2)
		i=i+1
'''
def cal():
	i=0
	diff=[]
	main_diff=[]
	for i in range(0,(len(data)-1)):
		diff[i] = cv2.subtract(data[i],data[i+1])	
	for i in range(0,(len(data)-1)):
		
'''























call_camera()

