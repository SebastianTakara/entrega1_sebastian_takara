from django import forms

class empleadoFormulario(forms.Form):

    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.EmailField()
    nacimiento = forms.DateField()

class Usuarioformulario(forms.Form):

    Usuario=forms.CharField (max_length=20)
    num_empleado=forms.IntegerField()
    puesto=forms.CharField(max_length=20)