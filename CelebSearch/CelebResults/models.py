from django.db import models

from pattern.web import Twitter, plaintext

class Clips_Adaptor(models.Model):

    def search_tweets(self):
        #TODO: make celeb a user input
        celeb="Lady Gaga"
        twitter_api = Twitter(language='en')
        #TODO: up the count for the final project
        return twitter_api.search(celeb, count=2)

