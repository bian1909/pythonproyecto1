# Proyecto 1 - Gestión de Cursos 

Este proyecto es una aplicación web desarrollada en **Django** como parte de la cátedra de Laboratorio de Programación Avanzada. La plataforma permite administrar de manera eficiente la información de una institución educativa, gestionando alumnos, cursos, entregables y profesores.

## Funcionalidades Principales
* **Buscador de Profesores:** Filtrado en tiempo real por nombre, apellido o profesión.
* **CRUD Completo de Profesores:** Vistas dedicadas para listar, añadir, editar y eliminar registros de docentes.
* **Panel de Administración:** Configuración de modelos (`Estudiante`, `Profesor`, `Curso`, `Entregable`) integrados con el panel de Django.
* **Interfaz Visual:** Maquetado responsivo utilizando componentes de Bootstrap.

## Integrantes
* **Longoni Bianca**
* **Seiber Facundo David**

## Tecnologías Utilizadas
* Python 3.x
* Django 6.x
* SQLite3
* Bootstrap / HTML5

## Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/bian1909/pythonproyecto1.git](https://github.com/bian1909/pythonproyecto1.git)
   cd pythonproyecto1

2. Crear y activar el entorno virtual:
   python -m venv .venv
# En Windows:
.\.venv\Scripts\activate

3. Instalar Django y levantar el servidor:
pip install django
python manage.py migrate
python manage.py runserver

