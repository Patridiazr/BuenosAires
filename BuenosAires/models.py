from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.IntegerField
    nombre = models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=30)
    comuna = models.CharField(max_length=100)
    codpos = models.IntegerField