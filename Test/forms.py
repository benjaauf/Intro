'''
from django import forms
from django.forms import fields
from .models import Horario

class Ingresar_ramo(forms.Form):
    ramo = forms.CharField(max_length=40)
'''
from django import forms
from .models import Ramo

class Ingresar_ramo(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['name']
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']