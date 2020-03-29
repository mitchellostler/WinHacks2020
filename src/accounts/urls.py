from django.urls import path
from . import views


urlpatterns = [

    path('dashboard/', views.dashboard_page),
    path('items/', views.items),
    path('donators/', views.donators)


]
