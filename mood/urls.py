from django.urls import path
from . import views
app_name = 'mood'

urlpatterns = [
    path('',views.mood, name = 'mood'),
] 