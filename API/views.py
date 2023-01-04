from django.shortcuts import render
from rest_framework import viewsets
from .models import ListaDeTarefas
from .serializer import ListaSerializer

class ListaViewSets(viewsets.ModelViewSet):
    queryset = ListaDeTarefas.objects.all()
    serializer_class = ListaSerializer
    http_method_names = ['get', 'head']
