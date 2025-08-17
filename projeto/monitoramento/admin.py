from django.contrib import admin
from .models import Leituras

@admin.register(Leituras)
class MonitoramentoAdmin(admin.ModelAdmin):
    list_display = ('temperatura' , 'ph', 'tds', 'data_hora' )
