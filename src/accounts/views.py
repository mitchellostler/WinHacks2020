from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import *
from providr_posts.models import UserPost



# def signup_view(request):
#     form = UserCreationForm()
#     render(request, 'signuptest.html')



def dashboard_page(request):

    # Finding the total amount of donations

    donations = Donate.objects.all()
    donators = Donator.objects.all()

    total_donators = donators.count()
    total_donations = donations.count()
    qs = UserPost.objects.all()
    # for(UserPost)

    # Filtering items that have been delivered

    delivered = donations.filter(status="Delivered").count()
    pending = donations.filter(status="Pending").count()

    context = {'donations': donations, 'donators': donators,
               "total_donators": total_donators, "total_donations": total_donations, "delivered": delivered, "pending": pending, }

    return render(request, 'accounts/dashboard.html', context)


def items(request):
    items = Item.objects.all()
    return render(request, "accounts/items.html", {"items": items})


def donators(request):
    return render(request, "accounts/donators.html")
