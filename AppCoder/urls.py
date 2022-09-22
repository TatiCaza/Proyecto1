from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', Cursos),
    path('profesores/', Profesores),
    path('estudiantes/', Estudiantes),
    path('entregables/', Entregables)
]
