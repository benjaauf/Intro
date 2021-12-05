from django import forms
from django.db.models import fields
from Test.models import *


class Test2(forms.ModelForm):
  
  # P2 = forms.ChoiceField(
  #   label='2. ¿Cada cuánto te gustaría repetir este test?',
  #   choices=[
  #     ('elec', 'Repetir de forma manual'),
  #     ('dsp', 'Después de cada certamen'),
  #     ('s', 'Cada una semana'),
  #     ('m', 'Cada un mes')
  #   ]
  # )
  class Meta:
    model = Ramo
    fields = ['dificultad']

  
# class EstudioForm(forms.ModelForm):
#   DISP = [
#     ('Libre','Libre'),
#     ('Estudiar','Estudiar')
#   ]

#   class Meta:
#     model = Horario
#     exclude = ['day', 'user']