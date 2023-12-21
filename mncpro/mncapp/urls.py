
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns= [
    path("mncs",views.mncs),
    path("mncid/<int:id>",views.mnc_id)
]