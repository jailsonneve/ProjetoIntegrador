from django.db import models
from rotas.models import Rota

class Diario(models.Model):
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diário - {self.rota}"