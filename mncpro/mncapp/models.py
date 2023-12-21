from django.db import models

# Create your models here.
class mncmodel(models.Model):
    name=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Industry=models.CharField(max_length=100)