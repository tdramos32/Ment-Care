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
   
   
    if request.method == 'POST':
        num = request.POST['mood']
        


        data = request.POST['mood']
        label,score = trained_models.bertweet(data)

        moodinfo = Mood(user = user, input = data, label = label)
        moodinfo.save()
        
        return redirect(reverse('patient-dashboard'))
    
    return render(request,'mood/mood.html',{'items':'none'})
