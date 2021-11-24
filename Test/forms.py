from django import forms
from django.forms.widgets import TextInput
from .models import Descanso, Ramo, Horario
from django.forms import fields
from .models import Horario

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
        exclude = ['day']
    prefix = 'Lunes'

class MartesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
    prefix = 'Martes'

class MiercolesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
    prefix = 'Miercoles'

class JuevesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
    prefix = 'Jueves'

class ViernesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
    prefix = 'Viernes'

class SabadoForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
    prefix = 'Sabado'

class DomingoForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
    prefix = 'Domingo'