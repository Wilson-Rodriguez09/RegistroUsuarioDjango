from django.urls import path
from .views import listarUsuarios, registrarUsuarios

urlpatterns = [
    path('',listarUsuarios, name="listarUsuarios"),
    path('registrar/',registrarUsuarios, name="registrarUsuarios")
]