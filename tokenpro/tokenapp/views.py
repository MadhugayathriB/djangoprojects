from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken,TokenAuthentication
from knox.auth import get_authorization_header
from .serializers import Registerserializer


def serialize_user(user):
    return {
        "username": user.username,
        "password":user.password,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }



@api_view(["POST"])
def login(request):
    serializer=AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.validated_data["user"]
    _, token=AuthToken.objects.create(user)
    return Response({
        "userinfo":serialize_user(user),
        "token":token
    })



@api_view(["POST"])
def register(request):
    serializer = Registerserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })
        
    
@api_view(["GET"])
def getuser(request):
    user=request.user
    if user.is_authenticated:
        return Response({
        "userinfo":serialize_user(user)})
    return Response({"error": "not authenticated"},status=400)


    




    
