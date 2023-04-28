from django.urls import path
from . import views
app_name = 'tweet'

urlpatterns = [
    path('',views.tweet, name = 'tweet'),
] 