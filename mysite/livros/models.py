from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
User = settings.AUTH_USER_MODEL

class Author(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Genre(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    ano_publicacao = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, blank=True, null=True, unique=True)
    editora = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='livros/', blank=True, null=True)
    possui = models.BooleanField(default=False)
    lido = models.BooleanField(default=False)
    cadastrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Estante(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    avaliacao = models.IntegerField(default=0)

    class Meta:
        unique_together = ('usuario', 'livro')  # Evita duplicidade na estante

    def __str__(self):
        return f"{self.usuario} - {self.livro}"
