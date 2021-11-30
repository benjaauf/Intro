from django.shortcuts import render
from .models import *

def avatar(request):
    return render(request,'Avatar/avatar.html')