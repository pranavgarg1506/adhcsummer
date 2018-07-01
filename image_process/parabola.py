#!/usr/bin/python3


import cv2
import numpy as np
import math
img = cv2.imread('cat2.jpg',1)
print(np.shape(img))

x = int(input('Enter h'))
y = int(input('Enter k'))
a = int(input('Enter a'))
#cv2.circle(img,(200,272),(50),(255,255,0),1)
lol = np.zeros((600,475,3))
cv2.imwrite('para1.jpg',lol)

hehe = cv2.imread('para1.jpg',1)

if a>0:
	for j in range(y,np.shape(img)[1]):
		p=int((j-y)/a)
		temp = int(math.sqrt(p))
		temp1 = x + temp
		temp2 = x - temp
		for i in range(temp2,temp1):
			hehe[i][j][0] = img[i][j][0]
			hehe[i][j][1] = img[i][j][1]
			hehe[i][j][2] = img[i][j][2]


			img[i][j][0] = 0
			img[i][j][1] = 0
			img[i][j][2] = 0

else:
	for j in range(0,y):
		temp = int(math.sqrt((j-y)/(-a)))
		temp1 = x + temp
		temp2 = x - temp
		for i in range(temp2,temp1):
			hehe[i][j][0] = img[i][j][0]
			hehe[i][j][1] = img[i][j][1]
			hehe[i][j][2] = img[i][j][2]


			img[i][j][0] = 0
			img[i][j][0] = 0
			img[i][j][0] = 0



cv2.imwrite('ans.jpg',hehe)
cv2.imshow('main',hehe)
cv2.imshow('main1',img)


cv2.waitKey(0)
cv2.destroyAllWindows()




