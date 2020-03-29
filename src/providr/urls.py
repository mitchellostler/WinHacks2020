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
from django.urls import path, re_path, include

# importing functions from the component(mini-application views)

# importing the require functions from the project vierws
from .views import (
    home_page,
    # about_page,
    # contact_page
)

#urlpatterns = [
    # path('login/', login_page),
    # path('signup/', signup_page),
    # path('dashboard/<str:user_id>', dashboard_page),
    # path('dashboard/create_post>', create_post_page),
    # path('profile/<str:user_id>', profile_page),

from providr_posts.views import (
    user_post_create_view
    )


urlpatterns = [
    
    path('', home_page),
    path('users/', include('Users.urls')),
    path('post-new/', user_post_create_view),
    path('post/', include('providr_posts.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))

]
