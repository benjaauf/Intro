from django.db import models
from django.contrib.auth.models import User
from Test.models import Ramo
from datetime import date

# Create your models here.
class Nivel(models.Model):
    name= models.CharField(max_length=10)
    numero = models.IntegerField()

    def __str__(self):
        return self.name

class Exp(models.Model):
    name= models.CharField(max_length=10)
    valor = models.IntegerField()

    def __str__(self):
        return self.name

class Certamen(models.Model):
    HORAS = [
        ('b1','8:15-9:25'),
        ('b2','9:35-10:45'),
        ('b3','10:55-12:05'),
        ('b4','12:15-13:25'),
        ('b5','14:30-15:40'),
        ('b6','15:50-17:00'),
        ('b7','17:10-18:20'),
        ('b8','18:30-19:40'),
        ('b9','19:50-21:00'),
        ('b10','21:10-22:20')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, limit_choices_to={'user_id':'1'}) 
    """ usar limitchoices """
    fecha = models.DateField(default=date.today())
    hora = models.CharField(choices=HORAS, max_length=20, default='b1')
    
    def __str__(self):
        return f'Hora: {self.hora} Ramo: {self.ramo}'
