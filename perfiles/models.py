from django.db import models
from django.contrib.auth.models import User

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