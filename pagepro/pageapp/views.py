from django.shortcuts import render,redirect
from django.views import View
from .models import enter
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        ent=enter.objects.all()
        for i in ent:
            if username==i.username and password==i.password:
                return redirect(dashboard)
            

    return render(request,"login.html")

def home(request):
    
    return render(request,"home.html")
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        data=enter(username=username,password=password)
        data.save()
        
        return redirect(home)
    return render(request,"register.html")

def dashboard(request):
    if request.method=="POST":
        return redirect(home)
    return render(request,"dashboard.html")    
        