from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import Usuario
from .models import Livro, Estante
from .forms import LivroForm

@login_required
def livros_cadastrar(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.cadastrado_por = request.user

            if livro.isbn:
                if Livro.objects.filter(isbn=livro.isbn).exists():
                    messages.error(request, "Já existe um livro com esse ISBN.")
                    return redirect('livros_catalogo')
            livro.save()

            if not livro.isbn:
                Estante.objects.create(usuario=request.user, livro=livro)
                messages.success(request, "Livro cadastrado e adicionado à sua estante.")
                return redirect('livros_estante')
            else:
                request.session['livro_recente_id'] = livro.id
                return redirect('livros_adicionar_estante_confirmacao')

    else:
        form = LivroForm()

    return render(request, 'livros_cadastrar.html', {'form': form})

@login_required
def livros_adicionar_estante_confirmacao(request):
    livro_id = request.session.get('livro_recente_id')
    if not livro_id:
        return redirect('livros_catalogo')

    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        if 'adicionar' in request.POST:
            Estante.objects.create(usuario=request.user, livro=livro)
            messages.success(request, "Livro adicionado à sua estante.")
        return redirect('livros_estante')

    return render(request, 'livros_adicionar_estante_confirmacao.html', {'livro': livro})

@login_required
def livros_excluir(request, id):
    livro = get_object_or_404(Livro, id=id, cadastrado_por=request.user)

    if livro.isbn:
        messages.error(request, "Não é possível excluir livros com ISBN.")
        return redirect('livros_estante')

    livro.delete()
    messages.success(request, "Livro excluído com sucesso.")
    return redirect('livros_estante')

from django.db.models import Avg

@login_required
def livros_estante(request):
    estante = Estante.objects.filter(usuario=request.user).select_related('livro')
    return render(request, 'livros_estante.html', {'estante': estante})

@login_required
def livros_catalogo(request):
    livros = Livro.objects.filter(isbn__isnull=False)
    estante_usuario = Estante.objects.filter(usuario=request.user).values_list('livro_id', flat=True)
    avaliacoes = Estante.objects.values('livro_id').annotate(media=Avg('avaliacao'))

    # media_dict = {a['livro_id']: a['media'] for a in avaliacoes}
    # for livro in livros:
    #     livro.media = avaliacoes.get(livro.id, 0)

    return render(request, 'livros_catalogo.html', {
        'livros': livros,
        'estante_ids': set(estante_usuario)
    })

@login_required
def adicionar_ou_remover_estante(request, id):
    livro = get_object_or_404(Livro, id=id)
    estante_item = Estante.objects.filter(usuario=request.user, livro=livro).first()

    if estante_item:
        estante_item.delete()
        messages.success(request, "Livro removido da estante.")
    else:
        Estante.objects.create(usuario=request.user, livro=livro)
        messages.success(request, "Livro adicionado à estante.")

    return redirect('livros_catalogo')

@login_required
def estante_remover(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    # Remove o livro da estante do usuário (usando User)
    Estante.objects.filter(usuario=request.user, livro=livro).delete()
    
    return redirect('livros_estante')
