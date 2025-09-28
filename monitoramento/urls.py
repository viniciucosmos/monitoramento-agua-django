from django.urls import path
from . import views #esse ponto puxa os arquivos a partir da pasta projeto

#rotas globais
#Para poder usar a navbar com {% url %}, precisa dar nomes para as rotas.

urlpatterns = [
    path('leituras/ultima/', views.ultima_leitura, name="ultima_leitura"),
    path('leituras/nova/', views.registrar_leitura, name="registrar_leitura"),
    path('dashboard/', views.dashboard, name="dashboard"),   
    path('duvidas/', views.duvidas, name="duvidas"),        
]
