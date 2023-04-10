from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from mood.models import MoodModel
from datetime import date


# Create your views here.

def mood(request):
    user = request.user
   
   
    if request.method == 'POST':
        num = request.POST['val']
        moodinfo = MoodModel(user = user, mood = num)
        moodinfo.save()

        return redirect(reverse('patient-dashboard'))
    
    return render(request,'mood/mood.html',{'items':'none'})
