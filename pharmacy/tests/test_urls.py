from django.test import TestCase
from django.urls import reverse, resolve
from hospital.models import User
from pharmacy.views import pharmacy_shop, cart_view, checkout, pharmacy_single_product, remove_from_cart, add_to_cart, increase_cart, decrease_cart
class TestUrls(TestCase):


    def setUp(self):
        self.user = User.objects.create(
            username = 'testdoctor',
            email = 'test@gmail.com',
            password = 'p1',
        )

    def test_url_resolves(self):
        views_arg = ['pharmacy_single_product', 'remove_from_cart', 'add_to_cart', 'increase_cart', 'decrease_cart']

        urls_arg = ['product-single', 'remove-item', 'add-to-cart', 'increase-item', 'decrease-item']

        views_argless = ['pharmacy_shop', 'cart_view', 'checkout']

        urls_argless = ['pharmacy_shop', 'cart', 'checkout']
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
       
