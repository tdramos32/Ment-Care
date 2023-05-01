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
        
        urls_arg = ['change-password', 'chat', 'hospital-profile', 'hospital-department-list', 'hospital-doctor-list', 'hospital-doctor-register', 'view-report', 'test-cart',
                     'test-single', 'test-remove-cart', 'delete-prescription', 'delete-report']

        urls_argless = ['hospital_home', 'add-billing', 'edit-billing', 'privacy-policy',
                'about-us', 'patient-register', 'checkout-payment', 'data-table', 'testing']

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
            self.assertEqual(response.status_code,200)
        print()

       