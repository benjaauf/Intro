from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import  messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
   return render(request, 'perfiles/home.html')

def logout(request):
   return redirect('inicio')

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         # username = form.cleaned_data['username']
         # messages.success(request, f'Usuario {username} creado')
         return redirect('inicio')
   else:
      form = UserRegisterForm()
   context = {'form':form}
   return render(request, 'perfiles/register.html', context)

def inicio(request):
   return render(request, 'perfiles/inicio.html')