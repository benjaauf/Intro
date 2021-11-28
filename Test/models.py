from django.db import models
from django.contrib.auth.models import User


class Ramo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='Ramos', null=True)
    ramo = models.CharField(max_length=40)

    def __str__(self):
        return f'Usuario: {self.user}   Ramo: {self.ramo}'

DISP=[
    ('Ocupado', 'Ocuapado'),
    ('Libre','Libre'),
]
# Create your models here.

class Horario(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='horario', null=True)
    day = models.CharField(max_length=20)
    b1 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b2 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b3 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b4 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b5 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b6 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b7 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b8 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b9 = models.CharField(max_length=20, choices=DISP, default='Libre')
    b10 = models.CharField(max_length=20, choices=DISP, default='Libre')

    def __str__(self):
        return f'Usuario: {self.user} Dia: {self.day}'

class Descanso(models.Model):
    hora = models.DurationField()

    def __str__(self):
        return self.day



