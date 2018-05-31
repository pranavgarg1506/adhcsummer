#!/usr/bin/python3


# COLOR  ::::::: BGR
import cv2
import numpy as np				

# to read the image or create an image of yourself
img1 = cv2.imread('cat.jpg',1)   #_____________ READ the image
img2 = np.zeros((1400,1400,3))	 #_____________ Create your Own Image


# To cut an image
img3 = img1[300:1200,300:2200]
img4 = img2[0:600,0:700]

# to draw something on image
cv2.line(img3,(100,100),(200,200),(0,0,255),3)		#_________________	LINE
#      _image first     second    color     width
cv2.rectangle(img3,(100,100),(200,200),(0,255,0),5)	#_________________	RECTANGLE

cv2.circle(img3,(200,200),100,(255,0,0),12)		#_________________	CIRCLE



# to save the image locally
cv2.imwrite('lol.jpg',img3)

# to show the image
cv2.imshow('image',img3)

# to waut for the pic not to get deleted
cv2.waitKey(0)		# 0 for infinite time  time is In ms


#  to destroy one named window
#cv2.destroyWindows('image')
cv2.destroyAllWindows()
