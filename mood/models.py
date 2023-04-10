from django.db import models
from datetime import date
from datetime import datetime

# Create your models here.
class MoodModel(models.Model):
    user = models.CharField(max_length=100)
    mood = models.IntegerField()
    date = models.DateField(auto_now_add=True, null=True)



    def __str__(self):
        return f'{self.user} : {self.mood} : {self.date}'