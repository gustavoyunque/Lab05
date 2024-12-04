from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_base, name='pagina_base'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalles_libro, name='detalles_libro'),
    path('resenas/', views.lista_resenas, name='lista_resenas'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
     path('login/', views.login_usuario, name='login_usuario'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
]
