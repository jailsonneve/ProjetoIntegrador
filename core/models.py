from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from diario.models import Diario
from motoristas.models import Motorista
from rotas.models import Rota
from veiculos.models import Veiculo


class Filial(models.Model):
    nome = models.CharField(max_length=100)

    cidade = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    filial = models.ForeignKey(
        Filial,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    is_gerente = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class FilialCliente(models.Model):
    cliente = models.OneToOneField(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, null=True, blank=True, on_delete=models.CASCADE)
class FilialFornecedores(models.Model):
    fornecedor = models.OneToOneField(Fornecedor, null=True, blank=True, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, null=True, blank=True, on_delete=models.CASCADE)
class FilialDiario(models.Model):
    diario = models.OneToOneField(Diario, null=True, blank=True, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, null=True, blank=True, on_delete=models.CASCADE)
class FilialMotoristas(models.Model):
    motorista = models.OneToOneField(Motorista, null=True, blank=True, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, null=True, blank=True, on_delete=models.CASCADE)
class FilialRotas(models.Model):
    rotas = models.OneToOneField(Rota, null=True, blank=True, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, null=True, blank=True, on_delete=models.CASCADE)
class FilialVeiculos(models.Model):
    veiculos = models.OneToOneField(Veiculo, null=True, blank=True, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, null=True, blank=True, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)