from django.urls import path,include
from .views import client_register
urlpatterns = [
   
    path("",client_register,name="user_register"),
]