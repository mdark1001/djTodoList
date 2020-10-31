"""
@author mdark1001 | Miguel Cabrera R. <miguel.cabrera.app@gmail.com>
@date 26/10/20
@project 
@name urls
"""
from django.urls import path

from .views import home, ListTasksView,CreateTaskView

urlpatterns = [
    path('', ListTasksView.as_view(), name='home'),
    path('detail/<int:pk>', home, name='detail'),
    path('create/', CreateTaskView.as_view(), name='create')
]
