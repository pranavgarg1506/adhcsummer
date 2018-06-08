#! /usr/bin/python3

import cv2

def create_image_diff(x,y,z):
	diff1 = cv2.absdiff(x,y)
	diff2 = cv2.absdiff(y,z)
	diff3 = cv2.bitwise_and(diff1,diff2)
	return diff3


# to complete these functions one tym only
cap = cv2.VideoCapture(0)

img1 = cap.read()[1]
img2 = cap.read()[1]
img3 = cap.read()[1]

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

while 1:
	diff = create_image_diff(gray1,gray2,gray3)
	thresh = cv2.threshold(diff, 7, 255, cv2.THRESH_BINARY)[1]
	#diff = create_image_diff(img1,img2,img3)
	
	thresh1 = cv2.dilate(thresh, None, iterations=1)	

	cv2.imshow('diff',thresh1)

	frame = cap.read()[1]
	gray1 = gray2
	gray2 = gray3
	gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#img1 = img2
	#img2 = img3
	#img3 = frame
	cv2.imshow('main',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
