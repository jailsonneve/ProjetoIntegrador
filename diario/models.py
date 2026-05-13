from django.db import models
from rotas.models import Rota
from django.contrib.auth.models import User

class Diario(models.Model):
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"Diário - {self.rota}"