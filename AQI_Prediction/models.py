from pickle import TRUE
from django.db import models

# Create your models here.

class Users(models.Model):
    Date=models.DateField(auto_now_add=True)
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    MobileNo=models.CharField(max_length=10,primary_key=True)
    EmailId=models.CharField(max_length=50,unique= True)
    UserName=models.CharField(max_length=30,unique=True)
    Password=models.CharField(max_length=30)


class Data(models.Model):
    Date=models.DateField(auto_now_add=True)
    City=models.CharField(max_length=20)
    Avg_temp=models.FloatField()
    Max_temp=models.FloatField()
    Min_temp=models.FloatField()
    Humidity=models.FloatField()
    Visibility=models.FloatField()
    Wind_speed=models.FloatField() 
    Suspended_windspeed=models.FloatField()
    PM25=models.FloatField()
    

 