from django.db.models import fields
from django.db.models.enums import Choices
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

# def estudio(request):
# 	semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
# 	user = request.user
# 	lun = Horario.objects.get(user = user, day = semana[0])
# 	bloques = [lun.b1, lun.b2, lun.b3, lun.b4, lun.b5, lun.b6, lun.b7, lun.b8, lun.b9, lun.b10]
# 	prueba={}
# 	for i in range(len(bloques)):
# 		if bloques[i] == 'Libre':
# 			prueba[i+1]=bloques[i]
# 	if request.method == 'POST':
# 		form = EstudioForm(request.POST,)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('home')
# 	else:
# 		form = EstudioForm()
# 	context = {'form':form,'prueba':prueba}
# 	return render(request,'Test2/prueba.html',context)