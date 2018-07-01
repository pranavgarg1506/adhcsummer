#!/usr/bin/python3

# import libraries
import cv2
import numpy as np


	

# load the camera into a variable
cam = cv2.VideoCapture(0)

# to check the width and height  of the current camera
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)


# print the height and width
print('Width:-',width)
print('Height:-',height)

# set the video format
video_format = cv2.VideoWriter_fourcc(*'XVID')

# set the path where to save the video and the buffer rate
video_output = cv2.VideoWriter('lol.avi',video_format,20.0,(int(width),int(height)),True)

while cam.isOpened():
	status,frame = cam.read()
	#bkwas = cv2.inRange(frame,(0,0,40),(255,255,80))
	cv2.imshow('live_frame',frame)
	video_output.write(frame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

print(frame[0][2])
cv2.destroyAllWindows()
cam.release()
