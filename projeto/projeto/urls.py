from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('monitoramento/', include('monitoramento.urls')),
    path('admin/', admin.site.urls),
]

