from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Users.models import MyUser


class SignUpForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'fname', 'lname', 'password')

    email = forms.EmailField(required = True, widget=forms.TextInput(
        attrs={'class':"form-control", 'type':"text", 'placeholder':"Email"}))
    
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'type':"text", 'placeholder':"Username"}))

    fname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'type':"text", 'placeholder':"First Name"}))

    lname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'type':"text", 'placeholder':"Last Name"}))

    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'type':"text", 'placeholder':"Password"}))
    

    

