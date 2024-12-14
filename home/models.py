import locale
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    estoque = models.CharField(max_length=50)
    ordem = models.IntegerField()
    
    def __str__(self):
        return self.nome