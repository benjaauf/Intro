from django.shortcuts import render
from .forms import Ingresar_ramo
ramos=[]

def test(request):
    if request.method == 'POST':
        form = Ingresar_ramo(request.POST)
        if form.is_valid():
            ramo = form.cleaned_data["ramo"]
            ramos.append(ramo)
        else:
            form = Ingresar_ramo()
        context = {'form':form}
        return render(request,"Test/ramo.html",context)
