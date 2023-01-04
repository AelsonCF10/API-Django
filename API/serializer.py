from rest_framework import serializers
from .models import ListaDeTarefas

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeTarefas
        fields = ['title', 'descricao', 'data_inicio', 'data_de_encerramento']
        