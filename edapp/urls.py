from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("problem", views.problem, name="problem"),
    path("current-solutions", views.solutions, name="solutions"),
    path("how-you-can-help", views.help, name="help")
]