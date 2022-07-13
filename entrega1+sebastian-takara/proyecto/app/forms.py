from django import forms

class Usuarioformulario(forms.Form):
    
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.EmailField()
    nacimiento = forms.DateField()

class Empleadoformulario(forms.Form):

    Usuario=forms.CharField (max_length=20)
    num_empleado=forms.IntegerField()
    puesto=forms.CharField(max_length=20)

class Productoformulario(forms.Form):

    producto=forms.CharField(max_length=40)
    precio=forms.FloatField()
    vencimiento=forms.DateField()