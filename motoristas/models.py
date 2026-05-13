from django.db import models
from django.contrib.auth.models import User

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100, blank=True, null=True, unique=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    cnh = models.CharField(max_length=11, unique=True)
    criado_por = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nome