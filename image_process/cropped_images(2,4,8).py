#!/usr/bin/python3

#load libraries
import cv2
import numpy as np


img = cv2.imread('cat.jpg',1)
shape = np.shape(img)

x = shape[0]
y = shape[1]

def half():
	x1 = int(x/2)
	y1 = int(y/2)
	
	rest_x = x-x1
	rest_y = y-y1
	
	main = img[0:x1,0:y1]
	rest = img[x1:x,y1:y]
	rest_top = img[0:x1,y1:y]
	rest_bottom= img[x1:x,0:y1]
	
	cv2.imshow('main',main)
	cv2.imshow('rest',rest)
	cv2.imshow('rest_top',rest_top)
	cv2.imshow('rest_bottom',rest_bottom)	
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
	cv2.destroyAllWindows()

def quarter():
	x1 = int(x/4)
	y1 = int(y/4)
	
	rest_x = x-x1
	rest_y = y-y1
	
	main = img[0:x1,0:y1]
	rest = img[x1:x,y1:y]
	rest_top = img[0:x1,y1:y]
	rest_bottom= img[x1:x,0:y1]
	
	cv2.imshow('main',main)
	cv2.imshow('rest',rest)
	cv2.imshow('rest_top',rest_top)
	cv2.imshow('rest_bottom',rest_bottom)	
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
	cv2.destroyAllWindows()

def octal():
	x1 = int(x/8)
	y1 = int(y/8)
	
	rest_x = x-x1
	rest_y = y-y1
	
	main = img[0:x1,0:y1]
	rest = img[x1:x,y1:y]
	rest_top = img[0:x1,y1:y]
	rest_bottom= img[x1:x,0:y1]
	
	cv2.imshow('main',main)
	cv2.imshow('rest',rest)
	cv2.imshow('rest_top',rest_top)
	cv2.imshow('rest_bottom',rest_bottom)	
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
	cv2.destroyAllWindows()


option = '''
		Choice:- 
			1  for half
			2  for quarter
			3  for octal
'''

print(option)
user = input('Enter the choice:- ')

if user == '1':
	half()
elif user == '2':
	quarter()
elif user == '3':
	octal()
else:
	print('Invalid Choice')
