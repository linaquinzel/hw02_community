from django.urls import path

from . import views

urlpatterns = [
    path("posts", views.group_posts, name="posts"),
    path("", views.index, name="index"),
]
