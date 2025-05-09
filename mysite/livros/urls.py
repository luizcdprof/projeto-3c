from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.livros_listar, name='livros_listar'),
    path('cadastrar/', views.livros_cadastrar, name='livros_cadastrar'),
    path('excluir/<int:id>/', views.livros_excluir, name='livros_excluir'),
    path('estante/', views.livros_estante, name='livros_estante'),
    path('estante/remover/<int:livro_id>/', views.estante_remover, name='estante_remover'),
    path('catalogo/', views.livros_catalogo, name='livros_catalogo'),
    path('catalogo/toggle/<int:id>/', views.adicionar_ou_remover_estante, name='livros_toggle_estante'),
    path('confirmar-estante/', views.livros_adicionar_estante_confirmacao, name='livros_adicionar_estante_confirmacao'),
]
