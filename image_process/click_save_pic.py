#!/usr/bin/python3

import cv2
import numpy as np

cam = cv2.VideoCapture(0)
i=0
while cam.isOpened:
	status,frame = cam.read()
	cv2.imshow('lololol',frame)
	# use only 0 in the waitKey argument then only it will wait for to click the pic
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.destroyAllWindows(0)
		break
	res = 'lolol'+str(i)+'.jpg'
	cv2.imwrite(res,frame)
	cv2.destroyAllWindows()
	i=i+1








