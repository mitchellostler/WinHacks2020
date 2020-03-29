from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm



def home_page(request):
    return render(request, "landing.html")


# def login_page(request):
#     return HttpResponse("<h1>Add login file</h1>")


# def signup_page(request):
#     return HttpResponse("<h1>Add signup file</h1>")


# def dashboard_page(request):
#     return HttpResponse("<h1>add dashboard file</h1>")


# def create_post_page(request):
#     return HttpResponse("<h1>Add profile file</h1>")


# def profile_page(request):
#     return HttpResponse("<h1>Add profile file</h1>")


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "title": "Contact Us",
        "form" : form
        }
    return render(request, "form.html", context)

def example_page(request):
    context = {"title": "Example"}
    template_name = "home.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)

    #this is a test for backup
