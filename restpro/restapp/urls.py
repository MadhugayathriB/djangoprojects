from .import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("",views.restapp,name="restapp"),
    path("data",views.data,name="restapp")
]