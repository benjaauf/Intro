from django.db import models


class Ramo(models.Model):
    ramo = models.CharField(max_length=40)

    def __str__(self):
        return self.ramo

DISP=[
    ('ocupado', 'Ocuapado'),
    ('libre','Libre'),
]
# Create your models here.

class Horario(models.Model):
    day = models.CharField(max_length=20)
    b1 = models.CharField(max_length=20, choices=DISP, default='libre')
    b2 = models.CharField(max_length=20, choices=DISP, default='libre')
    b3 = models.CharField(max_length=20, choices=DISP, default='libre')
    b4 = models.CharField(max_length=20, choices=DISP, default='libre')
    b5 = models.CharField(max_length=20, choices=DISP, default='libre')
    b6 = models.CharField(max_length=20, choices=DISP, default='libre')
    b7 = models.CharField(max_length=20, choices=DISP, default='libre')
    b8 = models.CharField(max_length=20, choices=DISP, default='libre')
    b9 = models.CharField(max_length=20, choices=DISP, default='libre')
    b10 = models.CharField(max_length=20, choices=DISP, default='libre')

    def __str__(self):
        return self.day

class Descanso(models.Model):
    hora = models.DurationField()

    def __str__(self):
        return self.day



