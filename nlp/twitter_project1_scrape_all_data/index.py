#!/usr/bin/python3

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


consumer_key = '4pFDi9hjsRO1ETQGPL3OD8jTh'
consumer_secret = 'AwEyTj7s9mI5jxMs4C2hohzWHXXtwoQNuIUJdOyAnWsLdoRpOb'

access_key = '2255612793-3qkacVeIuFQaJykhvSvMadLPXvUuvm84ZXO62pu'
access_secret = 'qdsqHnAy7YprfN3ejtjO5i8E6zO1wgYmSTMKvE86XXfyd'


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
