from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Certamen


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        help_texts = {k:"" for k in fields}


class CertamenForm(forms.ModelForm):
    
    class Meta:
        model = Certamen
        fields = ['ramo','fecha','hora']

    # def __init__(self, *args, **kwargs):
    #     super(CertamenForm,self).__init__(*args,**kwargs)
    #     if self.instance.ramo and self.instance.ramo.id:
    #         user = self.instance.ramo.user.all()
    #         self.fields['user'].queryset = user
            