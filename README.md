Criar projeto Backend-django
Executar o projeto no Firebase

No terminal:
source .venv/bin/activate
cd mysite
django-admin startapp usuarios
django-admin startapp livros
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Na linha 29 do settings.py, adicionar:
CSRF_TRUSTED_ORIGINS = [
    'endereço-do-erro-do-login-do-admin'
]

Na linha 42 (INSTALLED_APPS):
'usuarios',
'livros'

Na linha 108:
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = False

usuarios:
Criar o arquivo urls.py e colocar o código do github nele.
Criar a pasta "templates", e os arquivos dentro dela:
 -usuarios_criar.html 
 -usuarios_listar.html

livros:
Criar o arquivo urls.py e colocar o código do github nele.
Criar a pasta "templates", e os arquivos dentro dela:
 -livros_criar.html 
 -livros_listar.html

Adicionar os novos arquivos urls em mysite/urls.py
