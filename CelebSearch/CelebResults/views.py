from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from django.shortcuts import render, render_to_response

from CelebResults.models import Clips_Adaptor

def index(request):
    #template = loader.get_template('CelebResults/index.html')
    #context = Context()
    context = RequestContext(request,{

        })
    #response = template.render(context)
    return render_to_response('CelebResults/index.html', context)

def results(request):
    if request.method == "GET":
        clips = Clips_Adaptor()
        name = request.GET.__getitem__("artistname")

        # If no input given, stay on search page
        if name == "":
            template = loader.get_template('CelebResults/index.html')
            context = Context()
            response = template.render(context)
            return HttpResponse(response)

        tweets = clips.search_tweets(name)
        scores = clips.get_sentiment(tweets)
        print tweets, scores
        template = loader.get_template('CelebResults/results.html')
        context = Context({'tweets':tweets, 'scores': scores})
        response = template.render(context)
        return HttpResponse(response)
