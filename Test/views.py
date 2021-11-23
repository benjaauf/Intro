from django.shortcuts import redirect, render
from .forms import *
from .models import *
ramos=[]

def lista(request):
    ramo = Ramo.objects.all().order_by('id')
    context = {'ramos':ramo}
    if request.method == 'POST':
        borrado = Ramo.objects.all()
        ramos.remove(borrado)
        borrado.delete()
    return render(request,"Test/lista.html",context)

def delete(request,ramo_id):
    Ramo.objects.get(id=ramo_id).delete()
    return redirect('lista')

def test(request):
    materias = Ramo.objects.all().order_by('id')
    if request.method == 'POST':
        form = Ingresar_ramo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')
    else:
        form = Ingresar_ramo()
    context = {'form':form, 'ramos': materias}
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

