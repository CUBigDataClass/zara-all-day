from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render

from CelebResults.models import Clips_Adaptor

def index(request):
    clips = Clips_Adaptor()
    tweets = clips.search_tweets()
    scores = clips.get_sentiment(tweets)
    template = loader.get_template('CelebResults/index.html')
    context = Context({'tweets':tweets, 'scores': scores})
    print tweets, scores
    response = template.render(context)
    return HttpResponse(response)
    