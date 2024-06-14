from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CarForm(forms.ModelForm):
    class Meta:
        model= Car
        fields='__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model =brand
        fields="__all__"


class registerForm(UserCreationForm):

    class Meta:
        model =  User
        fields = ['username' , 'first_name', 'last_name', 'email']


class CommentForm(forms.ModelForm):
    class Meta:
        model= comment
        fields=['name','body']


class ChangeUserForm(UserChangeForm):
    password=None
    
    class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name', 'email']