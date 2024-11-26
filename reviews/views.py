from django.shortcuts import render, get_object_or_404
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def detalles_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'detalles_libro.html', {'libro': libro})

