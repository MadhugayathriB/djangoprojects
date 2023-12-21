from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def myapp(request):
    if request.method=="POST":
        city=request.POST.get("city")
        apiurl=urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=d19fd2aec668813f11d65736c3201b0c").read()
        second=json.loads(apiurl)
        

        print(second)
        data={
            "city":city,
            "desc":second["weather"][0]["description"],
            "temp":second["main"]["temp"],
            "humidity":second["main"]["humidity"],
            "icon":second["weather"][0]["icon"]
        }
    else:
        data={
            "city":None,
            "desc":None,
            "temp":None,
            "humidity":None,
            "icon":None
        }

    
    return render(request,"index.html",{"data":data})
