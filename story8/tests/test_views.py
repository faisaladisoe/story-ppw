from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import resolve
from story8.views import bookCollection, jsonResult

# Create your tests here.
class story8ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.jsonResult = '/jsonResult/'
        cls.bookCollection = '/bookCollection/'

    def test_bookCollection_status_path(self):
        response = self.client.get(self.bookCollection)
        self.assertTemplateUsed(response, 'bookCollection.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_jsonResult_status_path(self):
        response = self.client.get(self.jsonResult)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_bookCollection_functionName(self):
        response = resolve(self.bookCollection)
        self.assertEqual(response.func, bookCollection)
    
    def test_jsonResult_functionName(self):
        response = resolve(self.jsonResult)
        self.assertEqual(response.func, jsonResult)

    def test_jsonResult_returnValue(self):
        path = '/bookCollection?q=Trump/'
        response = self.client.get(path)
        self.assertEqual(response.status_code, 301)
