from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estudiante
from AppCoder.forms import form_estudiantes
# Create your views here.

def inicio(request):
    return render(request, 'Inicio.html')

def home(request):
    return render(request, 'home.html')

def Cursos(request):
    return render(request, 'Cursos.html')

def Profesores(request):
    return render(request, 'Profesores.html')

def Estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()
        return render(request, 'home.html')
    return render(request, 'Estudiantes.html')

def Entregables(request):
    return render(request, 'Entregables.html')

def api_estudiantes(request):
    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid:
            information = formulario.cleaned_data
            estudiante = Estudiante(nombre=information['nombre'],apellido=information['apellido'], email=information['email'])
            estudiante.save()
            return render(request, 'api_estudiantes.html')
    else:
        formulario = form_estudiantes()
    return render(request, 'api_estudiantes.html', {'formulario': formulario})

def buscar_estudiantes (request):
    if request.GET['email']:
        email = request.GET['email']
        estudiantes = Estudiante.objects.filter(email__icontains = email)
        return render(request, 'Estudiantes.html', {'estudiantes': estudiantes})
    else:
        respuesta = 'No enviaste datos'
    return HttpResponse(respuesta)