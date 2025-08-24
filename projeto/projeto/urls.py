from django.urls import path, include

urlpatterns = [
    path('monitoramento/', include('monitoramento.urls')),
]

