from django.shortcuts import redirect, render
from .models import *

conacc = [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
concar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17]
conver = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14]

def deracc(request):
    accesorio = contador.objects.get(name='acceso')
    accesorio.valor = accesorio.valor +1
    accesorio.save()
    if accesorio.valor >= 17:
        accesorio.valor = 0
        accesorio.save()
    return redirect('avatar')
    
def dercar(request):
    cara = contador.objects.get(name='careta')
    cara.valor = cara.valor +1
    cara.save()
    if cara.valor >= 17:
        cara.valor = 0
        cara.save()
    return redirect('avatar')

def derves(request):
    ropa = contador.objects.get(name='vesto')
    ropa.valor = ropa.valor +1
    ropa.save()
    if ropa.valor >= 14:
        ropa.valor = 0
        ropa.save()
    return redirect('avatar')

def izqacc(request):
    accesorio = contador.objects.get(name='acceso')
    accesorio.valor = accesorio.valor -1
    accesorio.save()
    if accesorio.valor <= -1:
        accesorio.valor = 16
        accesorio.save()
    return redirect('avatar')

def izqcar(request):
    cara = contador.objects.get(name='careta')
    cara.valor = cara.valor -1
    cara.save()
    if cara.valor <= -1:
        cara.valor = 16
        cara.save()
    return redirect('avatar')

def izqves(request):
    ropa = contador.objects.get(name='vesto')
    ropa.valor = ropa.valor -1
    ropa.save()
    if ropa.valor <= -1:
        ropa.valor = 13
        ropa.save()
    return redirect('avatar')

def avatar(request):
    ac = conacc[contador.objects.get(name='acceso').valor]
    ca = concar[contador.objects.get(name='careta').valor]
    ve = conver[contador.objects.get(name='vesto').valor]

    accesorios = Accesorios.objects.get(id=ac)
    caras = Caras.objects.get(id=ca)
    vestuario = Vestuario.objects.get(id=ve)
    context = {'accesorios':accesorios, 'caras':caras, 'vestuario':vestuario}
    return render(request,'Avatar/avatar.html',context)



