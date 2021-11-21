from django.shortcuts import redirect, render
from .forms import Ingresar_ramo
ramos=[]

def test(request):
    if request.method == 'POST':
        form = Ingresar_ramo(request.POST)
        if form.is_valid():
            ramo = form.cleaned_data["ramo"]
            ramos.append(ramo)
            return redirect('test')
    else:
        form = Ingresar_ramo()
    context = {'form':form,'ramos':ramos}
    return render(request,"Test/ramo.html",context)
