from django.db import models
from django import forms

# Create your models here.
class MyUser(models.Model):
    email     = models.EmailField(max_length=30, blank=True)
    username  = models.CharField(max_length=20, blank=True, unique=True)
    password  = models.CharField(max_length=20, blank=True)
    fname     = models.CharField(max_length=20, blank=True)
    lname     = models.CharField(max_length=20, blank=True)
    address   = models.CharField(max_length=40, blank=True)

class Login(models.Model):
    username  = models.CharField(max_length=20, blank=True, unique=True)
    password  = models.CharField(max_length=20)
