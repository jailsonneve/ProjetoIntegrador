from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from fornecedores.models import Fornecedor
from veiculos.models import Veiculo


class Manutencao(models.Model):

    TIPOS = [
        ('preventiva', 'Preventiva'),
        ('corretiva', 'Corretiva'),
    ]

    # CASCADE segue o padrão do projeto (Rota, Veiculo...). Com PROTECT, a view
    # deletar_veiculo quebraria (ProtectedError) para veículos com manutenção.
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name='manutencoes',
    )
    # Oficina responsável (opcional)
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='manutencoes',
        verbose_name='Oficina',
    )
    data_manutencao = models.DateField('Data da manutenção')
    tipo = models.CharField('Tipo', max_length=20, choices=TIPOS)
    descricao = models.TextField('Descrição')
    custo = models.DecimalField(
        'Custo (R$)',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'
        ordering = ['-data_manutencao', '-id']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.veiculo} ({self.data_manutencao:%d/%m/%Y})"
