from django import forms

class Ingresar_ramo(forms.Form):
    ramo = forms.CharField(max_length=40)

