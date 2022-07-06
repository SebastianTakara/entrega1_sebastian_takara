from cgitb import html
import email
from math import remainder
from urllib import request
from django.shortcuts import render, HttpResponse
from app.models import Usuario, producto, empleado
from app.forms import empleadoFormulario, Usuarioformulario
from django.http import HttpResponse
from django.http.request import QueryDict

def Usuario(recuest):
    
    return render(recuest, 'app/Usuario.html')

def producto(recuest):

    return render(recuest, 'app/producto.html')

def empleado(recuest):

    return render(recuest, 'app/empleado.html')

def Usuarios(request):

    if request.method == 'POST':

        miformulario = Usuarioformulario(request.POST)

        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data
            print(informacion)
            usuario = Usuario ( nombre=informacion['nombre'],apellido=informacion["apellido"],email=informacion["email"],nacimiento=informacion["nacimiento"])

            usuario.save()

            return render(request, 'app/Usuario.html')
    
    else:

        miformulario= Usuarioformulario()


    return render(request, 'app/UsuarioFormulario.html',{'miformulario':miformulario})

def empleados(request):
    
    if request.method == 'POST':

        miformulario = empleadoFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            
            informacion = miformulario.cleaned_data
            print(informacion)
            Empleado = empleado(Usuario=informacion["Usuario"],num_empleado=informacion["num_empleado"],puesto=informacion["puesto"])

            Empleado.save()

            return render(request, 'app/empleado.html')
    else:
            miformulario= empleadoFormulario()

    return render(request, 'app/empleadoFormulario.html',{'miformulario':miformulario})

def buscar(request):

    if request.get['puesto']:

        puesto = request.GET['puesto']
        print(puesto)
        Empleados = empleado.objects.filter(puesto__icontains=puesto)
        print(Empleados)
        return render(request, "app/empleado.html", {"Empleados":Empleados, "puesto":puesto})

    else: 
         respuesta = "No enviaste datos"
    return render(request,"app/empleado.html", {"respuesta":respuesta})
# Create your views here.
