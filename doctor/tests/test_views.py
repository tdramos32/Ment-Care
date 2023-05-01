from django.test import TestCase, Client
from django.urls import reverse
from hospital.models import User

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username = 'testdoctor',
            email = 'test@gmail.com',
            password = 'p1',
        )
    
    def test_project_doctor_GET(self):
        

        urls_arg = ['doctor-profile', 'doctor-change-password', 'booking', 'create-prescription', 'patient-profile', 'delete-education', 'delete-experience', 'accept-appointment', 'reject-appointment', 'patient-search',
                                      'doctor_review', 'doctor-view-prescription', 'doctor-view-report']
        
        urls_argless = ['doctor-dashboard', 'doctor-profile-settings', 'my-patients', 'booking-success', 'schedule-timings', 'patient-id', 'appointments', 'doctor-test-list']

        print("~~~TESTING ARGS~~~")
        for i in range(len(urls_arg)):
            print("testing "+urls_arg[i])
            response = self.client.get(reverse(urls_arg[i],args=[self.user.pk]))
            self.assertEquals(response.status_code,302)
        print()

        print("~~~TESTING ARGLESS~~~")
        for i in range(len(urls_argless)):
            print("testing "+urls_argless[i])
            response = self.client.get(reverse(urls_argless[i]))
            self.assertEquals(response.status_code,302)     
        print()   