No Firebase Studio (studio.firebase.google.com)
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

Na linha 14 do settings.py, adicionar:
import os

Na linha 30 do settings.py, adicionar:
CSRF_TRUSTED_ORIGINS = [
    'endereço-do-erro-do-login-do-admin'
]

Na linha 43 (INSTALLED_APPS):
'usuarios',
'livros'

Na linha 62:
'DIRS': [os.path.join(BASE_DIR, 'templates')],

Na linha 111:
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = False

Criar o arquivo de base dos templates em mysite/templates/base.html e copiar o código do github nele.

usuarios:
Criar o arquivo urls.py e colocar o código do github nele.
Criar a pasta "templates", os arquivos dentro dela e copiar o código do github neles:
 -usuarios_criar.html
 -usuarios_listar.html

livros:
Criar o arquivo urls.py e colocar o código do github nele.
Criar a pasta "templates", e os arquivos dentro dela:
 -livros_criar.html 
 -livros_listar.html

Adicionar os novos arquivos urls em mysite/urls.py (linha 6):
path('usuarios/', include('usuarios.urls')),
path('livros/', include('livros.urls'))