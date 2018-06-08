#!/usr/bin/python3


# IMPORT LIBRARY
import cv2

# reading an image
img1 = cv2.imread('cat2.jpg',1)

# call ROI fn
points = cv2.selectROI(img1)

#print(points)

# to show diagonals points of the rectangle
x1 = points[0]
y1 = points[1]
x2 = points[0] + points[2]
y2 = points[1] + points[3]

#cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),3)    USED TO FIND THE POINTS

img2 = img1[y1:y2,x1:x2]  # CROPPED IMAGE BY ROI

cv2.imshow('lol',img2)  # SHOWING THE ROI IMAGE ON NEW WINDOW


cv2.waitKey(0)
cv2.destroyAllWindows()
