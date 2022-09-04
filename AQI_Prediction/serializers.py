
from dataclasses import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['Date','FirstName','LastName','MobileNo','EmailId','UserName','Password']



  


class LoginSerializer(serializers.ModelSerializer):
    UserName = serializers.CharField(max_length=30)
    class Meta:
        model = Users
        fields = ['UserName','Password']





class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['Max_temp','Min_temp','Humidity','Wind_speed','Suspended_windspeed']