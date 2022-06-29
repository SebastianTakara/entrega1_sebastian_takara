from cgitb import html
import email
from math import remainder
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import Usuario, producto, empleado


def Usuario(recuest):
    
    return render(recuest, 'app/Usuario.html')

def producto(recuest):

    return render(recuest, 'app/producto.html')

def empleado(recuest):

    return render(recuest, 'app/empleado.html')


# Create your views here.
