#!/usr/bin/python3


# COLOR  ::::::: BGR
import cv2
import numpy as np				

# to read the image or create an image of yourself
img1 = cv2.imread('cat2.jpg',1)   #_____________ READ the image
img2 = np.zeros((1400,1400,3))	 #_____________ Create your Own Image


# To cut an image
img3 = img1[300:1200,300:2200]
img4 = img2[0:600,0:700]

# to draw something on image
#cv2.line(img1,(200,10),(600,300),(0,0,255),3)		#_________________	LINE
#      _image first     second    color     width
cv2.rectangle(img1,(10,100),(200,300),(0,255,0),1)	#_________________	RECTANGLE

#cv2.circle(img3,(200,200),100,(255,0,0),12)		#_________________	CIRCLE

#cv2.ellipse(img3,(100,100),(150,125),10,0,270,(100,100,100),3)
#		   center   x  y        sa  fa    color     thick
#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img3,[pts],True,(0,255,255))



# to save the image locally
cv2.imwrite('lol.jpg',img3)

# to show the image
cv2.imshow('image',img1)

# to waut for the pic not to get deleted
cv2.waitKey(0)		# 0 for infinite time  time is In ms


#  to destroy one named window
#cv2.destroyWindows('image')
cv2.destroyAllWindows()
