#!/usr/bin/python3

from nltk.tokenize import sent_tokenize,word_tokenize 
from bs4 import BeautifulSoup
import numpy as np
import requests
from nltk.corpus import stopwords
import string as sr
from nltk.stem.porter import PorterStemmer
from nltk.probability import FreqDist


stop_words=stopwords.words('english')


url = 'https://www.ndtv.com/india'

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

#______________________________________________DATA CLEANING

# removing punctuation
pun_cleaned_data = [ i for i in tokenized_data  if i not in sr.punctuation]

# removing stop words
#stop_cleaned_data = [ i for i in pun_cleaned_data  if i not in stop_words]


# removing stop words (effectively)
stop_cleaned_data = [ i for i in pun_cleaned_data  if i.lower() not in stop_words]

#_________________________________________________ FILTER OUT THAT ARE NOT ALPHA NUMERIC
alpha_cleaned_data = [ i for i in stop_cleaned_data  if not i.isalpha()]


#__________________________________________________FILTER OUT THE STEM WORDS
stemmer = PorterStemmer()
stem_cleaned_data = [stemmer.stem(i) for i in alpha_cleaned_data]



print(np.size(tokenized_data))
print(np.size(pun_cleaned_data))
print(np.size(stop_cleaned_data))
print(np.size(alpha_cleaned_data))
print(np.size(stem_cleaned_data))



# plotting data
freq = FreqDist(stem_cleaned_data)
freq.plot(20)

















