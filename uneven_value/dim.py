#! /usr/bin/env python3

import numpy as np

list1 = []
print("Enter the values")

while 1:
    data=input()		# for only integer data possible
    try:
        list1.append(int(data))
    except:
        break
            
size=len(list1)            
print(size) 
n1=size**.5
n2=np.ceil(n1)

print(n2)

for i in range(2,int(n2)+1):
    if (size%i)==0:
        flag=1
        break
    else:
        flag=0
        break
        
if flag==0:
    data=input("Enter one more dimension")
    list1.append(int(data))
    
print("Values are:- ")
for k in list1:
    print(k,end=" ")

    
new_size=len(list1)

z=int(new_size/2)+1
print()

print("Possible Dimensions:- ")

for x in range(2, z):
    if ((new_size%x)==0):
        q=(new_size/x)
        print(x,"*",int(q))

