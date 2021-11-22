from django import forms
from .models import Ramo, Horario

class Ingresar_ramo(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['name']
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']