from django.test import TestCase
from story6.models import Event, Visitor

# Create your tests here.
class story6ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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
    
    def test_event_label(self):
        event_name = Event.objects.get(id = 1)
        field_label = event_name.event
        self.assertEqual(field_label, 'Campus Fair')
    
    def test_event_brief_description_label(self):
        brief_description_content = Event.objects.get(id = 1)
        field_label = brief_description_content.brief_description
        self.assertEqual(field_label, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

    def test_event_complete_description_label(self):
        complete_description_content = Event.objects.get(id = 1)
        field_label = complete_description_content.complete_description
        self.assertEqual(field_label, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')

    def test_event_max_length(self):
        event_name = Event.objects.get(id = 1)
        max_length = event_name._meta.get_field('event').max_length
        self.assertEqual(max_length, 50)

    def test_event_brief_description_max_length(self):
        brief_description_content = Event.objects.get(id = 1)
        max_length = brief_description_content._meta.get_field('brief_description').max_length
        self.assertEqual(max_length, 200)

    def test_event_complete_description_max_length(self):
        complete_description_content = Event.objects.get(id = 1)
        max_length = complete_description_content._meta.get_field('complete_description').max_length
        self.assertEqual(max_length, 2000)

    def test_event_str_label(self):
        event_name = Event.objects.get(id = 1)
        expected_event_name = f'{event_name.event}'
        self.assertEqual(expected_event_name, str(event_name))
    
    def test_visitor_name_label(self):
        visitor_name_content = Visitor.objects.get(id = 1)
        field_label = visitor_name_content.visitor_name
        self.assertEqual(field_label, 'Muhammad Faisal Adi Soesatyo')

    def test_visitor_age_label(self):
        visitor_content = Visitor.objects.get(id = 1)
        field_label = visitor_content.visitor_age
        self.assertEqual(field_label, 19)

    def test_visitor_id_type_label(self):
        visitor_content = Visitor.objects.get(id = 1)
        field_label = visitor_content.id_type
        self.assertEqual(field_label, 'SIM')
    
    def test_visitor_identity_number_label(self):
        visitor_content = Visitor.objects.get(id = 1)
        field_label = visitor_content.identity_number
        self.assertEqual(field_label, '123456789')
    
    def test_visitor_event_registered_label(self):
        visitor_content = Visitor.objects.get(id = 1)
        field_label = visitor_content.event.event
        self.assertEqual(field_label, 'Campus Fair')

    def test_visitor_name_max_length(self):
        visitor_name_content = Visitor.objects.get(id = 1)
        max_length = visitor_name_content._meta.get_field('visitor_name').max_length
        self.assertEqual(max_length, 75)
    
    def test_visitor_id_type_max_length(self):
        visitor_content = Visitor.objects.get(id = 1)
        max_length = visitor_content._meta.get_field('id_type').max_length
        self.assertEqual(max_length, 10)

    def test_visitor_identity_number_max_length(self):
        visitor_content = Visitor.objects.get(id = 1)
        max_length = visitor_content._meta.get_field('identity_number').max_length
        self.assertEqual(max_length, 75)
    
    def test_visitor_str_label(self):
        visitor_content = Visitor.objects.get(id = 1)
        expected_visitor_name = f'{visitor_content.visitor_name}'
        self.assertEqual(expected_visitor_name, str(visitor_content))
