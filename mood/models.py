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