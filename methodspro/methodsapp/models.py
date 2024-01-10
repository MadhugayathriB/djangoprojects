from django.db import models

# Create your models here.
class methodsmodel(models.Model):
    company=models.CharField(max_length=100)
    establishedyear=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    

