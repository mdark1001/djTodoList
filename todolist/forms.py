"""
@author mdark1001 | Miguel Cabrera R. <miguel.cabrera.app@gmail.com>
@date 30/10/20
@project 
@name forms
"""
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'descrripcion', 'user', 'tag', 'state')
