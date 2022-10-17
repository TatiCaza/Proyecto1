from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    def __self__(self):
        return f"Nombre: {self.nombre} - Comision: {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregada = models.BooleanField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank=True)

