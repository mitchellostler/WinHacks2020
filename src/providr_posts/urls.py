
from django.urls import path
from providr_posts.views import (
    user_post_detail_view,
    user_post_list_view,
    user_post_update_view,
    user_post_delete_view
    )

urlpatterns = [
    path('', user_post_list_view),
    path('<str:slug>/delete/', user_post_delete_view),
    path('<str:slug>/edit/', user_post_update_view),
    path('<str:slug>/', user_post_detail_view)
]