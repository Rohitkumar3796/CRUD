from django.contrib import admin
from django.urls import path,include
from register.views import *

urlpatterns = [
    path('',showEmpdata,name="show"),
    path('add/',empRegister, name="add"),
    path('<int:id>/',edit, name="edit-data"),
    path('delete/',delete, name="delete"),


]