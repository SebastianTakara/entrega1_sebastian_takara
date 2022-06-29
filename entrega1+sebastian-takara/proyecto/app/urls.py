from django.urls import path

from app import views

urlpatterns = [
    path('', views.Usuario, name="Usuario"),
    path('producto', views.producto, name="producto" ),
    path('empleado', views.empleado, name="empleado"),
   
]