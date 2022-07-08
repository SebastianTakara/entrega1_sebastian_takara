from django.db import models

class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    nacimiento = models.DateField()

class Producto(models.Model):

    producto=models.CharField(max_length=40)
    precio=models.FloatField()
    vencimiento=models.DateField()

class Empleado(models.Model):

    Usuario=models.CharField (max_length=20)
    num_empleado=models.IntegerField()
    puesto=models.CharField(max_length=20)


