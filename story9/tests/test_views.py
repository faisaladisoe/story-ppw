from http import HTTPStatus
from django.test import TestCase, Client
from story9.views import userRegister, userLogin, userLogout

# Create your tests here.
class story9ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.register = '/register/'
        cls.login = '/login/'
        cls.logout = '/logout/'
    
    def test_userRegister_success(self):
        response = self.client.post(self.register, {
            'username': 'faisaladisoe',
            'email': 'muhammad.faisal95@ui.ac.id',
            'password1': 'ayokitajoggingdulu',
            'password2': 'ayokitajoggingdulu'
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'story9/login.html')
    
    def test_userRegister_fail(self):
        response = self.client.post(self.register, {
            'username': '123+qwert``~~',
            'email': 'muhammad.faisal95@ui.ac.id',
            'password1': 'woiburuankerjainnya',
            'password2': 'woiburuankerjainnya'
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'story9/register.html')
    
    def test_userLogin_success(self):
        create = self.client.post(self.register, {
            'username': 'faisaladisoe',
            'email': 'muhammad.faisal95@ui.ac.id',
            'password1': 'ayokitajoggingdulu',
            'password2': 'ayokitajoggingdulu'
        }, follow = True)
        response = self.client.post(self.login, {
            'username': 'faisaladisoe',
            'password': 'ayokitajoggingdulu'
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_userLogin_fail(self):
        create = self.client.post(self.register, {
            'username': 'faisaladisoe',
            'email': 'muhammad.faisal95@ui.ac.id',
            'password1': 'ayokitajoggingdulu',
            'password2': 'ayokitajoggingdulu'
        }, follow = True)
        response = self.client.post(self.login, {
            'username': 'faisaladi',
            'password': 'ayokitajoggingdulu'
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_userLogout(self):
        usercreate = self.client.post(self.register, {
            'username': 'faisaladisoe',
            'email': 'muhammad.faisal95@ui.ac.id',
            'password1': 'ayokitajoggingdulu',
            'password2': 'ayokitajoggingdulu'
        }, follow = True)
        usercreate.client.login(username='faisaladisoe', password='ayokitajoggingdulu')
        response = self.client.get(self.logout, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_userAuthentication(self):
        usercreate = self.client.post(self.register, {
            'username': 'faisaladisoe',
            'email': 'muhammad.faisal95@ui.ac.id',
            'password1': 'ayokitajoggingdulu',
            'password2': 'ayokitajoggingdulu'
        }, follow = True)
        usercreate.client.login(username='faisaladisoe', password='ayokitajoggingdulu')
        registerResponse = self.client.get(self.register, follow = True)
        loginResponse = self.client.get(self.login, follow = True)
        self.assertEqual(registerResponse.status_code, HTTPStatus.OK)
        self.assertEqual(loginResponse.status_code, HTTPStatus.OK)
        self.assertRedirects(registerResponse, '/')
        self.assertRedirects(loginResponse, '/')
