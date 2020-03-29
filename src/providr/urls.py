"""providr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from providr_posts.views import (
#     user_post_detail_view,
#     user_post_list_view,
#     user_post_create_view
# )


from .views import (
    home_page,
    # login_page,
    # signup_page,
    # create_post_page,
    # profile_page,
    # example_page
)

urlpatterns = [
    # path('login/', login_page),
    # path('signup/', signup_page),
    # path('dashboard/create_post>', create_post_page),
    # path('profile/<str:user_id>', profile_page),
    # path('blog/', user_post_list_view),
    # path('blog-new/', user_post_create_view),
    # path('blog/<str:slug>/', user_post_detail_view),
    # path('example/', example_page),
    path('', home_page),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))

]
