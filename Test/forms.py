from django import forms
from .models import Ramo, Horario

class Ingresar_ramo(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['ramo']
        
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']