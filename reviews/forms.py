from django import forms
from .models import Usuario, Libro

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control'})
        }


class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'})
        }