from django.db import models
from motoristas.models import Motorista
from django.contrib.auth.models import User

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    cor = models.CharField(max_length=50, default='Desconhecida', blank=False)
    criado_por = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"