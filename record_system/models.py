from django.db import models
from django import forms

# Create your models here.
class record(models.Model):
    doctor_id = models.AutoField(primary_key=True) 
    doctor_name = models.AutoField(primary_key=True) 
    patient_name = models.CharField(max_length=100, null=True, blank=True)
    patient_dob = models.DateField(auto_now_add=True, null=True)
    patient_id = models.AutoField(primary_key=True)
    patient_age = models.IntegerField(null=True, blank=True)
    patient_diagnoses = models.TextField(max_length=1500, null=True, blank=True)
    patient_drugs = models.TextField(max_length=1500, null=True, blank=True)
    is_violent = models.BooleanField(default=False)
    is_suicidal = models.BooleanField(default=False)
    has_been_sectioned = models.BooleanField(default=False)
    is_sectioned = models.BooleanField(default=False)
    is_violent = models.BooleanField(default=False)
    
    relationship_choices = (
        ('1', 'Single'),
        ('2', 'Married'),
        ('3', 'Engaged'),
        ('4', 'In a Relationship'),
        ('5', "It's Complicated"),
    )
    relationship_status = forms.MultipleChoiceField(choices=relationship_choices)

    suffix_choices = (
        ('1','Mr.'),
        ('2','Mrs.'),
        ('3','Miss'),
        ('4','Dr.')
        ('5','NONE')
    )
    suffix = forms.MultipleChoiceField(choices=suffix_choices)
    children_count = models.IntegerField(default=0,null=True,blank=True)
    patient_history = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return 

