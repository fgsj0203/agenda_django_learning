from django.contrib import admin
from core.models import Evento

# Register your models here.
#Registrar o model criado

class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo","data_evento","data_criacao")
    list_filter = ("titulo","usuario")


admin.site.register(Evento, EventoAdmin)
