#!/usr/bin/python3

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize 
import string as sr
from nltk.stem.porter import PorterStemmer
from nltk.probability import FreqDist
import PyPDF2
import numpy as np
from collections import Counter

stop_words=stopwords.words('english')

#open the pdf
pdf_object = open('Harry_Potter_and_the_Sorcerers_Stone.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(pdf_object)
count = pdfreader.numPages

# print no of pages
print(count)

'''
total_words = []

for j in range(40,42):
	page = pdfreader.getPage(j)
	raw_text = page.extractText()

	pun_cleaned_data = [ i for i in raw_text  if i not in sr.punctuation]
	joined = ''.join(pun_cleaned_data)
	tokenized_data = word_tokenize(joined)
	stop_cleaned_data = [ i for i in tokenized_data  if i.lower() not in stop_words]
	for k in stop_cleaned_data:
		total_words.append(k)

print(total_words)
dictionary = Counter(total_words)
'''

words=[]


for i in range(40,41):
	page = pdfreader.getPage(i)
	raw_text = page.extractText()
	#print(raw_text)
	tokenized_sentence = sent_tokenize(raw_text)
	
	#print(type(tokenized_sentence))		#list
	#print(type(tokenized_sentence[0]))		#string
	sentences=[]
	for k in tokenized_sentence:
		k=k.replace('\n','')
		data = [ i for i in k if i not in sr.punctuation]		
		joined = ''.join(data)
		sentences.append(joined)
	sentences1=[]
	for k in sentences:
		tokenized_data = word_tokenize(k)
		stop_cleaned_data = [ i for i in tokenized_data  if i.lower() not in stop_words]
		#stemmer = PorterStemmer()
		#stem_cleaned_data = [stemmer.stem(i) for i in stop_cleaned_data]
		joined1 = ' '.join(stop_cleaned_data)
		sentences1.append(joined1)
	
	for k in sentences1:
		
	



	
