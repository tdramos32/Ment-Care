from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from twitter.models import Tweet
from datetime import date
import requests
from bs4 import BeautifulSoup

# Create your views here.








def tweet(request):
    user = request.user
    acc = user.twitter

    if request.method == 'POST':
        num = request.POST['tweet']
        
        data = request.POST['tweet']
        #label,score = trained_models.bertweet(data)
        URL = "https://nitter.net/"+acc+"/with_replies"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.findall("div", class_="tweet-content media-body")

        for r in results:
            if len(r.contents):
                if r.string is not None:
                    tweet = r.string
                    rating = "SEVERE"
                    
        
        tweetinfo = Tweet(user = user, rating = rating, text = tweet)
        tweetinfo.save()
        
        return redirect(reverse('patient-dashboard'))
    
    return render(request,'tweet/tweet.html',{'items':'none'})