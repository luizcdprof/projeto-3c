from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome_completo', 'bio')
    search_fields = ('user__username', 'nome_completo')