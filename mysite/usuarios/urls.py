from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.usuarios_criar, name='usuarios_criar'),
    path('listar/', views.usuarios_listar, name='usuarios_listar'),
    path('login/', views.usuarios_login, name='login'),
    path('logout/', views.usuarios_logout, name='logout'),
]