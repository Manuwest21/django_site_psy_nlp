from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    birthdate = forms.DateField()
    
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "birthdate", "email"]