from django import forms
from django.forms import ModelForm
from .models import Parcel 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class ParcelForm(ModelForm):
  class Meta:
    model = Parcel
    fields = '__all__'
    exclude = ['host']

