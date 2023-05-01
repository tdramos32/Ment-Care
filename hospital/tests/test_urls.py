from django.test import TestCase
from django.urls import reverse, resolve
from hospital.models import User
from hospital.views import hospital_home, search, add_billing, appointments, edit_billing, edit_prescription, patient_dashboard, privacy_policy, profile_settings, about_us, patient_register
from hospital.views import logoutUser, multiple_hospital, chat_doctor, checkout_payment, pharmacy_shop, data_table, testing, change_password, chat, hospital_profile, hospital_department_list,  hospital_doctor_list
from hospital.views import hospital_doctor_register, view_report, test_cart, prescription_view, prescription_pdf, test_single, test_remove_cart, test_add_to_cart, delete_prescription, delete_report
class TestUrls(TestCase):


    def setUp(self):
        self.user = User.objects.create(
            username = 'testdoctor',
            email = 'test@gmail.com',
            password = 'p1',
        )

    def test_url_resolves(self):
        views_arg = ['change_password', 'chat', 'hospital_profile', 'hospital_department_list', 'hospital_doctor_list', 'hospital_doctor_register', 'view_report', 'test_cart', 'prescription_view', 
             'prescription_pdf', 'test_single', 'test_remove_cart', 'delete_prescription', 'delete_report']

        urls_arg = ['change-password', 'chat', 'hospital-profile', 'hospital-department-list', 'hospital-doctor-list', 'hospital-doctor-register', 'view-report', 'test-cart', 'prescription-view', 
            'pres_pdf', 'test-single', 'test-remove-cart', 'delete-prescription', 'delete-report']

        views_argless = ['hospital_home', 'search', 'add_billing', 'edit_billing', 'edit_prescription', 'patient_dashboard', 'privacy_policy', 'profile_settings', 
                 'about_us', 'patient_register', 'logoutUser', 'multiple_hospital', 'chat_doctor', 'checkout_payment', 'data_table', 'testing']

        urls_argless = ['hospital_home', 'search', 'add-billing', 'edit-billing', 'edit-prescription', 'patient-dashboard', 'privacy-policy', 'profile-settings', 
                'about-us', 'patient-register', 'logout', 'multiple-hospital', 'chat-doctor', 'checkout-payment', 'data-table', 'testing']
        
        print("~~~TESTING ARGS~~~")
        for i in range(len(urls_arg)):
            print("testing "+urls_arg[i])
            url = reverse(urls_arg[i], args=[self.user.pk])
            self.assertEquals(resolve(url).func, eval(views_arg[i]))
        print()

        print("~~~TESTING ARGLESS~~~")
        for i in range(len(urls_argless)):
            print("testing "+urls_argless[i])
            url = reverse(urls_argless[i])
            self.assertEquals(resolve(url).func, eval(views_argless[i]))
        print()
