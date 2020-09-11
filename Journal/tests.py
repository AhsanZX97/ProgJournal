from django.test import TestCase, Client
from .models import resource
from django.test.client import RequestFactory
from .views import resources, addPage
from django.urls import reverse, resolve


# Create your tests here.
class ResourceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = resource(name="Google", link="www.google.com", image="python_aSpKBup.png")
        cls.res.save()
        cls.res = resource(name="Stackoverflow", link="www.stackoverflow.com", image="python_aSpKBup.png")
        cls.res.save()
        cls.res = resource(name="devto", link="www.dev.to", image="python_aSpKBup.png")
        cls.res.save()
        cls.resources = resource.objects

    @classmethod
    def tearDownClass(cls):
        cls.res.delete()
        resource.objects.get(id= 1).delete()

    def test_all_res(self):
        self.assertEqual(self.resources.all().count(), 3)

    def test_get_first_res(self):
        testRes = self.resources.get(id = 1)
        self.assertEqual(testRes.name, "Google")
        self.assertEqual(testRes.link, "www.google.com")
        self.assertEqual(testRes.image, "python_aSpKBup.png")

    def test_get_second_res(self):
        testRes = self.resources.get(id = 2)
        self.assertEqual(testRes.name, "Stackoverflow")
        self.assertEqual(testRes.link, "www.stackoverflow.com")
        self.assertEqual(testRes.image, "python_aSpKBup.png")

    def test_get_third_res(self):
        testRes = self.resources.get(id = 3)
        self.assertEqual(testRes.name, "devto")
        self.assertEqual(testRes.link, "www.dev.to")
        self.assertEqual(testRes.image, "python_aSpKBup.png")

    def test_del_second_res(self):
        testRes = self.resources.get(id = 2)
        testRes.delete()
        self.assertEqual(resource.objects.all().count(), 2)

    def test_update_first_res(self):
        testRes = self.resources.get(id = 1)
        testRes.name = "Youtube"
        testRes.link = "www.youtube.com"
        testRes.image = "dj2_f8reo0x.jpg"
        testRes.save()
        test = self.resources.get(id = 1)
        self.assertEqual(test.name, "Youtube")
        self.assertEqual(test.link, "www.youtube.com")
        self.assertEqual(testRes.image, "dj2_f8reo0x.jpg")

class urlTest(TestCase):

    def test_homePage(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, resources)

    def test_addPage(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func, addPage)

    def test_editPage(self):
        url = reverse('edit',args=[41])
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

    def test_addResource(self):
        response = self.client.post(reverse('addRes'),{
            "name": "Google",
            "link": "https://www.google.com",
            "file": "python_aSpKBup.png"
        })
        resource.objects.get(id=2).delete()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(resource.objects.first().name, "Google")

    def test_editPage(self):
        response = self.client.post(reverse('addRes'),{
            "name": "Google",
            "link": "https://www.google.com",
            "file": "python_aSpKBup.png"
        })
        self.assertEqual(response.status_code, 302)
        resource.objects.get(id=2).delete()
        self.assertEqual(resource.objects.first().name, "Google")
        response2 = self.client.get(reverse("edit", args=[6]))
        self.assertTemplateUsed(response2, 'add.html')

    def test_editResource(self):
        response = self.client.post(reverse('addRes'),{
            "name": "Google",
            "link": "https://www.google.com",
            "file": "python_aSpKBup.png"
        })
        self.assertEqual(response.status_code, 302)
        resource.objects.get(id=2).delete()
        self.assertEqual(resource.objects.first().name, "Google")
        response2 = self.client.post(reverse("editRes", args=[7]),{
            "editname": "Youtube",
            "editlink": "https://www.youtube.com",
            "editfile": "python_aSpKBup.png"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resource.objects.first().name, "Youtube")

    def test_deleteResource(self):
        response = self.client.post(reverse('addRes'),{
            "name": "Google",
            "link": "https://www.google.com",
            "file": "python_aSpKBup.png"
        })
        self.assertEqual(response.status_code, 302)
        resource.objects.get(id=2).delete()
        self.assertEqual(resource.objects.all().count(), 1)
        response2 = self.client.get(reverse("delRes", args=[5]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resource.objects.all().count(), 0)