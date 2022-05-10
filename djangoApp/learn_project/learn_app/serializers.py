from rest_framework import serializers
from .models import Kucharz,Potrawa
class KucharzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kucharz
        fields = ('age','name')
class PotrawaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Potrawa
        fields = ('name','smak','powi')