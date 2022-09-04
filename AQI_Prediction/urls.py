from django import views
from django.urls import path 
from AQI_Prediction import views


urlpatterns = [            

        path('signup/', views.UserCreateView.as_view()),
        path('login/', views.UserLoginView.as_view()),
        path('data/<str:pk>/', views.DataView.as_view())

]