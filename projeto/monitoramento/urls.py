from django.urls import path
from . import views #esse ponto puxa os arquivos a partir da pasta projeto

#rotas globais

urlpatterns = [
    path('leituras/ultima/', views.ultima_leitura),
    path('leituras/nova/', views.registrar_leitura),
    path('dashboard', views.dashboard)
]
