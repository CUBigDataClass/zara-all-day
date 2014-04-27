from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response

from CelebResults.models import Clips_Adaptor, Mongo_Service

def index(request):
    '''
    Renders the main search page
    '''
    context = RequestContext(request,{
        })
    return render_to_response('CelebResults/index.html', context)

def results(request):
    '''
    Renders the results page
    '''
    if request.method == "GET":
        clips = Clips_Adaptor()
        mongodb = Mongo_Service()
        name = request.GET.__getitem__("artistname")

        ## If no input given, stay on search page
        if name == "":
            template = loader.get_template('CelebResults/index.html')
            context = Context()
            response = template.render(context)
            return HttpResponse(response)

        ## Search tweets in mongo
        tweets = mongodb.search_tweets(name)
        
        ## If none found, search twitter
        if len(tweets) == 0:
            tweets = clips.search_tweets(name)

        ## Score the tweets with sentiment analysis
        scores = clips.get_sentiment(tweets)
        context = RequestContext(request, {'tweets':tweets, 'scores': scores})
        return render_to_response('CelebResults/results.html', context)

