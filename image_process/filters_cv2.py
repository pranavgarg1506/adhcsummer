#!/usr/bin/python3

import cv2


# to blur the image
#img = cv2.imread('cat2.jpg',1)
#img1 = cv2.blur(img,(1,1))
#cv2.imshow('main',img1)


# GAUSSIAN BLUR
#img = cv2.imread('cat2.jpg',1)
#img1 = cv2.GaussianBlur(img,(	23,25	),50,500)      # (23,23)____ this must be positive and odd 50____Xsigma    500________ysigma
			#    kernel size
#cv2.imshow('main',img1)


#  MEDIAN BLUR
#img = cv2.imread('cat2.jpg',1)
#img1 = cv2.medianBlur(img,99)  #  99 is KSIZE AND should be positive and odd  it is a linear value
#cv2.imshow('main',img1)


# BILATERAL FILTER
img = cv2.imread('cat2.jpg',1)
img1 = cv2.bilateralFilter(img,1,50,150)	#________- 1 =filter size  and 50,150 = sigma values
cv2.imshow('main',img1)




cv2.waitKey(0)
cv2.destroyAllWindows()
