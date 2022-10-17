import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return render(request, 'Inicio.html')

@login_required
def home(request):
    return render(request, 'home.html')

def Cursos(request):
    if request.method == "POST":
        cursos = Curso(nombre = request.POST['nombre'], comision = request.POST['comision'])
        cursos.save()   
        return render(request, 'home.html')
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

def buscar_curso (request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains = comision)
        return render(request, 'Cursos.html', {'curso': cursos})
    else:
        respuesta = 'No enviaste datos'
    return HttpResponse(respuesta)

def create_estudiantes (request):
    if request.method == 'POST':
        estudiantes = Estudiante(nombre= request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiantes.save()
        estudiantes = Estudiante.objects.all() #trae todo
        return render (request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
    return render(request, "estudiantesCRUD/create_estudiantes.html")

def read_estudiantes (request = None):
    estudiantes = Estudiante.objects.all() #trae todo
    return render (request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})

def update_estudiantes (request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)

    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save()
            read_estudiantes()
            estudiantes = Estudiante.objects.all() #trae todo
            return render (request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
    else: 
        formulario = form_estudiantes(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
    return render(request, "estudiantesCRUD/update_estudiantes.html", {"formulario": formulario})

    return False

def delete_estudiantes (request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)
    estudiante.delete()
    estudiantes = Estudiante.objects.all() #trae todo
    return render (request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})

# forma 2 para cursos
class CursoList (ListView):
    model = Curso
    template_name = "/AppCoder/cursos_list.html"

class CursoDetalle (DetailView):
    model = Curso
    template_name = "/AppCoder/cursos_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url=  "/AppCoder/cursos/list"
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/cursos/list"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    success_url= "/AppCoder/cursos/list"

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password= pwd)

            if user is not None: 
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {'form':form})
        else: 
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def registro (request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        #form = UserRegisterFrom(request.POST)
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect(request, "/AppCoder/login")
        else:
            return render(request, "registro.html", {'form': form})

    form = UserRegisterFrom()
    return render(request, "registro.html", {'form': form})

@login_required
def editarPerfil (request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)

    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)

        if form.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'home.html')
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = UserEditForm(initial = {'email':usuario.email, 'username':usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, 'editarPerfil.html', {'form':form, 'usuario':usuario})

@login_required
def changepass(request):
    usuario = request.user
    if request.method =='POST':
        #form = PasswordChangeForm(data = request.POST, user = request.user)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'home.html')
    else:
       #form = PasswordChangeForm(request.user)
       form = ChangePasswordForm(request.user)
    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})
@login_required
def perfilView(request):
    return render(request, 'perfil.html')