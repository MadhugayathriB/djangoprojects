from django.http import JsonResponse
from django.shortcuts import render
from .models import methodsmodel
from .serializers import methodsserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET","POST"])
def methods(request):
    if request.method =="GET":
        method=methodsmodel.objects.all()
        serializer=methodsserializer(method,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method=="POST":
        serializer=methodsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        
        
@api_view(["PUT","GET","DELETE"])
def methods_id(request,id):
    try:
        method=methodsmodel.objects.get(pk=id)
    except method.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=methodsserializer(method)
        return JsonResponse(serializer.data)
    if request.method=="PUT":
        serializer=methodsserializer(method,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        method.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        

        



