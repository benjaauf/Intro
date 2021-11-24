from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from .forms import *
from .models import *


def delete(request,ramo_id):
    Ramo.objects.get(id=ramo_id).delete()
    return redirect('test')

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
        lunes = LunesForm(request.POST, instance= Horario(day = 'Lunes'))
        martes = MartesForm(request.POST,instance= Horario(day = 'Martes'))
        miercoles = MiercolesForm(request.POST,instance= Horario(day = 'Miercoles'))
        jueves = JuevesForm(request.POST,instance= Horario(day = 'Jueves'))
        viernes = ViernesForm(request.POST,instance= Horario(day = 'Viernes'))
        sabado = SabadoForm(request.POST,instance= Horario(day = 'Sabado'))
        domingo = DomingoForm(request.POST,instance= Horario(day = 'Domingo'))
        if lunes.is_valid() and martes.is_valid() and miercoles.is_valid() and jueves.is_valid() and viernes.is_valid() and sabado.is_valid() and domingo.is_valid():
            lunes.save()
            martes.save() 
            miercoles.save() 
            jueves.save() 
            viernes.save() 
            sabado.save() 
            domingo.save() 
        return redirect('horario')
    else:
        lunes = LunesForm()
        martes = MartesForm()
        miercoles = MiercolesForm()
        jueves = JuevesForm()
        viernes = ViernesForm()
        sabado = SabadoForm()
        domingo = DomingoForm()
    context= {'Lunes':lunes,'Martes':martes,'Miercoles':miercoles,'Jueves':jueves,'Viernes':viernes,'Sabado': sabado,'Domingo':domingo}
    return render(request, 'Test/hora.html',context)

# def horario(request):
#     if request.method == 'POST':
#         dia = Horario(day='Lunes')
#         form = LunesForm(request.POST, instance=dia)
#         if form.is_valid():
#             form.save() 
#             return redirect('horario')
#     else:
#         form = LunesForm()
#     context = {'Lunes':form}
#     return render(request, 'Test/hora.html',context)
