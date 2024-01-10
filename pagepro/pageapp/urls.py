from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("home",views.home),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("dashboard",views.dashboard)
]
