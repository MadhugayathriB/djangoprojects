from django.db import models

# Create your models here.
class employee(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    domain=models.CharField(max_length=50)
    comapny=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)