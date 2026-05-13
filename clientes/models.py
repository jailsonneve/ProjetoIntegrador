from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    endereco = models.TextField()
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    cnh = models.CharField(max_length=11, unique=True, null=True, blank=True)
    criado_por = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    @property
    def cpf_formatado(self):

        if not self.cpf:
            return '-'

        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
    
    @property
    def telefone_formatado(self):

        if not self.telefone:
            return '-'

        if len(self.telefone) == 11:
            return f'({self.telefone[:2]}) {self.telefone[2:7]}-{self.telefone[7:]}'

        return f'({self.telefone[:2]}) {self.telefone[2:6]}-{self.telefone[6:]}'

    def __str__(self):
        return self.nome