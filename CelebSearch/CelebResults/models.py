from django.db import models

from pattern.web import Twitter, plaintext
from pattern.en import sentiment
import pymongo
from pymongo import MongoClient

class Clips_Adaptor(models.Model):

    def search_tweets(self):
        #TODO: make celeb a user input
        celeb="Lady Gaga"
        twitter_api = Twitter(language='en')
        #TODO: up the count for the final project
        return twitter_api.search(celeb, count=2)

    def get_sentiment(self, tweets):
        scores = []
        for tweet in tweets:
            score = sentiment(tweet.text)
            scores.append(score)
        return scores



class Mongo_Service(models.Model):
    client = ''
    db = ''
    collection = ''

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['tweetDB']
        self.collection = self.db['tweets']

