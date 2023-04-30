import email
from email.mime import image
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from hospital.models import Hospital_Information, User, Patient
from django.db.models import Q
from pharmacy.models import Medicine, Pharmacist
from doctor.models import Doctor_Information, Prescription, Prescription_test, Report, Appointment, Experience , Education,Specimen,Test
from pharmacy.models import Order, Cart
from sslcommerz.models import Payment
from mood.models import Mood


from hospital_admin.models import Admin_Information,specialization,service,hospital_department, Clinical_Laboratory_Technician, Test_Information
import random,re
import string
from django.db.models import  Count
from datetime import datetime
import datetime
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.urls import reverse


# Create your views here.
def staff_dashboard(request):
    return render(request,'Health_Staff/staff-dashboard')

@csrf_exempt
@login_required(login_url='admin_login')
def labworker_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_labworker:
            
            lab_workers = Clinical_Laboratory_Technician.objects.get(user=request.user)
            doctor = Doctor_Information.objects.all()
            context = {'doctor': doctor,'lab_workers':lab_workers}
            return render(request, 'Health_Staff/staff-dashboard.html',context)
        
@csrf_exempt
@login_required(login_url='admin-login')
def mypatient_list(request):
    if request.user.is_authenticated:
        if request.user.is_labworker:
            lab_workers = Clinical_Laboratory_Technician.objects.get(user=request.user)
            #report= Report.objects.all()
            patient = Patient.objects.all()
            context = {'patient': patient,'lab_workers':lab_workers}
            return render(request, 'Health_Staff/mypatient-list.html',context)
        

def test_list(request):
    if request.user.is_labworker:
        lab_workers = Clinical_Laboratory_Technician.objects.get(user=request.user)
        test = Test_Information.objects.all()
        context = {'test':test,'lab_workers':lab_workers}
    return render(request, 'Health_Staff/test-list.html',context)

@csrf_exempt
@login_required(login_url='admin-login')
def prescription_list(request,pk):
    if request.user.is_authenticated:
        if request.user.is_labworker:
            lab_workers = Clinical_Laboratory_Technician.objects.get(user=request.user)
            patient = Patient.objects.get(patient_id=pk)
            prescription = Prescription.objects.filter(patient=patient)
            context = {'prescription': prescription,'lab_workers':lab_workers,'patient':patient}
            return render(request, 'Health_Staff/prescription-list.html',context)
        

csrf_exempt
@login_required(login_url="login")
def patient_search(request):
    if request.user.is_authenticated and request.user.is_labworker:
        # doctor = Doctor_Information.objects.get(doctor_id=pk)
        id = int(request.GET['search_query'])
        patient = Patient.objects.get(patient_id=id)
        prescription = Prescription.objects.filter(patient=patient)
        appointments = Appointment.objects.filter(patient=patient)
        report = Report.objects.filter(patient=patient) 
        mood = Mood.objects.filter(user = patient.username).all()
        context = {'appointments': appointments,'patient': patient,'report': report, 'mood':mood,'prescription': prescription, 'id' : id}
        return render(request, 'Health_Staff/patient-profile.html', context)
    else:
        logout(request)
        messages.info(request, 'Not Authorized')
        return render(request, 'doctor-login.html')
    
@csrf_exempt
@login_required(login_url="doctor-login")
def patient_profile(request, pk):
    if request.user.is_doctor:
        # doctor = Doctor_Information.objects.get(user_id=pk)
        doctor = Doctor_Information.objects.filter(doctor_id_gte=0)
        patient = Patient.objects.get(patient_id=pk)
        appointments = Appointment.objects.filter(patient=patient).filter(Appointment_STATUS = 'pending')
        prescription = Prescription.objects.filter(patient=patient).all()[0]
        report = Report.objects.filter(patient=patient) 
        mood = Mood.objects.filter(user = patient.username).all()
        
        
    else:
        redirect('doctor-logout')
    context = {'appointments': appointments, 'patient': patient, 'prescription': prescription, 'report': report, 'mood':mood}  
    return render(request, 'Health_Staff/patient-profile.html', context)

@csrf_exempt
@login_required(login_url="doctor-login")
def reject_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'cancelled'
    appointment.save()
    
    
    messages.error(request, 'Appointment Rejected')
    return redirect(f'/staff/patient-search/?search_query={appointment.patient.patient_id}')

csrf_exempt        
@login_required(login_url="doctor-login")
def accept_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.appointment_status = 'confirmed'
    appointment.save()
    print('executed')
    
    # Mailtrap
    
    patient_email = appointment.patient.email
    patient_name = appointment.patient.name
    patient_username = appointment.patient.username
    patient_serial_number = appointment.patient.serial_number
    doctor_name = appointment.doctor.name

    appointment_serial_number = appointment.serial_number
    appointment_date = appointment.date
    appointment_time = appointment.time
    appointment_status = appointment.appointment_status
    
    subject = "Appointment Acceptance Email"
    
    values = {
            "email":patient_email,
            "name":patient_name,
            "username":patient_username,
            "serial_number":patient_serial_number,
            "doctor_name":doctor_name,
            "appointment_serial_num":appointment_serial_number,
            "appointment_date":appointment_date,
            "appointment_time":appointment_time,
            "appointment_status":appointment_status,
    }
    
    html_message = render_to_string('appointment_accept_mail.html', {'values': values})
    plain_message = strip_tags(html_message)
    
    
    
    messages.success(request, 'Appointment Accepted')
    return redirect(f'/staff/patient-search/?search_query={appointment.patient.patient_id}')
def generate_random_string():
    N = 8
    string_var = ""
    string_var = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    return string_var

csrf_exempt
@login_required(login_url="doctor-login")
def booking(request, pk):
    patient = Patient.objects.get(patient_id = pk)
    doctors = Doctor_Information.objects.all()



    if request.method == 'POST':
        doctor= Doctor_Information.objects.get(username = request.POST['doctor_name'])

        appointment = Appointment(patient=patient, doctor=doctor)
        date = request.POST['appoint_date']
        time = request.POST['appoint_time']
        appointment_type = request.POST['appointment_type']
        message = request.POST['message']

    
        transformed_date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
        transformed_date = str(transformed_date)
         
        appointment.date = transformed_date
        appointment.time = time
        appointment.appointment_status = 'pending'
        appointment.serial_number = generate_random_string()
        appointment.appointment_type = appointment_type
        appointment.message = message
        appointment.save()
        
        
        
        messages.success(request, 'Appointment Booked')
        return redirect('Health_Staff:staff-dashboard')

    context = {'patient': patient, 'doctors': doctors}
    #return render(request, 'Health_Staff/booking.html', context)
    # redi = '/staff/booking/'
    return render(request,'Health_Staff/booking.html',context)
