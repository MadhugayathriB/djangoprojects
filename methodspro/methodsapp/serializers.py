from rest_framework import serializers
from .models import methodsmodel
class methodsserializer(serializers.ModelSerializer):
    class Meta:
        model=methodsmodel
        fields=["id","company","establishedyear","ceo"]