'''
from django import forms

class Ingresar_ramo(forms.Form):
    ramo = forms.CharField(max_length=40)
'''
from django import forms
from .models import Ramo

class Ingresar_ramo(forms.ModelForm):

    class Meta:
        model = Ramo
        fields = ['name']