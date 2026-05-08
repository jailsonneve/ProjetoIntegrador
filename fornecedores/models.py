from django.db import models

class Fornecedor(models.Model):

    TIPOS = [
        ('manutencao', 'Manutenção'),
        ('combustivel', 'Combustível'),
        ('pecas', 'Peças'),
    ]

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)


    tipo_servico = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome