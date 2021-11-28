from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate,login
from .forms import UserRegisterForm
from Test.models import *
# Create your views here.

def home(request):
   user = request.user
   ramos = Ramo.objects.all().filter(user=user).order_by('id')
   horario = Horario.objects.all().filter(user=user)
   context = {'user':user,'ramos':ramos,'horario':horario}
   return render(request, 'perfiles/home.html',context)

def logout(request):
   return redirect('inicio')

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         username = request.POST['username']
         password = request.POST['password1']
         user = authenticate(request,username=username, password =password)
         login(request,user)
         return redirect('test')
   else:
      form = UserRegisterForm()
   context = {'form':form}
   return render(request, 'perfiles/register.html', context)

def inicio(request):
   return render(request, 'perfiles/inicio.html')