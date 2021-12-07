from django.shortcuts import redirect, render
from django.contrib.auth import  authenticate,login
from .forms import UserRegisterForm, CertamenForm
from Test.models import *
from .calendario import crear_calendario, crear_estudio, crear_certamen
from .models import *
from Avatar.models import Accesorios,Caras,Vestuario,contador
conacc = [35,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36]
concar = [18, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,19]
conver = [18, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,19]

# Create your views here.

def home(request):
   nivel=Nivel.objects.get(name='nivelon')
   exp = Exp.objects.get(name='experience')
   supera = Exp.objects.get(name='supera')
   while exp.valor >= supera.valor:
      nivel.numero = nivel.numero + 1
      nivel.save()
      exp.valor = exp.valor - supera.valor
      exp.save()
      supera.valor = supera.valor + 15
      supera.save()
   ac = conacc[contador.objects.get(name='acceso').valor]
   ca = concar[contador.objects.get(name='careta').valor]
   ve = conver[contador.objects.get(name='vesto').valor]
   accesorios = Accesorios.objects.get(id=ac)
   caras = Caras.objects.get(id=ca)
   vestuario = Vestuario.objects.get(id=ve)
   user = request.user
   ramos = Ramo.objects.all().filter(user=user).order_by('id')
   horario = Horario.objects.all().filter(user=user)
   context = {'user':user,'ramos':ramos,'horario':horario,'accesorios':accesorios, 'caras':caras, 'vestuario':vestuario,'nivel':nivel,'exp':exp,'supera':supera}
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


         ##############################################################

         accesorio = contador.objects.get(name='acceso')
         accesorio.valor = 0
         accesorio.save()

         cara = contador.objects.get(name='careta')
         cara.valor = 0
         cara.save()

         ropa = contador.objects.get(name='vesto')
         ropa.valor = 0
         ropa.save()

         nivel = Nivel.objects.get(name='nivelon')
         nivel.numero = 1
         nivel.save()

         exp = Exp.objects.get(name='experience')
         exp.valor = 0
         exp.save()

         supera = Exp.objects.get(name='supera')
         supera.valor = 15
         supera.save()

         ##############################################################

         return redirect('test')
   else:
      form = UserRegisterForm()
   context = {'form':form}
   return render(request, 'perfiles/register.html', context)

def inicio(request):
   # hacer que cuando se vaya inicio se deslogue automaticamente
   return render(request, 'perfiles/inicio.html')


def hora_estudio(request):
   user = request.user
   horarios = Horario.objects.filter(user = user)
   materias = Ramo.objects.filter(user=user).order_by('dificultad')
   eventos = crear_estudio(horarios,materias)
   return redirect('home')

def cumplido(request):
   exp = Exp.objects.get(name='experience')
   exp.valor = exp.valor + 10
   exp.save()
   return redirect('home')

def certamen(request):
   user = request.user
   choices = Ramo.objects.filter(user=user)
   if request.method == 'POST':
      form = CertamenForm(request.POST, instance=Certamen(user=user))
      if form.is_valid():
         form.save()
         return redirect('hora_certamen')
   else:
      form = CertamenForm(instance=Certamen(user=user))
   context = {'form':form}
   return render(request,'perfiles/certamen.html',context)

def hora_certamen(request):
   user = request.user
   certamenes = Certamen.objects.filter(user = user)
   eventos = crear_certamen(certamenes)
   return redirect('home')
