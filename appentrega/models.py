from django.db import models

# Create your models here.
class pago(models.Model):
    metodoPago = models.CharField(max_length=30)
    cuotas = models.IntegerField()
    
class datosPersonales(models.Model):
    nombres = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=40, null=True)

class prenda(models.Model):
    nombre = models.CharField(max_length=40)
    sexo = models.CharField(max_length=1)
    talle = models.CharField(max_length=4)
    color = models.CharField(max_length=40)