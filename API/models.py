from django.db import models

class ListaDeTarefas(models.Model):
    title = models.CharField(max_length=75)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateTimeField()
    data_de_encerramento = models.DateTimeField()

    def __str__(self):
        return self.title
