from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    empresa = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.empresa}"