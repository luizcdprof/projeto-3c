from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'genero', 'ano_publicacao', 'isbn', 'editora', 'capa', 'possui', 'lido']
