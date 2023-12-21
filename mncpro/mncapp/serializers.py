from rest_framework import serializers
from .models import mncmodel
class mncserializer(serializers.ModelSerializer):
    class Meta:
        model=mncmodel
        fields=["id","name","ceo","address","Industry"]