from django.contrib import admin
from django.urls import path
from . import views #esse ponto puxa os arquivos a partir da pasta projeto

#rotas globais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste_view),
    path('leituras/ultima/', views.ultima_leitura),
]
