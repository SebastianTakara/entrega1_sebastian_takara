from ast import Return
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import Usuario, Empleado
from app.forms import Empleadoformulario, Usuarioformulario



def usuario(recuest):
    
    return render(recuest, 'app/usuario.html')

def producto(recuest):

    return render(recuest, 'app/producto.html')

def empleado(recuest):

    return render(recuest, 'app/empleado.html')

def usuarios(request):

    if request.method == 'POST':
        
        miformulario =  Usuarioformulario(request.POST)

        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data
            print(informacion)

            usuario = Usuario (nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'], nacimiento=informacion['nacimiento'])
            
            usuario.save()

            return render(request, 'app/usuario.html')
    
    else:
        
        miformulario= Usuarioformulario()
        return render(request, 'app/usuarios.html',{'miformulario':miformulario})





def empleados(request):
    
    if request.method == 'POST':

        miformulario = Empleadoformulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            
            informacion = miformulario.cleaned_data
            print(informacion)
            empleado = Empleado(Usuario=informacion["Usuario"],num_empleado=informacion["num_empleado"],puesto=informacion["puesto"])

            empleado.save()

            return render(request, 'app/empleado.html')
    else:
            miformulario= Empleadoformulario()

    return render(request, 'app/empleados.html',{'miformulario':miformulario})

def buscar(request):

    if  request.GET["puesto"]: 

	    
        puesto = request.GET['puesto'] 
        print(puesto)
        empleados = Empleado.objects.filter(puesto__icontains=puesto)
        print(empleados)
        return render(request, "app/buscar.html", {"empleados":empleados, "puesto":puesto})

    else: 
        respuesta = "No enviaste datos"
        return render(request,"app/buscar.html", {"respuesta":respuesta})



