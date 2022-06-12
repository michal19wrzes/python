from .models import UserAccount
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ['id', 'name', 'email','password',]
        read_only_fields = ['is_active', 'is_staff',]
    
    def create(self, validated_data):
        user = super(UserSerializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user