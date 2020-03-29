from django.contrib import admin
from django.urls import path, include
from .views import signup_view, login_view

urlpatterns = [
    path('signup/', signup_view),
    path('login/', login_view),
    path('tester/', login_view)
]