#!/usr/bin/python3


import numpy as np
from sklearn.datasets import load_iris 
from sklearn import tree
import matplotlib.pyplot as plt


# data-set == load_iris

#loading load_iris into a variable
iris=load_iris()
#print(iris)

# dir(iris)   to see the functions unser iris


#loading training data into the variable
train_data_1 = iris.data[0:49]  # left the last one for testing in all the three cases
train_data_2 = iris.data[50:99]
train_data_3 = iris.data[100:149]


#loading test data into the variable
test_data_1 = iris.data[49]	# assign the last dataset in every gp to test
test_data_2 = iris.data[99]
test_data_3 = iris.data[149]

#loading result of training data into the variable
output_train_data_1 = iris.target[0:49]
output_train_data_2 = iris.target[50:99]
output_train_data_3 = iris.target[100:149]


# call the decision tree for start for every flower
algo1=tree.DecisionTreeClassifier()
algo2=tree.DecisionTreeClassifier()
algo3=tree.DecisionTreeClassifier()


# convert the ndarry into list


'''
for i in range(1,4):
	list_traindata_i = train_data_i.tolist()
	list_output_train_data_i = output_train_data_i.tolist()
'''
list_train_data_1 = train_data_1.tolist()
list_train_data_2 = train_data_2.tolist()
list_train_data_3 = train_data_3.tolist()


list_output_train_data_1 = output_train_data_1.tolist()
list_output_train_data_2 = output_train_data_2.tolist()
list_output_train_data_3 = output_train_data_3.tolist()


# print(np.shape(test_data_1))		----- this is in the order of 4*1   


array_test_data_1 = np.reshape(test_data_1,(1,4))	# conversion of the test data from 4*1 to 1*4 array
array_test_data_2 = np.reshape(test_data_2,(1,4))
array_test_data_3 = np.reshape(test_data_3,(1,4))


list_test_data_1 = array_test_data_1.tolist()	#  conversion of array into list
list_test_data_2 = array_test_data_2.tolist()
list_test_data_3 = array_test_data_3.tolist()


# training the machine with the input and output
trained_1 = algo1.fit(list_train_data_1,list_output_train_data_1)
trained_2 = algo2.fit(list_train_data_2,list_output_train_data_2)
trained_3 = algo3.fit(list_train_data_3,list_output_train_data_3)


# testing the machine with the testing set
result_1 = trained_1.predict(list_test_data_1)
result_2 = trained_2.predict(list_test_data_2)
result_3 = trained_3.predict(list_test_data_3)


# printing the predicted result
print(result_1)
print(result_2)
print(result_3)



list1=[]
list2=[]
list3=[]






for i in range(0,4):
	list1.append(max(iris.data[0:49,i]))

for i in range(0,4):
	list2.append(max(iris.data[50:99,i]))

for i in range(0,4):
	list3.append(max(iris.data[100:149,i]))


'''
max01 = max(iris.data[0:49,0])
max02 = max(iris.data[50:99,0])
max03 = max(iris.data[100:149,0])

max11 = max(iris.data[0:49,1])
max12 = max(iris.data[50:99,1])
max13 = max(iris.data[100:149,1])

max21 = max(iris.data[0:49,2])
max22 = max(iris.data[50:99,2])
max23 = max(iris.data[100:149,2])

max31 = max(iris.data[0:49,3])
max32 = max(iris.data[50:99,3])
max33 = max(iris.data[100:149,3])

list1 = [max01,max11,max21,max31]
list2 = [max02,max12,max22,max32]
list3 = [max03,max13,max23,max33]
'''

plt.plot(iris.feature_names,list1,label='flw1',color='r',marker='*')
plt.plot(iris.feature_names,list2,label='flw2',color='b',marker='.')
plt.plot(iris.feature_names,list3,label='flw3',color='g',marker='1')
plt.xlabel('Features of flowers')
plt.ylabel('Values')
plt.title('max feature of every flower')
plt.legend()
plt.grid()
plt.show()



		### ----------------------------- COMPLETED --------------------------------###



