from django.contrib import admin
from .models import Livro, Author, Genre

# Register your models here.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero')
    search_fields = ('titulo', 'autor')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)