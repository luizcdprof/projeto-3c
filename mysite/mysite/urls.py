from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from usuarios.views import home  # importa a view da home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # raiz do site
    path('usuarios/', include('usuarios.urls')),
    path('livros/', include('livros.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)