from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Resena, Usuario  
from .forms import FormularioUsuario, FormularioLibro


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'reviews/lista_libros.html', {'libros': libros})

def detalles_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'reviews/detalles_libro.html', {'libro': libro})

def lista_resenas(request):
    resenas = Resena.objects.all()
    return render(request, 'reviews/lista_resenas.html', {'resenas': resenas})

def crear_libro(request):
    if request.method == 'POST':
        formulario = FormularioLibro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_libros')
    else:
        formulario = FormularioLibro()
    return render(request, 'reviews/formulario_libro.html', {'formulario': formulario})

def crear_usuario(request):
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')
    else:
        formulario = FormularioUsuario()
    return render(request, 'reviews/formulario_usuario.html', {'formulario': formulario})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'reviews/lista_usuarios.html', {'usuarios': usuarios})