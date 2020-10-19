from django import forms
from django.forms import ModelForm
from .models import Course
# from .views import registerVisitor

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
    
# class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = '__all__'
    
#     event = forms.CharField(
#         required = True,
#         max_length = 50,
#         widget = forms.TextInput(
#             attrs = {
#                 'id' : 'event',
#                 'class' : 'form-control',
#                 'placeholder' : 'input your event here',
#                 'autocomplete' : 'off',
#             }
#         )
#     )

#     brief_description = forms.CharField(
#         required = True,
#         max_length = 200,
#         widget = forms.TextInput(
#             attrs = {
#                 'id' : 'brief-description',
#                 'class' : 'form-control',
#                 'placeholder' : 'share your event tagline (maximum 200 characters)',
#                 'autocomplete' : 'off',
#             }
#         )
#     )

#     complete_description = forms.CharField(
#         required = True,
#         max_length = 1000,
#         widget = forms.Textarea(
#             attrs = {
#                 'id' : 'complete-description',
#                 'class' : 'form-control',
#                 'placeholder' : 'tell us what\'s your event sounds like',
#                 'autocomplete' : 'off',
#             }
#         )
#     )

# class VisitorForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = '__all__'
    
#     visitor_name = forms.CharField(
#         required = True,
#         max_length = 75,
#         widget = forms.TextInput(
#             attrs = {
#                 'id' : 'visitor-name',
#                 'class' : 'form-control',
#                 'placeholder' : 'input your name here',
#                 'autocomplete' : 'off',
#             }
#         )
#     )

#     visitor_age = forms.IntegerField(
#         required = True,
#         min_value = 17,
#         widget = forms.NumberInput(
#             attrs = {
#                 'id' : 'visitor-age',
#                 'class' : 'form-control',
#                 'placeholder' : 'input your age here',
#                 'autocomplete' : 'off',
#             }
#         )
#     )

#     TYPES = (
#         ('KTM', 'KTM'),
#         ('KTP', 'KTP'),
#         ('SIM', 'SIM'),
#         ('Passport', 'Passport'),
#     )
#     id_type = forms.ChoiceField(
#         required = True,
#         choices = TYPES,
#         widget = forms.Select(
#             attrs = {
#                 'id' : 'id-type',
#             }
#         )
#     )

#     identity_number = forms.CharField(
#         required = True,
#         max_length = 75,
#         widget = forms.TextInput(
#             attrs = {
#                 'id' : 'identity-number',
#                 'class' : 'form-control',
#                 'placeholder' : 'input your identity number here',
#                 'autocomplete' : 'off',
#             }
#         )
#     )
