
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    nombre_usuario = models.CharField(max_length=100)  # Nombre del usuario
    texto = models.TextField()  # Texto de la reseña
    calificacion = models.PositiveSmallIntegerField()  # Calificación del libro (ej. de 1 a 5)

    def __str__(self):
        return f"Reseña de {self.nombre_usuario} para {self.libro}"
