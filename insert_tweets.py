#!/usr/bin/python

import pymongo
from pymongo import MongoClient
import datetime
from pattern.web import Twitter, plaintext


twitter_api = Twitter(language='en')
client = MongoClient()
db = client['tweetdb']
collection = db['tweets']

some_bullshit = ['@','is','a','are','@','if','the','I','in','and']

for a_scoop in some_bullshit:
    tweets = twitter_api.search(a_scoop, count=3000)
    for tweet in tweets:
        tweet_id = tweet.id
        if collection.find({"tweet_id": tweet_id}).limit(1).count() == 0:
            text = tweet.text
            tweet_date = tweet.date
            date = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S +0000 %Y')
            my_tweet = {"tweet_id": tweet_id,
                        "text": text,
                        "date": date
                        }
            this_tweet_id = collection.insert(my_tweet)
