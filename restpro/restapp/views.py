from django.shortcuts import render
from django.http import HttpResponse

from restapp.models import restuarant
from django.views.decorators.csrf import csrf_protect




# Create your views here.
@csrf_protect
def restapp(request):
    if request.method=="POST":
        name=request.POST["name"]
        foodordered=request.POST["foodordered"]
        favouritedish=request.POST["favouritedish"]
        review=request.POST["review"]
        rest=restuarant(name=name,foodordered=foodordered,favouritedish=favouritedish,review=review)
        rest.save()
    
    return render (request,"index.html")
def data(request):
    res=restuarant.objects.all()
    return render (request,"data.html",{"reviews":res})