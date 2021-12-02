from django.shortcuts import render
from .models import *

def avatar(request):
    accesorios = Accesorios.objects.get(id=1).imagen
    caras = Caras.objects.get(id=1).imagen
    vestuario = Vestuario.objects.get(id=1).imagen
    context = {'accesorios':accesorios, 'caras':caras, 'vestuario':vestuario}
    return render(request,'Avatar/avatar.html',context)