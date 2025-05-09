# Instruções do projeto
## No Firebase Studio (studio.firebase.google.com):
* Criar projeto Backend-django
* Executar o projeto no Firebase

## Atualizar o arquivo requirements.txt
### No final do arquivo, adicionar:
* pillow==11.2.1

## No terminal:
* source .venv/bin/activate
* cd mysite
* pip install -r requirements.txt
* django-admin startapp usuarios
* django-admin startapp livros
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver

## Acessar o projeto para obter o endereço pra liberar o CSRF 
* Segure o "ctrl" e clique no endereço IP que está no terminal (http://127.0.0.1:8000/)
* Vai aparecer a janela do django com o foguete. Clique na barra de endereços e adicione "/admin" ao final
* Faça o login com o usuário e senha criados no comando createsuperuser
* Irá aparecer uma janela com erro. Nessa janela, abaixo do texto em negrito "Help", na linha escrito "Origin checking failed - ", tem o endereço que começa com "https" e termina com ".dev". Esse endereço que será usado na linha 30 do settings.py.
 
## mysite/mysite/settings.py
### Na linha 14:
* import os

### Na linha 30:
```
CSRF_TRUSTED_ORIGINS = [
     'endereço-do-erro-do-login-do-admin'
]
```

### Na linha 43 (INSTALLED_APPS):
```
'usuarios',
'livros'
```

### Na linha 62:
```
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

### Na linha 111:
```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = False
```

### Na linha 124:
```
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## mysite/
### Criar os arquivos e/ou copiar o código do github:
* static/images/default_book.png

## mysite/mysite/
### Criar os arquivos e/ou copiar o código do github:
* urls.py:

## mysite/templates/
### Criar os arquivos e/ou copiar o código do github:
* base.html
* home.html

## mysite/usuarios/
### Criar os arquivos e/ou copiar o código do github:
* admin.py
* forms.py
* models.py
* urls.py
* views.py
* templates/usuarios_criar.html
* templates/usuarios_listar.html
* templates/usuarios_login.html

## mysite/livros/
### Criar os arquivos e/ou copiar o código do github:
* admin.py
* forms.py
* models.py
* urls.py
* views.py
* templates/livros_adicionar_estante_confirmacao.html
* templates/livros_cadastrar.html
* templates/livros_catalogo.html
* templates/livros_estante.html
* templates/livros_listar.html

## No terminal:
* source .venv/bin/activate
* cd mysite
* python manage.py collectstatic
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

## Acessar o sistema:
* Segure o "control" e clique no endereço IP que for exibido no terminal (http://127.0.0.1:8000/)
