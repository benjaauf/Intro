from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ramo(models.Model):
    DIFF=[
      (5, 'Pf, facilísimo'),
      (4, 'Fácil'),
      (3, 'Medio'),
      (2, 'Difícil'),
      (1, 'Muy difícil')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='Ramos', null=True)
    ramo = models.CharField(max_length=40)
    dificultad = models.IntegerField(choices=DIFF,null=True)

    def __str__(self):
        return f'{self.ramo}'

class Horario(models.Model):
    DISP=[
    ('Ocupado', 'Ocuapado'),
    ('Libre','Libre'),
    ('Estudiar','Estudiar')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='horario', null=True)
    day = models.CharField(max_length=20)
    b1 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '8:15-9:25')
    b2 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '9:35-10:45')
    b3 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '10:55-12:05')
    b4 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '12:15-13:25')
    b5 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '14:30-15:40')
    b6 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '15:50-17:00')
    b7 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '17:10-18:20')
    b8 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '18:30-19:40')
    b9 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '19:50-21:00')
    b10 = models.CharField(max_length=20, choices=DISP, default='Libre',verbose_name = '21:10-22:20')

    def __str__(self):
        return f'Usuario: {self.user} Dia: {self.day}'

class Descanso(models.Model):
    hora = models.DurationField()

    def __str__(self):
        return self.day



