#!/usr/bin/env python3

import math
import numpy as np

dim_list=[]  # initalize big matrix dimensions list
values=[]  #  for elements level filter
final_values=[] # for matrix level filter

big_x,big_y=input("Enter the order of the big matrix:- ").split(' ') # take the value and put them in 2 different variables with the split

big_x=int(big_x)  # conversion of str dim into int
big_y=int(big_y)

#print(big_x)
#print(big_y)


elements=big_x*big_y  # calculate no of elements in big matrix
print("No of elements are:- ",elements)

half_elements=int(elements/2)  # to find the  possible values


for i in range(4,half_elements+1):
	if ((elements%i)==0):
		values.append(i)

print("first values are:- ",values) # correct execution

for j in range(0,len(values)):  # for all possible values possible
	for i in range(2,int(np.ceil(values[j]**.5))+1):
		if((values[j]%i)==0):
			final_values.append(values[j])
			break


print("Final values are:- ",final_values)


print("Possible Short matrice possible are:- ") 

for i in range(0,len(final_values)):	# for matrices
	for j in range(2,int(np.ceil(values[i]**.5))+1):
		if((final_values[i]%j)==0):
			print(j,"*",int(final_values[i]/j))




































