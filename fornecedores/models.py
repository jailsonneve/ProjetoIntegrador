from django.db import models
from django.contrib.auth.models import User

class Fornecedor(models.Model):

    TIPOS = [
        ('manutencao', 'Manutenção'),
        ('combustivel', 'Combustível'),
        ('pecas', 'Peças'),
    ]

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    criado_por = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


    tipo_servico = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome