from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return render(request, 'dashboard.html')


def products_page(request):
    return render(request, "products.html")


def signup_page(request):
    return HttpResponse("<h1>Add signup file</h1>")


def dashboard_page(request):
    return HttpResponse("<h1>add dashboard file</h1>")


def create_post_page(request):
    return HttpResponse("<h1>Add profile file</h1>")


def profile_page(request):
    return HttpResponse("<h1>Add profile file</h1>")
