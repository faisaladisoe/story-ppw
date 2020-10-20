from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import resolve, reverse
from story6.models import Event, Visitor

# Create your tests here.
class story6ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.test_event = Event.objects.create(
            event = 'Campus Fair',
            brief_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            complete_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
        )
        cls.test_visitor = Visitor.objects.create(
            visitor_name = 'Muhammad Faisal Adi Soesatyo',
            visitor_age = 19,
            id_type = 'SIM',
            identity_number = '123456789',
            event = cls.test_event
        )
        cls.event_url = '/events/'
        cls.addEvent_url = '/events/addEvents/'
        cls.deleteEvents_url = '/events/deleteEvents/%d/' % cls.test_event.id
        cls.eventDetails_url = '/events/eventDetails/%d/' % cls.test_event.id
        cls.registerVisitor_url = '/events/registerVisitor/%d/' % cls.test_visitor.id
        cls.updateVisitor_url = '/events/updateVisitor/%d/' % cls.test_visitor.id
        cls.deleteVisitor_url = '/events/deleteVisitor/%d/' % cls.test_visitor.id
    
    def test_event_url_GET(self):
        response = self.client.get(self.event_url)
        self.assertTemplateUsed(response, 'story6/events.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_add_event_url_GET(self):
        response = self.client.get(self.addEvent_url)
        self.assertTemplateUsed(response, 'story6/addEvents.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_delete_event_url_GET(self):
        response = self.client.get(self.deleteEvents_url)
        self.assertTemplateUsed(response, 'story6/deleteEvents.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_event_details_url_GET(self):
        response = self.client.get(self.eventDetails_url)
        self.assertTemplateUsed(response, 'story6/eventDetails.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_register_visitor_url_GET(self):
        response = self.client.get(self.registerVisitor_url)
        self.assertTemplateUsed(response, 'story6/registerVisitor.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_updateVisitor_url_GET(self):
        response = self.client.get(self.updateVisitor_url)
        self.assertTemplateUsed(response, 'story6/updateVisitor.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_deleteVisitor_url_GET(self):
        response = self.client.get(self.deleteVisitor_url)
        self.assertTemplateUsed(response, 'story6/deleteVisitor.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_events_url_POST(self):
        response = self.client.post(self.addEvent_url, {
            'event' : 'Campus Fair',
            'brief_description' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'complete_description' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_delete_events_url_POST(self):
        response = self.client.post(self.deleteEvents_url, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_register_visitor_url_POST(self):
        response = self.client.post(self.registerVisitor_url, {
            'visitor_name' : 'Muhammad Faisal Adi Soesatyo',
            'visitor_age' : 19,
            'id_type' : 'SIM',
            'identity_number' : '123456789',
            'event' : self.test_event
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_delete_visitor_url_POST(self):
        response = self.client.post(self.deleteVisitor_url, follow = True)
        self.assertEquals(response.status_code, HTTPStatus.OK)
    
    def test_update_visitor_url_POST(self):
        response = self.client.post(self.updateVisitor_url, {
            'visitor_name' : 'Muhammad Faisal Adi Soesatyo',
            'visitor_age' : 19,
            'id_type' : 'SIM',
            'identity_number' : '123456789',
            'event' : self.test_event
        }, follow = True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    