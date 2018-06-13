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

# removing tags 
text_data = source_data.get_text(strip=True) # by using (strip=True) as argument it will remove all the space
#print(text_data)


# ___________________________________________removing punctuation
pun_cleaned_data = [ i for i in text_data  if i not in sr.punctuation]
#print(pun_cleaned_data)

#__________ joining data
joined = ''.join(pun_cleaned_data)
#print(joined)

#_____________________________________________to tokenize the data or means to separate them into words
tokenized_data = word_tokenize(joined)
#print(tokenized_data)

#______________________________________________removing stop words (effectively)
stop_cleaned_data = [ i for i in tokenized_data  if i.lower() not in stop_words]
#print(stop_cleaned_data)


#__________________________________________________FILTER OUT THE STEM WORDS
stemmer = PorterStemmer()
stem_cleaned_data = [stemmer.stem(i) for i in stop_cleaned_data]


print(np.size(pun_cleaned_data))
print(np.size(tokenized_data))
print(np.size(stop_cleaned_data))
print(np.size(stem_cleaned_data))


#PLOTTING DATA
freq = FreqDist(stem_cleaned_data)
freq.plot(20)















