#!/usr/bin/python3

# load libraries
import cv2
import numpy as np

# load both the images in img and img1
img = cv2.imread('random.jpg',1)
img1 = cv2.imread('cat1.jpg')

#a = np.zeros((1000,1000,3))

y = img[200:300,320:420,0:3]	# copy a small part in another variable
img1[100:200,100:200,0:3] = y	# copy that variable into second image


cv2.imshow('try_1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()




