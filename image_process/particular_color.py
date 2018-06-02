#!/usr/bin/python3

import  cv2

#  loading image
#img=cv2.imread('redhat.png')

#print(img.shape)
#  only picking  red color range
#  starting  camera  
cap=cv2.VideoCapture(0)
#  checking for  web  cam 
while cap.isOpened():
	# true ,false , image frame 
	status,frame=cap.read()
         #                           starting color, end color range
	
	only_red=cv2.inRange(frame,(0,0,40),(255,255,255))
	only_green=cv2.inRange(frame,(0,0,40),(180,200,200))
	cv2.imshow('window_red',only_red)
	cv2.imshow('window_green',only_green)
	if  cv2.waitKey(1) & 0xFF ==  ord('q') :
		break

cv2.destroyAllWindows()
cap.release()
