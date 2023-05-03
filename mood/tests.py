from django.test import TestCase

# Create your tests here.
from train import *
from scraper import *
def getSent(data):
    
   
    output = clean_output(data)
    toxic = output['toxic']
    severe_toxic = output['severe_toxic']
    obscene = output['obscene']
    threat = output['threat']
    insult = output['insult']
    identity_hate = output['identity_hate']

tweets = tweet_scraper('elonmusk')

for tweet in tweets:
    print(tweet,clean_output(tweet))