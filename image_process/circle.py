#!/usr/bin/python3

# importing libraries
import cv2
import numpy as np
import math

# reading the image
img = cv2.imread('cat2.jpg',1)
#print(np.shape(img))

#take center and radius of the circle as input
h = int(input('Enter h:- '))
k = int(input('Enter k:- '))
r = int(input('Enter r:- '))
#cv2.circle(img,(200,272),(50),(255,255,0),1)

# create a blank image
blank = np.zeros((600,475,3))
cv2.imwrite('blank_circle.jpg',blank)

# read that blank image
second_image = cv2.imread('blank_circle.jpg',1)


# initalixing the loop for cropping the image
for i in range(h-r,h+r):  # for x range
	temp_x = i-h
	temp = int(math.sqrt((r**2)-(temp_x**2)))  # solving the general circle equation
	temp1 = k+temp
	temp2 = k-temp
	for j in range(temp2,temp1):
		second_image[i][j][0] = img[i][j][0]
		second_image[i][j][1] = img[i][j][1]   #  copy that cropped part in another image
		second_image[i][j][2] = img[i][j][2]
		
		img[i][j][0] = 0
		img[i][j][1] = 0	#  remove the cropped part from main image
		img[i][j][2] = 0

cv2.imwrite('ans.jpg',second_image)
cv2.imshow('main',second_image)
cv2.imshow('main1',img)

cv2.waitKey(0)
cv2.destroyAllWindows()




