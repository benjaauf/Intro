from django import forms
from .models import Ramo, Horario
from django.forms import fields
from .models import Horario

class Ingresar_ramo(forms.Form):
    ramo = forms.CharField(max_length=40)



class LunesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']

class MartesForm(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['ramo']
        
class HorarioForm(forms.ModelForm):
        model = Horario
        exclude = ['day']
class MiercolesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
class JuevesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
class ViernesForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
class SabadoForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']
class DomingoForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['day']