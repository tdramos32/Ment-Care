from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from mood.models import Mood, Twitter
from mood.scraper import *
from mood.train import *
from . import trained_models
from datetime import date
from mood.models import Tweets


# Create your views here.

def mood(request):
    user = request.user
    has_user_name = int(len(Twitter.objects.filter(user = user))) > 0
    if(has_user_name):
        print("He has username")
    else:
        print("He doesn't have username")
   
    if request.method == 'POST':
        num = request.POST['mood']
        


        data = request.POST['mood']
        label,score = trained_models.bertweet(data)

        moodinfo = Mood(user = user, input = data, label = label)
        moodinfo.save()
        twitter_user = str(request.POST['twitter'])
        if(twitter_user == ""):
            print("Didn't enter a username")
        else:
            tweetinfo = Twitter(user = user, tweeter_username = twitter_user, registered = "ON")
            tweetinfo.save()
            all_tweets = tweet_scraper(twitter_user)
            for tweet in all_tweets:
                output = clean_output(tweet)
                the_tweet = Tweets(user = user, tweet = tweet, toxic = output['toxic'], severe_toxic = output['severe_toxic'], obscene = output['obscene'], threat = output['threat'] , insult = output['insult'], identity_hate = output['identity_hate'])
                print(the_tweet.toxic)
                the_tweet.save()
            
        return redirect(reverse('patient-dashboard'))
    
    return render(request,'mood/mood.html',{'gottwitter':has_user_name})
