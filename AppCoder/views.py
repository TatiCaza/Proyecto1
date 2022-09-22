from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'Inicio.html')

def Cursos(request):
    return render(request, 'Cursos.html')

def Profesores(request):
    return render(request, 'Profesores.html')

def Estudiantes(request):
    return render(request, 'Estudiantes.html')

def Entregables(request):
    return render(request, 'Entregables.html')