from django.contrib.auth.models import User
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
# serializers.py
from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
