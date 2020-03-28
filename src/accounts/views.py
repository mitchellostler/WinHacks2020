from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    form = UserCreationForm()
    render(request, 'signuptest.html')
# Create your views here.
