from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns=[
    path('home2/',home2,name='home2')

]