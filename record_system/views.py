from io import BytesIO
from urllib import response
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from doctor.models import Doctor_Information, Appointment
from doctor.models import  Prescription,Prescription_medicine,Prescription_test
from hospital.models import Patient
from datetime import datetime
from record_system.models import appointment_notes, record
from django.views.generic import View
# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="aplication/pdf")
    return None

def ViewPatientRecord(request,pk):
    record_info = record.objects.get(record_id=pk)
    patient = record_info.patient
    doctor = record_info.doctor
    context={
        'record_info':record_info,
        'patient':patient,
        'doctor':doctor
    }
    pres_pdf=render_to_pdf('patient_full_pdf.html', context)
    if pres_pdf:
        response=HttpResponse(pres_pdf, content_type='application/pres_pdf')
        content="inline; filename=prescription.pdf"
        response['Content-Disposition']= content
        return response
    return HttpResponse("Not Found")
def ViewRecordSummary(request,pk):
    record_info = record.objects.get(record_id=pk)
    patient = record_info.patient
    doctor = record_info.doctor
    context={
        'record_info':record_info,
        'patient':patient,
        'doctor':doctor
    }
    pres_pdf=render_to_pdf('patient_summary_pdf.html', context)
    if pres_pdf:
        response=HttpResponse(pres_pdf, content_type='application/pres_pdf')
        content="inline; filename=prescription.pdf"
        response['Content-Disposition']= content
        return response
    return HttpResponse("Not Found")
def ViewAppoinmentNotes(request,pk):
    appointment_info = appointment_notes.objects.get(appointment_notes_id=pk)
    patient = appointment_info.patient
    doctor = appointment_info.doctor
    app = appointment_info.appointment
    prescriptions = appointment_info.prescriptions
    notes = appointment_info.notes
    next_app = appointment_info.next_appointment
    diagnoses = appointment_info.diagnoses
    context={
        'appointment_info':appointment_info,
        'patient':patient,
        'doctor':doctor,
        'app':app,
        'prescriptions':prescriptions,
        'notes':notes,
        'next_app':next_app,
        'diagnoses':diagnoses
    }
    pres_pdf=render_to_pdf('appointment_notes_pdf.html', context)
    if pres_pdf:
        response=HttpResponse(pres_pdf, content_type='application/pres_pdf')
        content="inline; filename=prescription.pdf"
        response['Content-Disposition']= content
        return response
    return HttpResponse("Not Found")
"""
def prescription_pdf(request,pk):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        prescription = Prescription.objects.get(prescription_id=pk)
        perscription_medicine = Perscription_medicine.objects.filter(prescription=prescription)
        perscription_test = Perscription_test.objects.filter(prescription=prescription)
        current_date = datetime.date.today()
        context={'patient':patient,'current_date' : current_date,'prescription':prescription,'perscription_test':perscription_test,'perscription_medicine':perscription_medicine}
        pdf=render_to_pdf('prescription_pdf.html', context)
        if pdf:
            response=HttpResponse(pdf, content_type='application/pdf')
            content="inline; filename=report.pdf"
            # response['Content-Disposition']= content
            return response
        return HttpResponse("Not Found")
def full_report(request,pk):
    if request.user.is_patient:
        patient = Patient.objects.get(user=request.user)
        prescription = Prescription.objects.get(prescription_id=pk)
        perscription_medicine = Perscription_medicine.objects.filter(prescription=prescription)
        perscription_test = Perscription_test.objects.filter(prescription=prescription)
        current_date = datetime.date.today()
        context={'patient':patient,'current_date' : current_date,'prescription':prescription,'perscription_test':perscription_test,'perscription_medicine':perscription_medicine}
        pdf=render_to_pdf('prescription_pdf.html', context)
        if pdf:
            response=HttpResponse(pdf, content_type='application/pdf')
            content="inline; filename=report.pdf"
            # response['Content-Disposition']= content
            return response
        return HttpResponse("Not Found")
"""