from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import ProfesorForm

# Vista para el index
def index(request):
    context = {'mensaje': 'Bienvenidos a mi aplicación Django'}
    return render(request, 'myapp/index.html', context)

# Vistas para Estudiantes
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/estudiante_detail.html', {'estudiante': estudiante})

# VISTAS PARA PROFESORES (CON EL CRUD NUEVO)
def profesores(request):
    query = request.GET.get('q')
    # Si el usuario busca algo en la barra, filtramos; si no, trae todos
    if query:
        profesores = Profesor.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(profesion__icontains=query)
        )
    else:
        profesores = Profesor.objects.all()
        
    return render(request, 'myapp/profesores.html', {'profesores': profesores, 'query': query})

def profesor_editar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('myapp:profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'myapp/profesor_editar.html', {'form': form, 'profesor': profesor})

def profesor_eliminar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('myapp:profesores')
    return render(request, 'myapp/profesor_confirm_delete.html', {'profesor': profesor})

def detalle_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, 'myapp/profesores.html', {'profesor': profesor})

# Vistas para Cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html', {'cursos': cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'myapp/curso_detail.html', {'curso': curso})

# Vistas para Entregables
def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html', {'entregables': entregables})

def detalle_entregable(request, pk):
    entregable = get_object_or_404(Entregable, pk=pk)
    return render(request, 'myapp/entregable_detail.html', {'entregable': entregable})