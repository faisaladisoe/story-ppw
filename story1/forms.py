from django import forms
from .models import Course
from django.forms import ModelForm

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    course_name = forms.CharField(
        required = True,
        max_length = 150,
        widget = forms.TextInput(
            attrs = {
                'id' : 'course-name',
                'class' : 'form-control',
                'placeholder' : 'input your course name here',
                'autocomplete' : 'off',
            }
        )
    )

    lecturer = forms.CharField(
        required = True,
        max_length = 150,
        widget = forms.TextInput(
            attrs = {
                'id' : 'lecturer',
                'class' : 'form-control',
                'placeholder' : 'input your lecturer name here',
                'autocomplete' : 'off',
            }
        )
    )

    credits = forms.IntegerField(
        required = True,
        widget = forms.NumberInput(
            attrs = {
                'id' : 'credits',
                'class' : 'form-control',
                'placeholder' : 'input the credits of your course here',
                'autocomplete' : 'off',
            }
        )
    )

    description = forms.CharField(
        required = True,
        max_length = 250,
        widget = forms.Textarea(
            attrs = {
                'id' : 'description',
                'class' : 'form-control',
                'placeholder' : 'input the description about your course here',
                'autocomplete' : 'off',
            }
        )
    )

    TERM_CHOICES = (
        ('odd', 'odd'),
        ('even', 'even')
    )
    term = forms.ChoiceField(
        required = True,
        choices = TERM_CHOICES,
        widget = forms.Select(
            attrs = {
                'id' : 'term',
                'class' : 'form-control',
                'placeholder' : 'input the terms of the course here',
                'autocomplete' : 'off',
            }
        )
    )

    ACADEMIC_YEAR = (
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022')
    )
    academic_year = forms.ChoiceField(
        required = True,
        choices = ACADEMIC_YEAR,
        widget = forms.Select(
            attrs = {
                'id' : 'academic-year',
                'class' : 'form-control',
                'placeholder' : 'input the academic year of the course here',
                'autocomplete' : 'off',
            }
        )
    )

    room = forms.CharField(
        required = True,
        max_length = 20,
        widget = forms.TextInput(
            attrs = {
                'id' : 'room',
                'class' : 'form-control',
                'placeholder' : 'input the room number of the course here',
                'autocomplete' : 'off',
            }
        )
    )
    