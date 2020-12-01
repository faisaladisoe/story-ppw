from django import forms
from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    
    bookName = forms.CharField(
        required = True,
        max_length = 50,
        widget = forms.TextInput(
            attrs = {
                'id' : 'book',
                'class' : 'form-control',
                'placeholder' : 'input title of your book here',
                'autocomplete' : 'off',
                'onchange' : 'submit();'
            }
        )
    )