from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

#TEST za provjeru navigacije po stranici
class TestUserNavigation(TestCase):
    
    def test_navigation_flow(self):

        response = self.client.get(reverse('main:mainpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainpage.html')
        
        
        response = self.client.get(reverse('main:dnevnik'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/journalentry_list.html')
        
        response = self.client.get(reverse('main:lijekovi'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/lijekovi_list.html')

        response = self.client.get(reverse('main:klijek'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/korisniklijek_list.html')

        response = self.client.get(reverse('main:raspolozenje'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/raspolozenje_list.html')

#TEST za projveru uspješnosti prijave korisnika
class TestUserLogin(TestCase):

    def setUp(self):
        self.username = 'test2'
        self.password = 'nikola12!'
        self.user = User.objects.create_user(username=self.username, password=self.password)


    def test_login_view(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {'username': self.username, 'password': self.password}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
