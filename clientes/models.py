from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome