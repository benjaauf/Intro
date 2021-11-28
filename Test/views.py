from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from .forms import *
from .models import *


def delete(request,ramo_id):
    Ramo.objects.get(id=ramo_id).delete()
    return redirect('test')

# def test(request):
#     materias = Ramo.objects.all().order_by('id')
#     if request.method == 'POST':
#         form = Ingresar_ramo(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('test')
#     else:
#         form = Ingresar_ramo()
#     context = {'form':form, 'ramos': materias}
#     return render(request,"Test/ramo.html",context)
    
def descanso(request):
    if request.method == 'POST':
        form = DescansoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DescansoForm()
    return render(request,"Test/descanso.html")


def test(request):
    user = request.user
    ramos = Ramo.objects.all().filter(user=user).order_by('id')
    if request.method == 'POST':
        form = Ingresar_ramo(request.POST,instance=Ramo(user=user))
        lunes = LunesForm(request.POST, instance= Horario(day = 'Lunes',user=user),auto_id='l%s')
        martes = MartesForm(request.POST,instance= Horario(day = 'Martes',user=user),auto_id='ma%s')
        miercoles = MiercolesForm(request.POST,instance= Horario(day = 'Miercoles',user=user), auto_id='mi%s')
        jueves = JuevesForm(request.POST,instance= Horario(day = 'Jueves',user=user), auto_id='j%s')
        viernes = ViernesForm(request.POST,instance= Horario(day = 'Viernes',user=user),auto_id='v%s')
        sabado = SabadoForm(request.POST,instance= Horario(day = 'Sabado',user=user), auto_id='s%s')
        domingo = DomingoForm(request.POST,instance= Horario(day = 'Domingo',user=user), auto_id='d%s')
        if form.is_valid():
            form.save()
            return redirect('test')
        if lunes.is_valid() and martes.is_valid() and miercoles.is_valid() and jueves.is_valid() and viernes.is_valid() and sabado.is_valid() and domingo.is_valid():
            lunes.save()
            martes.save() 
            miercoles.save() 
            jueves.save() 
            viernes.save() 
            sabado.save() 
            domingo.save() 
            return redirect('home')
        # elif lunes.user == user:
        #     lunes.update(request.POST)
    else:
        form = Ingresar_ramo()
        lunes = LunesForm(auto_id='l%s')
        martes = MartesForm(auto_id='ma%s')
        miercoles = MiercolesForm( auto_id='mi%s')
        jueves = JuevesForm(auto_id='j%s')
        viernes = ViernesForm(auto_id='v%s')
        sabado = SabadoForm(auto_id='s%s')
        domingo = DomingoForm(auto_id='d%s')
    context = {'form':form, 'ramos': ramos,'Lunes':lunes,'Martes':martes,'Miercoles':miercoles,'Jueves':jueves,'Viernes':viernes,'Sabado': sabado,'Domingo':domingo,'user':user}
    return render(request,"Test/test.html",context)