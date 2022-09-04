from django.contrib import admin
from .models import Users , Data

# Register your models here.


@admin.register(Users)


class RegisterProduct(admin.ModelAdmin):
    list_display = ('Date','FirstName','LastName','MobileNo','EmailId','UserName','Password')



@admin.register(Data)


class RegisterProduct(admin.ModelAdmin):
    list_display = ('Date','City','Avg_temp','Max_temp','Min_temp','Humidity','Visibility','Wind_speed','Suspended_windspeed','PM25')