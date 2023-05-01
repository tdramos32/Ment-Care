from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from mood.models import Mood
from . import trained_models
from datetime import date


# Create your views here.

def mood(request):
    user = request.user
   
   
    
    
    return render(request,'mood/mood.html',{'items':'none'})
