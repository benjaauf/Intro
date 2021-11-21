from django.db import models

# Create your models here.

class Ocupado(models.Model):
    DISP = [
        ('L','Libre'),
        ('O', 'Ocupado')
    ]
    day = models.CharField(max_length=15)
    b12 = models.CharField(max_length=6, choices=DISP)
    b34 = models.CharField(max_length=6, choices=DISP)
    b56 = models.CharField(max_length=6, choices=DISP)
    b78 = models.CharField(max_length=6, choices=DISP)
    b910 = models.BooleanField(max_length=6, choices=DISP)
    b1112= models.CharField(max_length=6, choices=DISP)
    b1314 = models.CharField(max_length=6, choices=DISP)
    b1516 = models.CharField(max_length=6, choices=DISP)
    b1718 = models.CharField(max_length=6, choices=DISP)
    b1920 = models.CharField(max_length=6, choices=DISP)