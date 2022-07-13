from ast import Return
from urllib import request
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import Usuario, Empleado, Producto
from app.forms import Empleadoformulario, Usuarioformulario, Productoformulario



def usuario(request):
    
    return render(request, 'app/usuario.html')

def producto(request):

    return render(request, 'app/producto.html')

def empleado(request):

    return render(request, 'app/empleado.html')

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

def productos(request):
    if request.method == 'POST':

        miformulario = Productoformulario(request.POST)
        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data
            print(informacion)
            
            producto = Producto(producto=informacion['producto'],precio=informacion['precio'], vencimiento=informacion['vencimiento'])
            
            producto.save()

            return render(request, 'app/producto.html')
    else:
            miformulario = Productoformulario()

    return render (request, 'app/productos.html',{'miformulario':miformulario})
    


def buscar(request):

    if  request.GET["num_empleado"]: 

	    
            num_empleado = request.GET['num_empleado'] 
            print(num_empleado)
            empleados = Empleado.objects.filter(num_empleado__icontains=num_empleado)
            print(empleados)
            return render(request, "app/buscar_num_empleado.html", {"empleados":empleados, "num_empleado":num_empleado})

    else: 
        respuesta = "No enviaste datos"
    return render(request,"app/buscar_num_empleado.html", {"respuesta":respuesta})

def buscar_num_empleado(request):

    return render(request, 'app/buscar_num_empleado.html')

