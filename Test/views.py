from django.shortcuts import redirect, render
from .forms import Ingresar_ramo
from .models import Ramo
from .forms import *
from .models import *
ramos=[]

def editar(request):
    context={'ramos':ramos}
    return render(request,"Test/lista.html",context)

def test(request):
    if request.method == 'POST':
        form = Ingresar_ramo(request.POST)
        if form.is_valid():
            ramo = form.save()
            ramos.append(ramo)
            return redirect('test')
    else:
        form = Ingresar_ramo()
    context = {'form':form, 'ramos': ramos}
    return render(request,"Test/ramo.html",context)

def horario(request):
    if request.method == 'POST':
        dia = Horario(day='Lunes')
        form = HorarioForm(request.POST, instance=dia)
        if form.is_valid():
            form.save() 
            return redirect('horario')
    else:
        form = HorarioForm()
    context = {'form':form}
    return render(request, 'Test/hora.html',context)

