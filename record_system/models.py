from django.db import models
from django import forms
from doctor.models import Prescription, Doctor_Information, Appointment
from hospital.models import Patient
# Create your models here.
class diagnoses_info(models.Model):
    diagnoses = models.CharField(max_length=64, null=True, blank=True)
    date_of_diagnosis = models.DateField(auto_now_add=True, null=True)

class record(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return(self.patient_name + "'s Mental Health Report") 

#tes
class appointment_notes(models.Model):
    appointment_notes_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    prescriptions = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    #Will also need the medical staff which simon is making
    notes = models.TextField(max_length=1000, null=True, blank=True)
    next_appointment = models.DateField(auto_now_add=True, null=True)
    diagnoses = models.ForeignKey(diagnoses_info, on_delete=models.CASCADE, null=True, blank=True)