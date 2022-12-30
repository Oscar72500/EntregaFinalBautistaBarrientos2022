from django.db import models

# Create your models here.

class Terror(models.Model):
    mas_vistas = models.CharField(max_length=40)
    taquilla = models.IntegerField()
    critica_peliculas = models.CharField(max_length=40)

class Accion(models.Model):
    mas_vistas = models.CharField(max_length=40)
    taquilla = models.IntegerField()
    critica_peliculas = models.CharField(max_length=40)

class Aventura(models.Model):
    mas_vistas = models.CharField(max_length=40)
    taquilla = models.IntegerField()
    critica_peliculas = models.CharField(max_length=40)
    




