from django.db import models
from datetime import date
from datetime import datetime

# Create your models here.
class Mood(models.Model):

    user = models.CharField(max_length=100)
    input = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True, null=True)
    


    def __str__(self):
        return f'{self.user} : {self.input} : {self.label} : {self.date}'

class Twitter(models.Model):

    user = models.CharField(max_length=100)
    tweeter_username = models.CharField(max_length=200, null=True, blank=True)
    registered = models.CharField(max_length=200, null=True, blank=True, default = 'OFF')

    def __str__(self):
        return f'{self.user} : {self.tweeter_username} : {self.registered}'

class Tweets(models.Model):
    user = models.CharField(max_length=100)
    tweet = models.CharField(max_length = 100)
    toxic = models.CharField(max_length = 6)
    severe_toxic = models.CharField(max_length = 6)
    obscene = models.CharField(max_length = 6)
    threat = models.CharField(max_length = 6)
    insult = models.CharField(max_length = 6)
    identity_hate = models.CharField(max_length = 6)
