from django import forms
from django.forms.widgets import TextInput
from .models import *



class Ingresar_ramo(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['ramo']


class DescansoForm(forms.ModelForm):
    class Meta:
        model = Descanso
        fields = ['hora']
        #widgets = {'hora' = TextInput(attrs={'class':'durationInputWidget'})}


class LunesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Lunes'

class MartesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Martes'

class MiercolesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Miercoles'

class JuevesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Jueves'

class ViernesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Viernes'

class SabadoForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Sabado'

class DomingoForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day','user']
    prefix = 'Domingo'