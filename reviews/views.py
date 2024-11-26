from django.shortcuts import render, get_object_or_404
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()  # Obtiene todos los libros
    return render(request, 'reviews/lista_libros.html', {'libros': libros})

def detalles_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  # Busca el libro por su ID (pk)
    return render(request, 'reviews/detalles_libro.html', {'libro': libro})
