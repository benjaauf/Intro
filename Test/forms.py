from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT

class Ingresar_ramo(forms.Form):
    ramo = forms.CharField(max_length=40,MAX_NUM_FORM_COUNT=12)