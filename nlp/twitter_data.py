#!/usr/bin/python3

#import libraries
import numpy as np
import string as sr
import tweepy
from textblob import TextBlob
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import string as sr
from nltk.stem.porter import PorterStemmer
import csv
import matplotlib.pyplot as plt



stop_words=stopwords.words('english')


consumer_key = ''
consumer_secret = ''

access_key = ''
access_secret = ''

#for connection
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_key,access_secret)

#  connecting  API  
connect=tweepy.API(auth)

'''
BELOW ARE THE FUNCTIONS U CAN WORK UPON THE CONNECTED OBJECT

print(dir(connect))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_list_members', '_lookup_friendships', '_lookup_users', '_pack_image', '_remove_list_members', '_statuses_lookup', 'add_list_member', 'add_list_members', 'api_root', 'auth', 'blocks', 'blocks_ids', 'cache', 'compression', 'configuration', 'create_block', 'create_favorite', 'create_friendship', 'create_list', 'create_saved_search', 'destroy_block', 'destroy_direct_message', 'destroy_favorite', 'destroy_friendship', 'destroy_list', 'destroy_saved_search', 'destroy_status', 'direct_messages', 'favorites', 'followers', 'followers_ids', 'friends', 'friends_ids', 'friendships_incoming', 'friendships_outgoing', 'geo_id', 'geo_search', 'geo_similar_places', 'get_direct_message', 'get_list', 'get_oembed', 'get_saved_search', 'get_settings', 'get_status', 'get_user', 'home_timeline', 'host', 'list_members', 'list_subscribers', 'list_timeline', 'lists_all', 'lists_memberships', 'lists_subscriptions', 'lookup_friendships', 'lookup_users', 'me', 'media_upload', 'mentions_timeline', 'parser', 'proxy', 'rate_limit_status', 'related_results', 'remove_list_member', 'remove_list_members', 'report_spam', 'retry_count', 'retry_delay', 'retry_errors', 'retweet', 'retweeters', 'retweets', 'retweets_of_me', 'reverse_geocode', 'saved_searches', 'search', 'search_host', 'search_root', 'search_users', 'send_direct_message', 'sent_direct_messages', 'set_delivery_device', 'set_settings', 'show_friendship', 'show_list_member', 'show_list_subscriber', 'statuses_lookup', 'subscribe_list', 'suggested_categories', 'suggested_users', 'suggested_users_tweets', 'supported_languages', 'timeout', 'trends_available', 'trends_closest', 'trends_place', 'unretweet', 'unsubscribe_list', 'update_list', 'update_profile', 'update_profile_background_image', 'update_profile_banner', 'update_profile_image', 'update_status', 'update_with_media', 'upload_host', 'upload_root', 'user_timeline', 'verify_credentials', 'wait_on_rate_limit', 'wait_on_rate_limit_notify']
'''



#____TYPE A KEYWORD AND SEARCH IT ON TWITTER
get_data=connect.search('modi',count=100) # count can be max 100

result = []
for i in get_data:
	raw_data = i.text
	punc_free_data = [ j for j in raw_data  if j not in sr.punctuation ]			#CLEANING
	joined_data = ''.join(punc_free_data)							#	OF
	tokenized_data = word_tokenize(joined_data)						# DATA
	stop_free_data = [ i for i in tokenized_data  if i.lower() not in stop_words]
	joined_data1 = ' '.join(stop_free_data)
	#print(joined_data1)	
	#________________ putting sentiment analyzer on the data too
	analysis = TextBlob(joined_data1)
	#print(analysis.sentiment)
	#analysis.sentiment is of list as type having size 2 and individual element can be accessed by [] method
	result.append(analysis.sentiment[0])

#print(len(result))
#print(result)   # printing sentiment list

'''
# saving the result into txt file
with open('sentiment_data_plot.csv','w') as file:
	writer = csv.writer(file, lineterminator='\n')
	for line in result:
		writer.writerow([line])

file.close() 
'''
sad=[]
neutral=[]
happy=[]
#TO CATEGORISE THE RESULT
for i in result:
	if i<0.0:
		sad.append(i)
	elif i==0.0:
		neutral.append(i)
	else:
		happy.append(i)

sad = len(sad)
neutral = len(neutral)
happy = len(happy)

print(sad,neutral,happy)

y = [sad,neutral,happy]
x = ['sad','neutral','happy']
plt.xlabel('EMOTIONS')
plt.ylabel('FREQUENCY')
plt.bar(x,y,label='graph')
plt.legend()
plt.show()

