from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.lista_estudiantes, name='estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('profesores/', views.profesores, name='profesores'),
    path('profesor/editar/<int:id>/', views.profesor_editar, name='profesorEditar'),       # NUEVA
    path('profesor/eliminar/<int:id>/', views.profesor_eliminar, name='profesorEliminar'), # NUEVA
    path('cursos/', views.cursos, name='cursos'),
    path('entregables/', views.entregables, name='entregables'),
]