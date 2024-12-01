from django.urls import path
from . import views

urlpatterns = [
    
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalles_libro, name='detalles_libro'),
    path('resenas/', views.lista_resenas, name='lista_resenas'),
    
    path('libro/crear/', views.crear_libro, name='crear_libro'),
    path('usuario/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]
