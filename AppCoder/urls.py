from django.urls import path, include
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('cursos/', Cursos),
    path('profesores/', Profesores),
    path('estudiantes/', Estudiantes),
    path('buscar_estudiantes/', buscar_estudiantes),
    path('buscar_cursos/', buscar_curso),
    path('entregables/', Entregables),
    path('create_estudiantes/', create_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('update_estudiantes/<estudiante_id>', update_estudiantes),
    path('delete_estudiantes/<estudiante_id>', delete_estudiantes),

    
    path('cursos/list', CursoList.as_view(), name = 'List'),
    path(r'^(?P<pk>\d+)$', CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', CursoCreacion.as_view(), name='New'),
    path(r'^edita/(?P<pk>\d+)$', CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', CursoDelete.as_view(), name='Delete'),

    path('login/', login_request),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name = 'Logout'),
    path('registro/', registro),
    path('perfil/', perfilView),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changepass)
    

]
