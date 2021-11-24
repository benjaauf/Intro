from django import forms


class Test2(forms.Form):
  P1 = forms.ChoiceField(\
    label = 'asignatura',\
    label_suffix = ':',\
    choices=[
    ('nada', 'Pf, facilísimo'),\
    ('F', 'Fácil'),\
    ('Me', 'Medio'),\
    ('D', 'Difícil'),\
    ('Muy', 'Muy difícil')

    ]
  )

  P2 = forms.ChoiceField(\
    label='2. ¿Cada cuánto te gustaría repetir este test?',\
    choices=[
    ('elec', 'Repetir de forma manual'),\
    ('dsp', 'Después de cada certamen'),\
    ('s', 'Cada una semana'),\
    ('m', 'Cada un mes')

    ]
  )
