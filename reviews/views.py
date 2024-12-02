from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Resena, Usuario  
from .forms import FormularioUsuario, FormularioLibro
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect

def lista_libros(request):
    if 'usuario_id' not in request.session:
        return HttpResponseRedirect('/login/')  # Redirige si no est� autenticado
    libros = Libro.objects.all()
    return render(request, 'reviews/lista_libros.html', {'libros': libros, 'usuario_nombre': request.session.get('usuario_nombre')})

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
            usuario = formulario.save(commit=False)
            # Hash de la contrasena
            usuario.contrasena = make_password(usuario.contrasena)
            usuario.save()
            return redirect('login_usuario')  # Redirige al login
    else:
        formulario = FormularioUsuario()
    return render(request, 'reviews/formulario_usuario.html', {'formulario': formulario})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'reviews/lista_usuarios.html', {'usuarios': usuarios})

def login_usuario(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(contrasena, usuario.contrasena):
                # Usa la sesi�n para autenticar
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre_usuario
                return redirect('lista_libros')  # Redirige a la lista de libros
            else:
                return render(request, 'reviews/login.html', {'error': 'Contrasena incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'reviews/login.html', {'error': 'Usuario no encontrado'})
    return render(request, 'reviews/login.html')

def logout_usuario(request):
    request.session.flush()  # Limpia la sesi�n
    return redirect('login_usuario')
