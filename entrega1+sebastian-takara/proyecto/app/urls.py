from django.urls import path

from app import views

urlpatterns = [
    path('', views.usuario, name="Usuario"),
    path('producto', views.producto, name="producto" ),
    path('empleado', views.empleado, name="empleado"),
    path('Usuarioformulario', views.usuarios, name='Usuarioformulario'),
    path('Empleadoformulario', views.empleados, name='Empleadoformulario'),
    path('buscar/', views.buscar),

    ]