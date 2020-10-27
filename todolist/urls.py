"""
@author mdark1001 | Miguel Cabrera R. <miguel.cabrera.app@gmail.com>
@date 26/10/20
@project 
@name urls
"""
from django.urls import path
from .views import home
urlpatterns=[
    path('',home,name='home')
]