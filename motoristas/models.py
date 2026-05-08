from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True, null=True, unique=True)
    cnh = models.CharField(max_length=20)

    def __str__(self):
        return self.nome