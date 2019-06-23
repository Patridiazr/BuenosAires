from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=30)
    comuna = models.CharField(max_length=100)

class Solicitud(models.Model):
    nombres = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    asunto = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)