from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('cursos/', Cursos),
    path('profesores/', Profesores),
    path('estudiantes/', Estudiantes),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiantes/', buscar_estudiantes),
    path('entregables/', Entregables)
]
