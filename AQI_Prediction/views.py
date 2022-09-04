
from ast import Return
from utils.webscrap import webscrapping
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView , CreateAPIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime



# Create your views here.

"""
def home(request):
    return render(request,'index.html')
"""






class UserCreateView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

 


class UserLoginView(APIView):
  def post(self, request, format=None):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    UserName = serializer.data.get('UserName')
    Password = serializer.data.get('Password')
    user = Users.objects.filter(UserName=UserName , Password=Password).values()
    if not user:
        return Response({'errors':{'non_field_errors':['User Name or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({ 'msg':'Login Success'}, status=status.HTTP_200_OK)

City=""




class DataView(APIView):
    def get( self , request , pk = None, format=None):
        City = pk
        if City is not None:
            if City == "rourkela":
                City='rourkela-privat'
            Date = datetime.date.today()
            Datas = Data.objects.filter(City=City, Date=Date).values()
            if not Datas:
                obj = webscrapping(City.lower())
                re = obj.WebscrapData()
                newdata = Data(Date=Date,City=City,Avg_temp=re['Avg_temp'],Max_temp=re['Max_temp'],Min_temp=re['Min_temp'],Humidity=re['Humidity'],Visibility=re['Visibility'],Wind_speed=re['Wind_speed'],Suspended_windspeed=re['Suspended_windspeed'],PM25=re['PM25'])
                newdata.save()
                Datas = Data.objects.filter(City=City, Date=Date).values()
                return Response(Datas)
            else :
                return Response (Datas)
        else:
            Datas = Data.objects.last()

            return Response (Datas)




        
    
    


    
    
    
    
    


