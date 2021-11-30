from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from .forms import *
from .models import *


def delete(request,ramo_id):
    Ramo.objects.get(id=ramo_id).delete()
    return redirect('test')
    
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
        lunes = LunesForm(request.POST, instance= Horario(day = 'Lunes',user=user))
        martes = MartesForm(request.POST,instance= Horario(day = 'Martes',user=user))
        miercoles = MiercolesForm(request.POST,instance= Horario(day = 'Miercoles',user=user))
        jueves = JuevesForm(request.POST,instance= Horario(day = 'Jueves',user=user))
        viernes = ViernesForm(request.POST,instance= Horario(day = 'Viernes',user=user))
        sabado = SabadoForm(request.POST,instance= Horario(day = 'Sabado',user=user))
        domingo = DomingoForm(request.POST,instance= Horario(day = 'Domingo',user=user))
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
            return redirect('/test2')
    else:
        form = Ingresar_ramo()
        lunes = LunesForm()
        martes = MartesForm()
        miercoles = MiercolesForm( )
        jueves = JuevesForm()
        viernes = ViernesForm()
        sabado = SabadoForm()
        domingo = DomingoForm()
    context = {'form':form, 'ramos': ramos,'Lunes':lunes,'Martes':martes,'Miercoles':miercoles,'Jueves':jueves,'Viernes':viernes,'Sabado': sabado,'Domingo':domingo,'user':user}
    return render(request,"Test/test.html",context)

# Cambio del test 1 

def updatet1(request):
    user = request.user
    ramos = Ramo.objects.all().filter(user=user).order_by('id')
    lun = Horario.objects.get(user=user,day='Lunes')
    mar = Horario.objects.get(user=user,day='Martes')
    mie = Horario.objects.get(user=user,day='Miercoles')
    jue = Horario.objects.get(user=user,day='Jueves')
    vie = Horario.objects.get(user=user,day='Viernes')
    sab = Horario.objects.get(user=user,day='Sabado')
    dom = Horario.objects.get(user=user,day='Domingo')
    if request.method == 'POST':
        form = Ingresar_ramo(request.POST,instance=Ramo(user=user))
        lunes = LunesForm(request.POST, instance= lun)
        martes = MartesForm(request.POST,instance=  mar)
        miercoles = MiercolesForm(request.POST,instance= mie)  
        jueves = JuevesForm(request.POST,instance= jue)
        viernes = ViernesForm(request.POST,instance= vie) 
        sabado = SabadoForm(request.POST,instance= sab)
        domingo = DomingoForm(request.POST,instance= dom)
        if form.is_valid():
            form.save()
            return redirect('updatet1')
        if lunes.is_valid() and martes.is_valid() and miercoles.is_valid() and jueves.is_valid() and viernes.is_valid() and sabado.is_valid() and domingo.is_valid():
            lunes.save()
            martes.save() 
            miercoles.save() 
            jueves.save() 
            viernes.save() 
            sabado.save() 
            domingo.save() 
            return redirect('home')
    else:
        form = Ingresar_ramo()
        lunes = LunesForm(instance=lun)
        martes = MartesForm(instance=mar)
        miercoles = MiercolesForm( instance=mie)
        jueves = JuevesForm(instance=jue)
        viernes = ViernesForm(instance=vie)
        sabado = SabadoForm(instance=sab)
        domingo = DomingoForm(instance=dom)
    context = {'form':form, 'ramos': ramos,'Lunes':lunes,'Martes':martes,'Miercoles':miercoles,'Jueves':jueves,'Viernes':viernes,'Sabado': sabado,'Domingo':domingo,'user':user}
    return render(request,"Test/updatet1.html",context)

def deletet1(request,ramo_id):
    Ramo.objects.get(id=ramo_id).delete()
    return redirect('updatet1')