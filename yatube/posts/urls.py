from django.urls import path

from . import views

urlpatterns = [
    path("group/<slug:slug>/", views.group_posts, name="group"),
    path("posts", views.group_posts, name="posts"),
    path("", views.index, name="index"),
]
