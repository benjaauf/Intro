from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate,login
from .forms import UserRegisterForm
from Test.models import *
from .calendario import crear_calendario

from Avatar.models import Accesorios,Caras,Vestuario,contador

conacc = [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
concar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
conver = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Create your views here.

def home(request):
   ac = conacc[contador.objects.get(name='acceso').valor]
   ca = concar[contador.objects.get(name='careta').valor]
   ve = conver[contador.objects.get(name='vesto').valor]
   accesorios = Accesorios.objects.get(id=ac)
   caras = Caras.objects.get(id=ca)
   vestuario = Vestuario.objects.get(id=ve)
   user = request.user
   ramos = Ramo.objects.all().filter(user=user).order_by('id')
   horario = Horario.objects.all().filter(user=user)
   context = {'user':user,'ramos':ramos,'horario':horario,'accesorios':accesorios, 'caras':caras, 'vestuario':vestuario}
   return render(request, 'perfiles/home.html',context)

def logout(request):
   return render(request,'logout.html',context={'user':request.user})

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         username = request.POST['username']
         password = request.POST['password1']
         user = authenticate(request,username=username, password =password)
         login(request,user)
         calendario = crear_calendario()
         return redirect('test')
   else:
      form = UserRegisterForm()
   context = {'form':form}
   return render(request, 'perfiles/register.html', context)

def inicio(request):
   return render(request, 'perfiles/inicio.html')