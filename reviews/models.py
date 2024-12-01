from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre_usuario

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=100)
    texto = models.TextField()
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_usuario} - {self.libro.titulo}"