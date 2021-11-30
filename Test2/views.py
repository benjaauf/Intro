from django.shortcuts import redirect, render

from Test.forms import Ingresar_ramo
from .forms import Test2
from Test.models import *


def test2(request):
	user = request.user
	ramos = Ramo.objects.filter(user=user) 
	materias = []
	temp=[]
	context = {'user':user}
	for ramo in ramos:
		materias.append(ramo)
	for materia in materias:
		temp.append(materia.ramo)
	materias = temp
	temp=[]
	forms = []
	if request.method == 'POST':
		for materia in materias:
			ins = Ramo.objects.get(user= user, ramo= materia)
			form = Test2(request.POST,instance=ins,prefix=materia)
			if form.is_valid():
				form.save()
				forms.append(form)
		return redirect('home')	
	else:
		for materia in materias:
			ins = Ramo.objects.get(user= user, ramo= materia)
			form= Test2(instance=ins,prefix=materia)
			forms.append(form)
	context= {'user':user, 'materias':materias,'ramos':ramos,'forms':forms}
	return render(request,'Test2/test2.html', context)
