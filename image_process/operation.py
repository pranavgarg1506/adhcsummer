#!/usr/bin/python3

import  cv2
import numpy as np

img1=cv2.imread('cat.jpg')
img2=cv2.imread('lolol.jpg')
img3=cv2.imread('hi.jpg')
img4=cv2.imread('hi1.jpg')
img5=cv2.imread('hi2.jpg')
img6=cv2.imread('hi3.jpg')
img7=cv2.imread('hi4.jpg')


img1 = img1[200:700,200:900]
img2 = img2[200:700,200:900]
img3 = img3[200:700,200:900]
img4 = img4[200:700,200:900]
img5 = img5[200:700,200:900]
img6 = img6[200:700,200:900]
img7 = img7[200:700,200:900]

print(np.shape(img1))
print(np.shape(img2))
#  adding  image with equal contribution 
#  image shape must be common 
#newimg=cv2.add(img1,img3)
#newimg1=cv2.add(img3,img2)

#  to  add some %  of image             #  alpha factor for image properties
#  alpha can be  0 OR  1 
newimg=cv2.addWeighted(img1,0.9,img3,0.3,1)
newimg1=cv2.addWeighted(img1,0.5,img2,0.9,0)
newimg2=cv2.addWeighted(img5,0.5,img7,0.9,0)
newimg3=cv2.addWeighted(img3,0.5,img7,0.9,0)
newimg4=cv2.addWeighted(img4,0.5,img7,0.9,0)
newimg5=cv2.addWeighted(img5,0.5,img7,0.9,0)
newimg6=cv2.addWeighted(img6,0.5,img7,0.9,0)

cv2.imshow('windows',newimg)
cv2.imshow('windows19',newimg1)
cv2.imshow('windows20',newimg2)
cv2.imshow('windows21',newimg3)
cv2.imshow('windows22',newimg4)
cv2.imshow('windows23',newimg5)
cv2.imshow('windows24',newimg6)



cv2.waitKey(0)
cv2.destroyAllWindows()
