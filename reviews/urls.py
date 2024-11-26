from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalles_libro, name='detalles_libro'),
    path('resenas/', views.lista_resenas, name='lista_resenas'),  # Nueva URL para las reseñas
]