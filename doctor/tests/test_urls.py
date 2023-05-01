from django.test import TestCase
from django.urls import reverse, resolve
from hospital.models import User
from doctor.views import doctor_login, doctor_dashboard, doctor_profile, doctor_change_password, doctor_profile_settings, doctor_register, logoutDoctor, my_patients, booking, booking_success, schedule_timings, patient_id, create_prescription, patient_profile
from doctor.views import delete_education, delete_experience, appointments, accept_appointment, reject_appointment, patient_search, report_pdf, doctor_review, doctor_test_list, doctor_view_prescription, doctor_view_report

class TestUrls(TestCase):


    def setUp(self):
        self.user = User.objects.create(
            username = 'testdoctor',
            email = 'test@gmail.com',
            password = 'p1',
        )

    def test_url_resolves(self):
        views_arg = ['doctor_profile', 'doctor_change_password', 'booking', 'create_prescription', 'patient_profile', 'delete_education', 'delete_experience', 'accept_appointment', 'reject_appointment', 'patient_search', 'report_pdf', 
                     'doctor_review', 'doctor_view_prescription', 'doctor_view_report']

        urls_arg = ['doctor-profile', 'doctor-change-password', 'booking', 'create-prescription', 'patient-profile', 'delete-education', 'delete-experience', 'accept-appointment', 'reject-appointment', 'patient-search', 'pdf', 
                    'doctor_review', 'doctor-view-prescription', 'doctor-view-report']

        views_argless = ['doctor_login', 'doctor_dashboard', 'doctor_profile_settings', 'doctor_register', 'logoutDoctor', 'my_patients', 'booking_success', 'schedule_timings', 'patient_id', 'appointments', 'doctor_test_list']

        urls_argless = ['doctor-login', 'doctor-dashboard', 'doctor-profile-settings', 'doctor-register', 'doctor-logout', 'my-patients', 'booking-success', 'schedule-timings', 'patient-id', 'appointments', 'doctor-test-list']

        print("~~~TESTING ARGS~~~")
        for i in range(len(urls_arg)):
            print("testing "+urls_arg[i])
            url = reverse(urls_arg[i], args=[self.user.pk])
            self.assertEquals(resolve(url).func, eval(views_arg[i]))
        print()

        print("~~~TESTING ARGLESSS~~~")
        for i in range(len(urls_argless)):
            print("testing "+urls_argless[i])
            url = reverse(urls_argless[i])
            self.assertEquals(resolve(url).func, eval(views_argless[i]))
        print()
       
