from django.shortcuts import render
from django.http import HttpResponse

from CelebResults.models import Clips_Adaptor

def index(request):
    clips = Clips_Adaptor()
    tweets = clips.search_tweets()
    #TODO: create template file and pull HTML out of here
    response =  '''
    <html>
    <head>
        <title>Tweets</title>
    </head>
    <body>
        <ol>
            %s
        </ol>
    </body>
    </html>
    ''' % '\n'.join(['<li>%s</li>' % tweet.text for tweet in tweets])
    return HttpResponse(response)
