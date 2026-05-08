from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, blank=True, null=True, unique=True)
    cnh = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome