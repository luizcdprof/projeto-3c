from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UsuariosCriarForm
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'home.html')

def usuarios_criar(request):
    if request.method == 'POST':
        form = UsuariosCriarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('usuarios_listar')
    else:
        form = UsuariosCriarForm()
    
    return render(request, 'usuarios_criar.html', {'form': form})

def usuarios_listar(request):
    usuarios = Usuario.objects.all()
    print('IMPRIMIR USUARIOS:')
    for usuario in usuarios:
        print(usuario.id)
    return render(request, 'usuarios_listar.html', {'usuarios': usuarios})

def usuarios_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.username}!')
            return redirect('home')  # ou para onde quiser
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    
    return render(request, 'usuarios_login.html')

def usuarios_logout(request):
    logout(request)
    messages.info(request, 'Você saiu com sucesso.')
    return redirect('home')