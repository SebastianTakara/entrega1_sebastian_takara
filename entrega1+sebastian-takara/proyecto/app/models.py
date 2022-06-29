from django.db import models

class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    nacimiento = models.DateField()

class producto(models.Model):

    producto=models.CharField(max_length=40)
    precio=models.FloatField()
    vencimiento=models.DateField()

class empleado(models.Model):

    Usuario=models.CharField (max_length=20) #or models.EmailField() es posibles usar esto para que pueda entrar de las 2 maneras ?
    num_empleado=models.IntegerField()
    puesto=models.CharField(max_length=20)

# Create your models here.
