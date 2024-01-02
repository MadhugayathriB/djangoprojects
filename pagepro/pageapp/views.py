from django.shortcuts import render,redirect
from .models import enter
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        ent=enter.objects.all()
        for i in ent:
            if username==i.username and password==i.password:
                return render(request,"dashboard.html")
            else:
                return render(request,"home.html")

    return render(request,"login.html")
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        data=enter(username=username,password=password)
        data.save()
        
        return render(request,"home.html")
    return render(request,"register.html")
def dashboard(request):
    return render(request,"dashboard.html")