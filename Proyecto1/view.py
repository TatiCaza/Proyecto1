from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def inicio (request):
    return HttpResponse ('Hola página de inicio')

def homePage (self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre': 'Tatiana', 'apellido':'Cazazola', 'lista': lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse (documento)

def curso (self):
    #planilla = loader.get_template('cursos.html')
    curso = Curso(nombre="UX/UI", camada="12345")
    curso.save()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse (documento)