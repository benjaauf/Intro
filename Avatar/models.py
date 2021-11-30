from django.db import models

# Create your models here.


class accesorios(models.Model):
    name = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to="accesorios")

    def __str__(self):
        return self.name


class caras(models.Model):
    name = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="caras")

    def __str__(self):
        return self.name


class vestuario(models.Model):
    name = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="vestuario")

    def __str__(self):
        return self.name

class polis(models.Model):
    name = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="polis")

    def __str__(self):
        return self.name
