from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    username = forms.CharField(
        required = True,
        max_length = 150,
        widget = forms.TextInput(
            attrs = {
                'id' : 'username-field',
                'class' : 'form-control',
                'name' : 'username',
                'placeholder' : 'input your username here',
                'autocomplete' : 'off',
            }
        )
    )

    email = forms.EmailField(
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'id' : 'email-field',
                'class' : 'form-control',
                'name' : 'email',
                'placeholder' : 'input your email here',
                'autocomplete' : 'off',
            }
        )
    )

    password1 = forms.CharField(
        required = True,
        min_length = 8,
        widget = forms.PasswordInput(
            attrs = {
                'id' : 'password-field',
                'class' : 'form-control',
                'name' : 'password',
                'placeholder' : 'input your password here',
                'autocomplete' : 'off',
            }
        )
    )

    password2 = forms.CharField(
        required = True,
        min_length = 8,
        widget = forms.PasswordInput(
            attrs = {
                'id' : 'password_validation-field',
                'class' : 'form-control',
                'name' : 'passwordValidation',
                'placeholder' : 're-type your password here',
                'autocomplete' : 'off',
            }
        )
    )
