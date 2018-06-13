#!/usr/bin/python3


from nltk.corpus import wordnet


sub = input('Enter the Word: ')
out_come = wordnet.synsets(sub)
print('')
for i in out_come:
	print(i)
	print('DEFINITION:- '+str(i.definition()))
	print('EXAMPLES:- ')
	for k in i.examples():
		print(k)
	print('')


