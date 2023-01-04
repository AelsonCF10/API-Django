from django.contrib import admin
from .models import ListaDeTarefas

class ListaAdmin(admin.ModelAdmin):
    model = ListaDeTarefas
    list_display = ('title', 'data_inicio', 'data_de_encerramento')


admin.site.register(ListaDeTarefas, ListaAdmin)