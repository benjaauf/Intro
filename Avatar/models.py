from django.db import models

# Create your models here.


class Accesorios(models.Model):
    name = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to="accesorios")

    def __str__(self):
        return self.name


class Caras(models.Model):
    name = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="caras")

    def __str__(self):
        return self.name


class Vestuario(models.Model):
    name = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="vestuario")

    def __str__(self):
        return self.name
