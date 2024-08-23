from django.db import models

# Create your models here.

class Persona(models.Model):
    ESTADO_CHOICES = [('activo', 'Activo'),('inactivo', 'Inactivo')]
    name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES, default='activo')
    dateCreate = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
