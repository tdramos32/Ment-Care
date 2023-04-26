from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from record_system.views import ViewAppointmentPDF, ViewPatientSummaryPDF, ViewPatientFullPDF

urlpatterns = [
    path('appointment_notes_pdf/', views.ViewAppointmentPDF.as_view(), name='appointment-notes'),
    path('patient_full_pdf/', views.ViewPatientFullPDF.as_view(), name='patient-record'),
    path('patient_summary_pdf/', views.ViewPatientSummaryPDF.as_view(), name='patient-record-summary'),
]
