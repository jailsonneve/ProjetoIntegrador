from django.db import models
from motoristas.models import Motorista

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"