from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render


@login_required
def home(request):
    context={}
    return render(request,'home.html',context)
