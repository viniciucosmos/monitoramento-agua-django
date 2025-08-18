from django.contrib import admin
from django.urls import path, include
from . import views #esse ponto puxa os arquivos a partir da pasta projeto

#rotas globais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste_view),
    path('auth/', include('rest_framework.urls'))
]

