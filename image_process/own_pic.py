#!/usr/bin/python3

# loading libraries
import cv2
import numpy as np

# make your own pic
black_image = np.zeros((512,512,3))

# save that pic and then read  it through cv2 
cv2.imwrite('black.jpg',black_image)
img = cv2.imread('black.jpg',1)
img1 = cv2.imread('random.jpg',1)

img[100:300,100:300] = img1[100:300,100:300]

print(img[150][150])

for i in range(200,250):
	for j in range(200,250):
		img[i][j][0] = 159
		img[i][j][1] = 150
		img[i][j][2] = 100

cv2.imshow('try',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
