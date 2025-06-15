from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('full_name', 'email', 'bio')