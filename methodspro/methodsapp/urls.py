
from django.urls import path,include
from .import views

urlpatterns = [
    path("methods",views.methods),
    path("methods/<int:id>",views.methods_id)

    
]