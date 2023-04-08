from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    login = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)