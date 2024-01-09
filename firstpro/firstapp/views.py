from django.shortcuts import render
from django.http import HttpResponse

from firstapp.models import employee

# Create your views here.
def firstapp(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        salary=request.POST["salary"]
        age=request.POST["age"]
        gender=request.POST["gender"]
        domain=request.POST["domain"]
        comapny=request.POST["comapny"]
        email=request.POST["email"]
        experience=request.POST["experience"]
        emplo=employee(fname=fname,lname=lname,salary=salary,age=age,gender=gender,domain=domain,comapny=comapny,email=email,experience=experience)
        emplo.save()
    emp=employee.objects.all()
    return render(request,"index.html",{"employees":emp})