from . import views
from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Health_Staff'

urlpatterns = [
    path('',views.staff_dashboard, name = 'staff-dashboard'),
    path('staff-dashboard/', views.labworker_dashboard,name='staff-dashboard'),
    path('mypatient-list/', views.mypatient_list,name='mypatient-list'),
    path('test-list/', views.test_list,name='test-list'),
    path('prescription-list/<int:pk>', views.prescription_list,name='prescription-list'),
    path('patient-search/', views.patient_search, name='patient-search'),
    path('patient-profile/<int:pk>/',views.patient_profile, name='patient-profile'),
    path('accept-appointment/<int:pk>/',views.accept_appointment, name='accept-appointment'),
    path('reject-appointment/<int:pk>/',views.reject_appointment, name='reject-appointment'),
    path('booking/<int:pk>/', views.booking, name='booking'),

    

]