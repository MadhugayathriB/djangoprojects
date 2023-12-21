from django.db import models

# Create your models here.
class restuarant(models.Model):
    name=models.CharField(max_length=50)
    foodordered=models.CharField(max_length=100)
    favouritedish=models.CharField(max_length=100)
    review=models.CharField(max_length=500)