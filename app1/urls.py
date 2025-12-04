from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.hola),
    path("hello/", views.hello),
    path("index/", views.index),
    path("home/", views.home),
    path("casa/", views.casa),
]