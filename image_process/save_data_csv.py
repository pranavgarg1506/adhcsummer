#!/usr/bin/python3

import numpy as np
import cv2
import csv

# read the image
img1 = cv2.imread('hi1.jpg',1)

# find the shape and place into a variable
shape = np.shape(img1)		#____  it can save only 2D data
x = shape[0]
y = shape[1] * shape[2]

img1 = np.reshape(img1,(x,y))		#____________RESHAPING THE DATA INTO 2D DATA


# TO WRITE INTO THE FILE IT WILL REPLACE ALL THE PREVIOUS DATA WITH THE NEW ONE
with open('try.csv','w') as file:		#   it will write into the file and it is not there then it will create the file
	writer = csv.writer(file)		#   csv.writer is a fn which helps to write into the file
	for line in range(0,len(img1)):
		writer.writerow(img1[line])


#file.close()   #___________ IT WILL CLOSE THE FILE AND IF YOU WANT TO DO SOME MODIFICATION THE OPEN THE FILE


'''
# TO APPEND THE DATA INTO THE EXISTING FILE
data = np.ones((2,7680))


with open('try.csv','a') as file:
	writer = csv.writer(file)
	writer.writerow(data1)


print(np.shape(img1))
'''
#cv2.waitKey(0)
#cv2.destroyAllWindows()

