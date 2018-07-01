#!/usr/bin/python3

import cv2

'''
# main URL = "https://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html"

# GLOBAL THRESHOLD(THRESHOLD):-
	# argument----  [grayscale_image,threshold value,maxval(value to be given if pixe val > threshold),4th argument]

# url about argument 4 :- "https://docs.opencv.org/2.4/doc/tutorials/imgproc/threshold/threshold.html"
img = cv2.imread('cat1.jpg',1)
gray1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


lol1,thresh1 = cv2.threshold(gray1,190,205,cv2.THRESH_BINARY)
lol2,thresh2 = cv2.threshold(gray1,190,205,cv2.THRESH_BINARY_INV)
lol3,thresh3 = cv2.threshold(gray1,190,205,cv2.THRESH_TRUNC)
lol4,thresh4 = cv2.threshold(gray1,190,205,cv2.THRESH_TOZERO)
lol5,thresh5 = cv2.threshold(gray1,190,205,cv2.THRESH_TOZERO_INV)


cv2.imshow('main1',thresh1)
cv2.imshow('main2',thresh2)
cv2.imshow('main3',thresh3)
cv2.imshow('main4',thresh4)
cv2.imshow('main5',thresh5)

'''
# ADAPTIIVE THRESHOLD
'''
img = cv2.imread('cat1.jpg',1)
img1 = cv2.medianBlur(img,5)
img2 = cv2.adaptiveThreshold(img1,200,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow('main',img2)
'''



#OTSU THRESHOLD

img = cv2.imread('hi3.jpg',1)
gray1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lol1,thresh1 = cv2.threshold(gray1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('main',thresh1)
print(lol1)	# print the threshold value calculated by OTSU ALGO

cv2.waitKey(0)
cv2.destroyAllWindows()	

