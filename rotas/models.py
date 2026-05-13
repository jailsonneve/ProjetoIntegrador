from django.db import models
from motoristas.models import Motorista
from veiculos.models import Veiculo
from clientes.models import Cliente
from django.contrib.auth.models import User

class Rota(models.Model):

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    data = models.DateField()
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco_entrega = models.TextField()
    criado_por = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} - {self.cliente.nome}"