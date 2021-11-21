from django.shortcuts import render
from django.http import HttpResponse

def Test2(request):
	return HttpResponse('Crea tu tier list de las materias más difíciles')
