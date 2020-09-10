from django.core.handlers.wsgi import WSGIRequest
from django.test import TestCase, Client
from .models import resource
from django.test.client import RequestFactory
from .views import resources, addPage
from django.urls import reverse, resolve


# Create your tests here.
class ResourceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = resource(name="Google", link="www.google.com")
        cls.res.save()
        cls.res = resource(name="Stackoverflow", link="www.stackoverflow.com")
        cls.res.save()
        cls.res = resource(name="devto", link="www.dev.to")
        cls.res.save()

    @classmethod
    def tearDownClass(cls):
        cls.res.delete()

    def test_all_res(self):
        self.assertEqual(resource.objects.all().count(), 3)

    def test_get_first_res(self):
        testRes = resource.objects.get(id = 1)
        self.assertEqual(testRes.name, "Google")
        self.assertEqual(testRes.link, "www.google.com")

    def test_get_second_res(self):
        testRes = resource.objects.get(id = 2)
        self.assertEqual(testRes.name, "Stackoverflow")
        self.assertEqual(testRes.link, "www.stackoverflow.com")

    def test_get_third_res(self):
        testRes = resource.objects.get(id = 3)
        self.assertEqual(testRes.name, "devto")
        self.assertEqual(testRes.link, "www.dev.to")

    def test_del_second_res(self):
        testRes = resource.objects.get(id = 2)
        testRes.delete()
        self.assertEqual(resource.objects.all().count(), 2)

    def test_update_first_res(self):
        testRes = resource.objects.get(id = 1)
        testRes.name = "Youtube"
        testRes.link = "www.youtube.com"
        testRes.save()
        test = resource.objects.get(id = 1)
        self.assertEqual(test.name, "Youtube")
        self.assertEqual(test.link, "www.youtube.com")

class urlTest(TestCase):

    def test_homePage(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, resources)

    def test_addPage(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func, addPage)

class viewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homePage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'resource.html')

    def test_addPage(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')