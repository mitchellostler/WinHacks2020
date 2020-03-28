from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
	return render(request,"home.html")

def login_page(request):
	return HttpResponse("<h1>Add login file</h1>")

def signup_page(request):
	return HttpResponse("<h1>Add signup file</h1>")

def dashboard_page(request):
	return HttpResponse("<h1>add dashboard file</h1>")

def create_post_page(request):
    return HttpResponse("<h1>Add profile file</h1>")

def profile_page(request):
	return HttpResponse("<h1>Add profile file</h1>")

<<<<<<< HEAD
def example_page(request):
    context = {"title": "Example"}
    template_name = "home.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
=======
    #this is a test for backup
>>>>>>> backup
