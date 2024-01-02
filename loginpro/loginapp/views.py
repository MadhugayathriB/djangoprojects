from django.shortcuts import redirect, render
from .models import register,login
from django.http import HttpResponse

# Create your views here.
def registerreq(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        regis=register(username=username,password=password)
        regis.save()
    return render(request,"register.html")
def loginreq(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        log=login(username=username,password=password)
        log.save()
    logs=login.objects.all()
    regs=register.objects.all()

    return render(request,"login.html",{"logs":logs},{"regs":regs})
