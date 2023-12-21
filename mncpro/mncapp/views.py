from django.http import JsonResponse
from django.shortcuts import render
from .models import mncmodel
from .serializers import mncserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your vie
@api_view(["GET","POST"])
def mncs(request):
    if request.method=="GET":
        mnc=mncmodel.objects.all()
        serializer=mncserializer(mnc,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method=="POST":
        serializer=mncserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(["GET","PUT","DELETE"])
def mnc_id(request,id):
    try:
        mnc=mncmodel.objects.get(pk=id)
    except mnc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=mncserializer(mnc)
        return JsonResponse(serializer.data)
    if request.method=="PUT":
        serializer=mncserializer(mnc,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        mnc.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)