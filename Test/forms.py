from django import forms
from .models import Ramo, Horario

class Ingresar_ramo(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['ramo']

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