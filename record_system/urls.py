from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from record_system.views import ViewRecordSummary, ViewAppoinmentNotes, ViewPatientRecord

urlpatterns = [
    path('appointment_notes_pdf/', views.ViewAppoinmentNotes, name='appointment-notes'),
    path('patient_full_pdf/', views.ViewPatientRecord, name='patient-record'),
    path('patient_summary_pdf/', views.ViewRecordSummary, name='patient-record-summary'),
    
]
