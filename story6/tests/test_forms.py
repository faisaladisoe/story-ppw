from django.test import TestCase
from story6.forms import EventForm, VisitorForm

# Create your tests here.
class story6FormsTest(TestCase):
    def test_event_attribute_required(self):
        event_component = EventForm()
        event_attribute = event_component.fields['event'].required
        self.assertTrue(event_attribute)
    
    def test_event_attribute_max_length(self):
        event_component = EventForm()
        event_attribute = event_component.fields['event'].max_length
        self.assertEqual(event_attribute, 50)
    
    def test_event_attribute_widget_id(self):
        event_component = EventForm()
        event_attribute = event_component.fields['event'].widget.attrs['id']
        self.assertEqual(event_attribute, 'event')
    
    def test_event_attribute_widget_class(self):
        event_component = EventForm()
        event_attribute = event_component.fields['event'].widget.attrs['class']
        self.assertEqual(event_attribute, 'form-control')
    
    def test_event_attribute_widget_placeholder(self):
        event_component = EventForm()
        event_attribute = event_component.fields['event'].widget.attrs['placeholder']
        self.assertEqual(event_attribute, 'input your event here')

    def test_event_attribute_widget_autocomplete(self):
        event_component = EventForm()
        event_attribute = event_component.fields['event'].widget.attrs['autocomplete']
        self.assertEqual(event_attribute, 'off')
    
    def test_brief_description_attribute_required(self):
        event_component = EventForm()
        event_attribute = event_component.fields['brief_description'].required
        self.assertTrue(event_attribute)
    
    def test_brief_description_attribute_max_length(self):
        event_component = EventForm()
        event_attribute = event_component.fields['brief_description'].max_length
        self.assertEqual(event_attribute, 200)
    
    def test_brief_description_attribute_widget_id(self):
        event_component = EventForm()
        event_attribute = event_component.fields['brief_description'].widget.attrs['id']
        self.assertEqual(event_attribute, 'brief-description')
    
    def test_brief_description_attribute_widget_class(self):
        event_component = EventForm()
        event_attribute = event_component.fields['brief_description'].widget.attrs['class']
        self.assertEqual(event_attribute, 'form-control')
    
    def test_brief_description_attribute_widget_placeholder(self):
        event_component = EventForm()
        event_attribute = event_component.fields['brief_description'].widget.attrs['placeholder']
        self.assertEqual(event_attribute, 'share your event tagline (maximum 200 characters)')
    
    def test_brief_description_attribute_widget_autocomplete(self):
        event_component = EventForm()
        event_attribute = event_component.fields['brief_description'].widget.attrs['autocomplete']
        self.assertEqual(event_attribute, 'off')
    
    def test_complete_description_required(self):
        event_component = EventForm()
        event_attribute = event_component.fields['complete_description'].required
        self.assertTrue(event_attribute)
    
    def test_complete_description_max_length(self):
        event_component = EventForm()
        event_attribute = event_component.fields['complete_description'].max_length
        self.assertEqual(event_attribute, 2000)
    
    def test_complete_description_attribute_widget_id(self):
        event_component = EventForm()
        event_attribute = event_component.fields['complete_description'].widget.attrs['id']
        self.assertEqual(event_attribute, 'complete-description')
    
    def test_complete_description_attribute_widget_class(self):
        event_component = EventForm()
        event_attribute = event_component.fields['complete_description'].widget.attrs['class']
        self.assertEqual(event_attribute, 'form-control')

    def test_complete_description_attribute_widget_placeholder(self):
        event_component = EventForm()
        event_attribute = event_component.fields['complete_description'].widget.attrs['placeholder']
        self.assertEqual(event_attribute, 'tell us what\'s your event sounds like')
    
    def test_complete_description_attribute_widget_autocomplete(self):
        event_component = EventForm()
        event_attribute = event_component.fields['complete_description'].widget.attrs['autocomplete']
        self.assertEqual(event_attribute, 'off')
    
    def test_visitor_name_attribute_required(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_name'].required
        self.assertTrue(visitor_attribute)
    
    def test_visitor_name_attribute_max_length(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_name'].max_length
        self.assertEqual(visitor_attribute, 75)

    def test_visitor_name_attribute_widget_id(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_name'].widget.attrs['id']
        self.assertEqual(visitor_attribute, 'visitor-name')
    
    def test_visitor_name_attribute_widget_class(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_name'].widget.attrs['class']
        self.assertEqual(visitor_attribute, 'form-control')
    
    def test_visitor_name_attribute_widget_placeholder(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_name'].widget.attrs['placeholder']
        self.assertEqual(visitor_attribute, 'input your name here')
    
    def test_visitor_name_attribute_widget_autocomplete(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_name'].widget.attrs['autocomplete']
        self.assertEqual(visitor_attribute, 'off')

    def test_visitor_age_attribute_required(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_age'].required
        self.assertTrue(visitor_attribute)
    
    def test_visitor_age_attribute_max_length(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_age'].min_value
        self.assertEqual(visitor_attribute, 17)

    def test_visitor_age_attribute_widget_id(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_age'].widget.attrs['id']
        self.assertEqual(visitor_attribute, 'visitor-age')
    
    def test_visitor_age_attribute_widget_class(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_age'].widget.attrs['class']
        self.assertEqual(visitor_attribute, 'form-control')
    
    def test_visitor_age_attribute_widget_placeholder(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_age'].widget.attrs['placeholder']
        self.assertEqual(visitor_attribute, 'input your age here')
    
    def test_visitor_age_attribute_widget_autocomplete(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['visitor_age'].widget.attrs['autocomplete']
        self.assertEqual(visitor_attribute, 'off')
    
    def test_visitor_id_type_attribute_required(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['id_type'].required
        self.assertTrue(visitor_attribute)
    
    def test_visitor_id_type_attribute_max_length(self):
        visitor_component = VisitorForm()
        TYPES = [
            ('KTM', 'KTM'),
            ('KTP', 'KTP'),
            ('SIM', 'SIM'),
            ('Passport', 'Passport'),
        ]
        visitor_attribute = visitor_component.fields['id_type'].choices
        self.assertEqual(visitor_attribute, TYPES)

    def test_visitor_id_type_attribute_widget_id(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['id_type'].widget.attrs['id']
        self.assertEqual(visitor_attribute, 'id-type')

    def test_identity_number_attribute_required(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['identity_number'].required
        self.assertTrue(visitor_attribute)
    
    def test_identity_number_attribute_max_length(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['identity_number'].max_length
        self.assertEqual(visitor_attribute, 75)

    def test_identity_number_attribute_widget_id(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['identity_number'].widget.attrs['id']
        self.assertEqual(visitor_attribute, 'identity-number')
    
    def test_identity_number_attribute_widget_class(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['identity_number'].widget.attrs['class']
        self.assertEqual(visitor_attribute, 'form-control')
    
    def test_identity_number_attribute_widget_placeholder(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['identity_number'].widget.attrs['placeholder']
        self.assertEqual(visitor_attribute, 'input your identity number here')
    
    def test_identity_number_attribute_widget_autocomplete(self):
        visitor_component = VisitorForm()
        visitor_attribute = visitor_component.fields['identity_number'].widget.attrs['autocomplete']
        self.assertEqual(visitor_attribute, 'off')
    