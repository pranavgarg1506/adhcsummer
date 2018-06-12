#!/usr/bin/python3

from nltk.tokenize import sent_tokenize,word_tokenize 
from bs4 import BeautifulSoup
import numpy as np
import requests
from nltk.corpus import stopwords
import string as sr
from nltk.probability import FreqDist


stop_words=stopwords.words('english')


url = 'https://twitter.com/rahulgandhi'

#___________________________________________(data collection) source code
wiki = requests.get(url)
source_data = BeautifulSoup(wiki.text,'html5lib')

# trial version
#print(source_data.prettify())

# removing tags 
text_data = source_data.get_text(strip=True) # by using (strip=True) as argument it will remove all the space
#print(text_data)
print(type(text_data))


#_____________________________________________to tokenize the data or means to separate them into words
tokenized_data = word_tokenize(text_data)

#______DATA CLEANING

# removing punctuation
pun_cleaned_data = [ i for i in tokenized_data  if i not in sr.punctuation]


# removing stop words
#stop_cleaned_data = [ i for i in pun_cleaned_data  if i not in stop_words]


# removing stop words (effectively)
stop_cleaned_data = [ i for i in pun_cleaned_data  if i.lower() not in stop_words]

print(np.shape(tokenized_data))
print(np.shape(pun_cleaned_data))
print(np.size(stop_cleaned_data))

# plotting data
freq = FreqDist(stop_cleaned_data)
freq.plot(20)

















