from django.db import models

# Create your models here.

class Tweet(models.Model):
    user = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True, null=True)
    


    def __str__(self):
        return f'{self.user} : {self.rating} : {self.text} : {self.date}'